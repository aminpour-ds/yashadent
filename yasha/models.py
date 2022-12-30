from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.contrib import admin
from .validators import validate_file_size


class Department(models.Model):
    name = models.CharField(("نام بخش"), max_length=150)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'بخش'


class ServiceType(models.Model):
    name = models.CharField(("نوع خدمت"), max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'نوع خدمت'
        ordering = ['id']


class Service(models.Model):
    ServiceTypeID = models.ForeignKey(ServiceType, on_delete=models.PROTECT, related_name='service', verbose_name=("نوع خدمت"))
    name = models.CharField(("نام خدمت"), max_length=150)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='service', verbose_name=("نام بخش"))
    cost = models.BigIntegerField(("( ریال ) هزینه"), validators=[MinValueValidator(1)])
    duration = models.DurationField(("مدت زمان"), default=None)
    active = models.BooleanField(("فعال"))

    class Meta:
        verbose_name_plural = 'خدمات'
        ordering = ['id']


class Insurance(models.Model):
    name = models.CharField(("نام بیمه"), max_length=150)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'بیمه'


class Patient(models.Model):
    REFERRER_PERSON = 'Person'
    REFERRER_INSTAGRAM = 'Instagram'
    REFERRER_INTERNET = 'Internet'
    REFERRER_TRACT = 'Tract'
    REFERRER_ORGANIZATION = 'Organization'

    REFERRER_CHOICES = [
        (REFERRER_PERSON, 'شخص'),
        (REFERRER_INSTAGRAM, 'اینستاگرام'),
        (REFERRER_INTERNET, 'اینترنت'),
        (REFERRER_TRACT, 'تراکت'),
        (REFERRER_ORGANIZATION, 'سازمان')
    ]

    GENDER_MAN = 'man'
    GENDER_WOMAN = 'woman'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = [
        (GENDER_MAN, 'مرد'),
        (GENDER_WOMAN, 'زن'),
        (GENDER_OTHER, 'سایر')
    ]
    
    first_name = models.CharField(("نام"), max_length=150)
    last_name = models.CharField(("نام خانوادگی"), max_length=150)
    father_name = models.CharField(("نام پدر"), max_length=150)
    identity = models.CharField(("کد ملی"), unique=True, max_length=20)
    phone = models.CharField(("تلفن"), max_length=255)
    mobile = models.CharField(("موبایل"), max_length=255)
    date_joined = models.DateField(("تاریخ پذیرش بیمار"), default=timezone.now)
    birth_date = models.DateField(("تاریخ تولد"))
    guardian = models.CharField(("کد ملی سرپرست بیمار"), max_length=20)
    referrer = models.CharField(("معرف"), max_length=20, choices=REFERRER_CHOICES, default=REFERRER_ORGANIZATION)
    gender = models.CharField(("جنسیت"), max_length=20, choices=GENDER_CHOICES, default=GENDER_WOMAN)
    description = models.CharField(("توضیحات"), max_length=255, null=True, blank=True)
    email = models.EmailField(("ایمیل"), blank=True, unique=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.PROTECT, related_name='patient', verbose_name=("نام بیمه"))
    start_date_insurance = models.DateField(("تاریخ شروع بیمه"))
    end_date_insurance = models.DateField(("تاریخ پایان بیمه"))

    def __str__(self):
        return self.identity

    class Meta:
        verbose_name_plural = 'بیماران'
        ordering = ['first_name', 'last_name']


class Doctor(models.Model):
    GENDER_MAN = 'man'
    GENDER_WOMAN = 'woman'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = [
        (GENDER_MAN, 'مرد'),
        (GENDER_WOMAN, 'زن'),
        (GENDER_OTHER, 'سایر')
    ]
    
    identity = models.CharField(("کد ملی"), unique=True, max_length=20)
    professionalStatement = models.CharField(("تخصص"), max_length=255, null=True)
    phone = models.CharField(("تلفن"), max_length=255)
    mobile = models.CharField(("موبایل"), max_length=255)
    gender = models.CharField(("جنسیت"), max_length=20, choices=GENDER_CHOICES, default=GENDER_WOMAN)
    Contract = models.DecimalField(("درصد قرارداد"), max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=("کاربر"))

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    class Meta:
        verbose_name_plural = 'پزشکان'
        ordering = ['user__first_name', 'user__last_name']


class DoctorImage(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='yasha/images/doctor', validators=[validate_file_size])        


class Review(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'نظر بیمار'

    class Meta:
        verbose_name_plural = 'نظر بیماران'