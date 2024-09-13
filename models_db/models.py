# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EAcademicInformation(models.Model):
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING, db_column='_education_year',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_marking_system = models.ForeignKey('HMarkingSystem', models.DO_NOTHING,
                                             db_column='_marking_system')  # Field renamed because it started with '_'.
    field_decree = models.ForeignKey('EDecree', models.DO_NOTHING, db_column='_decree', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    academic_number = models.CharField(max_length=20, blank=True, null=True)
    academic_register_number = models.CharField(unique=True, max_length=30, blank=True, null=True)
    academic_register_date = models.DateField(blank=True, null=True)
    academic_status = models.CharField(max_length=64, blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    rector = models.CharField(max_length=255, blank=True, null=True)
    dean = models.CharField(max_length=255, blank=True, null=True)
    secretary = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_university = models.ForeignKey('EUniversity', models.DO_NOTHING, db_column='_university', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    university_name = models.CharField(max_length=255, blank=True, null=True)
    faculty_name = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    student_birthday = models.DateField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    field_curriculum = models.ForeignKey('ECurriculum', models.DO_NOTHING, db_column='_curriculum', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    curriculum_name = models.CharField(max_length=255, blank=True, null=True)
    student_status = models.CharField(max_length=255, blank=True, null=True)
    education_type_name = models.CharField(max_length=255, blank=True, null=True)
    education_form_name = models.CharField(max_length=255, blank=True, null=True)
    specialty_name = models.CharField(max_length=255, blank=True, null=True)
    specialty_code = models.CharField(max_length=255, blank=True, null=True)
    year_of_entered = models.CharField(max_length=255, blank=True, null=True)
    year_of_graduated = models.CharField(max_length=255, blank=True, null=True)
    field_semester = models.CharField(db_column='_semester', max_length=64, blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    semester_name = models.CharField(max_length=255, blank=True, null=True)
    subjects_count = models.IntegerField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_academic_information'
        db_table_comment = 'Akademik ma`lumotnoma ma`lumotlari'


class EAcademicInformationData(models.Model):
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester', max_length=64, blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_university = models.ForeignKey('EUniversity', models.DO_NOTHING, db_column='_university', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_decree = models.ForeignKey('EDecree', models.DO_NOTHING, db_column='_decree', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING, db_column='_education_year',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING, db_column='_education_type',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING, db_column='_education_form',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey('ECurriculum', models.DO_NOTHING, db_column='_curriculum', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    student_birthday = models.DateField(blank=True, null=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)
    blank_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    register_number = models.CharField(unique=True, max_length=30, blank=True, null=True)
    register_date = models.DateField(blank=True, null=True)
    given_city = models.CharField(max_length=255, blank=True, null=True)
    semester_name = models.CharField(max_length=255, blank=True, null=True)
    university_name = models.CharField(max_length=255, blank=True, null=True)
    rector_fullname = models.CharField(max_length=255, blank=True, null=True)
    dean_fullname = models.CharField(max_length=255, blank=True, null=True)
    secretary_fullname = models.CharField(max_length=255, blank=True, null=True)
    faculty_name = models.CharField(max_length=255, blank=True, null=True)
    continue_start_date = models.DateField(blank=True, null=True)
    continue_end_date = models.DateField(blank=True, null=True)
    moved_hei_name = models.CharField(max_length=1000, blank=True, null=True)
    studied_start_date = models.DateField(blank=True, null=True)
    studied_end_date = models.DateField(blank=True, null=True)
    specialty_name = models.CharField(max_length=255, blank=True, null=True)
    specialty_code = models.CharField(max_length=100, blank=True, null=True)
    accumulated_points = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    passing_score = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    last_education = models.CharField(max_length=255, blank=True, null=True)
    expulsion_decree_reason = models.CharField(max_length=255, blank=True, null=True)
    expulsion_decree_number = models.CharField(max_length=255, blank=True, null=True)
    expulsion_decree_date = models.DateField(blank=True, null=True)
    education_form_name = models.CharField(max_length=255, blank=True, null=True)
    academic_data_status = models.CharField(max_length=64, blank=True, null=True)
    subjects_count = models.IntegerField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    education_form_name_moved = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_academic_information_data'
        unique_together = (('field_student', 'field_student_meta'),)
        db_table_comment = 'Akademik ma`lumotnoma ma`lumotlari (transkript emas)'


class EAcademicInformationDataSubject(models.Model):
    field_academic_information_data = models.ForeignKey(EAcademicInformationData, models.DO_NOTHING,
                                                        db_column='_academic_information_data')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey('ECurriculum', models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    curriculum_name = models.CharField(max_length=256)
    education_year_name = models.CharField(max_length=255)
    semester_name = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    total_acload = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_point = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_academic_information_data_subject'
        db_table_comment = 'Akademik ma`lumotnoma fanlari ma`lumotlari'


class EAcademicRecord(models.Model):
    field_curriculum = models.ForeignKey('ECurriculum', models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester', max_length=64, blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    curriculum_name = models.CharField(max_length=256)
    education_year_name = models.CharField(max_length=256)
    semester_name = models.CharField(max_length=256, blank=True, null=True)
    student_name = models.CharField(max_length=256)
    student_id_number = models.CharField(max_length=20, blank=True, null=True)
    subject_name = models.CharField(max_length=256)
    total_acload = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_point = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_employee = models.IntegerField(db_column='_employee', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    employee_name = models.CharField(max_length=256, blank=True, null=True)
    finish_credit_status = models.BooleanField(blank=True, null=True)
    retraining_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_academic_record'
        db_table_comment = 'Akademik ma`lumotnoma (transkript) ma`lumotlari'


class EAdmin(models.Model):
    login = models.CharField(unique=True, max_length=255)
    field_role = models.ForeignKey('EAdminRole', models.DO_NOTHING, db_column='_role', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=64, blank=True, null=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
    full_name = models.CharField(max_length=128, blank=True, null=True)
    auth_key = models.CharField(max_length=32, blank=True, null=True)
    access_token = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password_reset_token = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password_reset_date = models.DateTimeField(blank=True, null=True)
    image = models.JSONField(blank=True, null=True)
    language = models.CharField(max_length=32)
    status = models.CharField(max_length=32)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    field_employee = models.ForeignKey('EEmployee', models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    password_valid = models.BooleanField(blank=True, null=True)
    password_date = models.DateTimeField(blank=True, null=True)
    user_uuid = models.UUIDField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_admin'


class EAdminGroup(models.Model):
    field_admin = models.ForeignKey(EAdmin, models.DO_NOTHING, db_column='_admin', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_admin_group'


class EAdminMessage(models.Model):
    field_forwarded = models.ForeignKey('self', models.DO_NOTHING, db_column='_forwarded', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_replied = models.ForeignKey('self', models.DO_NOTHING, db_column='_replied',
                                      related_name='eadminmessage_field_replied_set', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_sender = models.ForeignKey('EAdminMessageContact', models.DO_NOTHING, db_column='_sender', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_item = models.ForeignKey('EAdminMessageItem', models.DO_NOTHING, db_column='_item', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_recipients = models.JSONField(db_column='_recipients', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    sender_data = models.JSONField(blank=True, null=True)
    recipient_data = models.JSONField(blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    files = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    status_bd = models.CharField(max_length=16, blank=True, null=True)
    r_count = models.IntegerField(blank=True, null=True)
    send_on = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_admin_message'


class EAdminMessageContact(models.Model):
    name = models.CharField(max_length=2048, blank=True, null=True)
    label = models.CharField(max_length=2048, blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_admin = models.OneToOneField(EAdmin, models.DO_NOTHING, db_column='_admin', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_student = models.OneToOneField('EStudent', models.DO_NOTHING, db_column='_student', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey('EEmployee', models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_role = models.ForeignKey('EAdminRole', models.DO_NOTHING, db_column='_role', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_student_department = models.ForeignKey('EDepartment', models.DO_NOTHING, db_column='_student_department',
                                                 related_name='eadminmessagecontact_field_student_department_set',
                                                 blank=True, null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_admin_message_contact'


class EAdminMessageContactUser(models.Model):
    field_contact = models.ForeignKey(EAdminMessageContact, models.DO_NOTHING, db_column='_contact', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_user = models.ForeignKey(EAdminMessageContact, models.DO_NOTHING, db_column='_user',
                                   related_name='eadminmessagecontactuser_field_user_set', blank=True,
                                   null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_admin_message_contact_user'
        unique_together = (('field_contact', 'field_user'),)


class EAdminMessageFolder(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    field_recipient = models.IntegerField(db_column='_recipient')  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_admin_message_folder'


class EAdminMessageItem(models.Model):
    field_message = models.ForeignKey(EAdminMessage, models.DO_NOTHING,
                                      db_column='_message')  # Field renamed because it started with '_'.
    field_sender = models.ForeignKey(EAdminMessageContact, models.DO_NOTHING,
                                     db_column='_sender')  # Field renamed because it started with '_'.
    field_recipient = models.ForeignKey(EAdminMessageContact, models.DO_NOTHING, db_column='_recipient',
                                        related_name='eadminmessageitem_field_recipient_set', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_folder = models.ForeignKey(EAdminMessageFolder, models.DO_NOTHING, db_column='_folder', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_label = models.ForeignKey(EAdminMessageFolder, models.DO_NOTHING, db_column='_label',
                                    related_name='eadminmessageitem_field_label_set', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    type = models.CharField(max_length=16, blank=True, null=True)
    opened = models.BooleanField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    starred = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    opened_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_admin_message_item'


class EAdminResource(models.Model):
    path = models.CharField(unique=True, max_length=128)
    name = models.CharField(unique=True, max_length=256)
    group = models.CharField(max_length=64)
    comment = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, db_comment='Is Resource is available to use')
    login = models.BooleanField(blank=True, null=True, db_comment='Should user logged in to access this resource')
    skip = models.BooleanField(blank=True, null=True, db_comment='Should FilterAccessControl skip this resource')
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_admin_resource'


class EAdminRole(models.Model):
    code = models.CharField(unique=True, max_length=32)
    name = models.CharField(unique=True, max_length=32)
    status = models.CharField(max_length=16)
    parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_admin_role'


class EAdminRoleResource(models.Model):
    field_role = models.ForeignKey(EAdminRole, models.DO_NOTHING, db_column='_role', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_resource = models.ForeignKey(EAdminResource, models.DO_NOTHING, db_column='_resource', blank=True,
                                       null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_admin_role_resource'


class EAdminRoles(models.Model):
    field_admin = models.ForeignKey(EAdmin, models.DO_NOTHING,
                                    db_column='_admin')  # Field renamed because it started with '_'.
    field_role = models.ForeignKey(EAdminRole, models.DO_NOTHING,
                                   db_column='_role')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_admin_roles'


class EAdmissionQuota(models.Model):
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING, db_column='_education_form',
                                             related_name='eadmissionquota_field_education_form_set')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING, db_column='_education_year',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    admission_quota = models.IntegerField()
    field_quota_type = models.ForeignKey('HPaymentForm', models.DO_NOTHING,
                                         db_column='_quota_type')  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    fixed_student_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_admission_quota'
        db_table_comment = 'Qabul kvotalari'


class EAttendance(models.Model):
    field_subject_schedule = models.ForeignKey('ESubjectSchedule', models.DO_NOTHING, db_column='_subject_schedule',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair', max_length=64, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    lesson_date = models.DateField()
    field_employee = models.ForeignKey('EEmployee', models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    absent_on = models.SmallIntegerField(blank=True, null=True)
    absent_off = models.SmallIntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_individual_training_subject_schedule = models.ForeignKey('EIndividualTrainingSubjectSchedule',
                                                                   models.DO_NOTHING,
                                                                   db_column='_individual_training_subject_schedule',
                                                                   blank=True,
                                                                   null=True)  # Field renamed because it started with '_'.
    start_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_attendance'
        unique_together = (('field_student', 'field_semester', 'field_subject', 'field_training_type',
                            'field_lesson_pair', 'lesson_date'),)
        db_table_comment = 'Bitiruvchi talabalarning ishga joylashish ma`lumotlari'


class EAttendanceActivity(models.Model):
    field_attendance = models.ForeignKey(EAttendance, models.DO_NOTHING,
                                         db_column='_attendance')  # Field renamed because it started with '_'.
    field_employee = models.IntegerField(db_column='_employee', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    accepted = models.BooleanField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    status_for_activity = models.IntegerField(blank=True, null=True)
    reworked_date = models.DateTimeField(blank=True, null=True)
    absent_on = models.SmallIntegerField(blank=True, null=True)
    absent_off = models.SmallIntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    file = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_attendance_activity'
        db_table_comment = 'Davomat faoliyati bo`yicha amallar'


class EAttendanceControl(models.Model):
    field_subject_schedule = models.ForeignKey('ESubjectSchedule', models.DO_NOTHING, db_column='_subject_schedule',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_group = models.IntegerField(db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey('EEmployee', models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair', max_length=64, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    lesson_date = models.DateField()
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    load = models.IntegerField(blank=True, null=True)
    field_individual_training_subject_schedule = models.ForeignKey('EIndividualTrainingSubjectSchedule',
                                                                   models.DO_NOTHING,
                                                                   db_column='_individual_training_subject_schedule',
                                                                   blank=True,
                                                                   null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING, db_column='_student', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    start_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_attendance_control'
        unique_together = (('field_employee', 'field_group', 'field_education_year', 'field_semester', 'field_subject',
                            'field_training_type', 'field_lesson_pair', 'lesson_date'),)
        db_table_comment = 'Davomat kiritilish holati'


class EAttendanceSettingBorder(models.Model):
    field_attendance_setting = models.ForeignKey('HAttendanceSetting', models.DO_NOTHING,
                                                 db_column='_attendance_setting', blank=True,
                                                 null=True)  # Field renamed because it started with '_'.
    field_marking_system = models.ForeignKey('HMarkingSystem', models.DO_NOTHING, db_column='_marking_system',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    min_border = models.IntegerField(blank=True, null=True)
    max_border = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_attendance_setting_border'
        unique_together = (('field_attendance_setting', 'field_marking_system'),)
        db_table_comment = 'Sinxronizatsiya modellari'


class EAuditorium(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    field_building = models.ForeignKey('HBuilding', models.DO_NOTHING, db_column='_building', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_auditorium_type = models.ForeignKey('HAuditoriumType', models.DO_NOTHING, db_column='_auditorium_type',
                                              blank=True, null=True)  # Field renamed because it started with '_'.
    volume = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    link = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_auditorium'
        db_table_comment = 'OTMdagi auditoriyalar ro`yxati'


class EBankDetails(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    position = models.IntegerField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_bank_details'
        db_table_comment = 'Bank rekvizitlari ma`lumotlari'


class ECallSheet(models.Model):
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_university = models.ForeignKey('EUniversity', models.DO_NOTHING,
                                         db_column='_university')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING,
                                    db_column='_level')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING, db_column='_education_year',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    sheet_number = models.CharField(unique=True, max_length=20, blank=True, null=True)
    register_date = models.DateField(blank=True, null=True)
    study_start_date = models.DateField(blank=True, null=True)
    study_end_date = models.DateField(blank=True, null=True)
    university_name = models.CharField(max_length=255, blank=True, null=True)
    faculty_name = models.CharField(max_length=255, blank=True, null=True)
    specialty_name = models.CharField(max_length=255, blank=True, null=True)
    specialty_code = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    level_name = models.CharField(max_length=255, blank=True, null=True)
    student_name = models.CharField(max_length=255, blank=True, null=True)
    university_address = models.CharField(max_length=255, blank=True, null=True)
    department_head = models.CharField(max_length=255, blank=True, null=True)
    education_type_name = models.CharField(max_length=255, blank=True, null=True)
    education_form_name = models.CharField(max_length=255, blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_call_sheet'
        db_table_comment = 'Chaqiruv qog`ozi ma`lumotlari'


class ECertificateCommittee(models.Model):
    name = models.CharField(max_length=128)
    field_education_type = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_faculty = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                      db_column='_faculty')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING, db_column='_department',
                                         related_name='ecertificatecommittee_field_department_set')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_certificate_committee'
        db_table_comment = 'Davlat attestatsiya komissiyasi'


class ECertificateCommitteeMember(models.Model):
    field_certificate_committee = models.ForeignKey(ECertificateCommittee, models.DO_NOTHING,
                                                    db_column='_certificate_committee')  # Field renamed because it started with '_'.
    name = models.CharField(max_length=128)
    work_place = models.CharField(max_length=256)
    position = models.CharField(max_length=128)
    role = models.CharField(max_length=64)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_certificate_committee_member'
        db_table_comment = "Davlat attestatsiya komissiyasi a'zolari"


class ECertificateCommitteeResult(models.Model):
    field_certificate_committee = models.ForeignKey(ECertificateCommittee, models.DO_NOTHING,
                                                    db_column='_certificate_committee')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_faculty = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                      db_column='_faculty')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING, db_column='_department',
                                         related_name='ecertificatecommitteeresult_field_department_set')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_graduate_work = models.ForeignKey('EGraduateQualifyingWork', models.DO_NOTHING,
                                            db_column='_graduate_work')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    order_number = models.CharField(max_length=32)
    order_date = models.DateField()
    grade = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    ball = models.IntegerField(blank=True, null=True)
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING, db_column='_subject', blank=True,
                                      null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_certificate_committee_result'
        db_table_comment = 'DAK natijalari'


class ECirculationSheet(models.Model):
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    student_name = models.CharField(max_length=256)
    student_id_number = models.CharField(max_length=20, blank=True, null=True)
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    group_name = models.CharField(max_length=256)
    field_payment_form = models.ForeignKey('HPaymentForm', models.DO_NOTHING,
                                           db_column='_payment_form')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    circulation_doc_number = models.CharField(max_length=20)
    circulation_doc_date = models.DateField()
    circulation_status = models.BooleanField(blank=True, null=True)
    checked_count = models.IntegerField(blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_circulation_sheet'
        unique_together = (('field_student', 'field_student_meta'),)
        db_table_comment = 'Bitiruvchilar aylanma varaqasi ma`lumotlari'


class ECirculationSheetMeta(models.Model):
    field_circulation_sheet = models.ForeignKey(ECirculationSheet, models.DO_NOTHING,
                                                db_column='_circulation_sheet')  # Field renamed because it started with '_'.
    field_role = models.ForeignKey(EAdminRole, models.DO_NOTHING, db_column='_role',
                                   to_field='code')  # Field renamed because it started with '_'.
    field_admin = models.ForeignKey(EAdmin, models.DO_NOTHING,
                                    db_column='_admin')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    circulation_sheet_comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_circulation_sheet_meta'
        db_table_comment = 'Bitiruvchilar aylanma varaqasini belgilash ma`lumotlari'


class EContractPrice(models.Model):
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING, db_column='_education_year',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING, db_column='_education_type',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_country = models.CharField(db_column='_country', max_length=64, blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_citizenship_type = models.ForeignKey('HCitizenshipType', models.DO_NOTHING, db_column='_citizenship_type',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_have_access_certificate = models.BooleanField(db_column='_have_access_certificate', blank=True,
                                                        null=True)  # Field renamed because it started with '_'.
    field_minimum_wage = models.ForeignKey('EMinimumWage', models.DO_NOTHING, db_column='_minimum_wage', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_contract_currency = models.ForeignKey('HProjectCurrency', models.DO_NOTHING,
                                                db_column='_contract_currency')  # Field renamed because it started with '_'.
    coefficient = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    summa = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    contract_locality = models.CharField(max_length=64, blank=True, null=True)
    field_student_type = models.ForeignKey('HStudentType', models.DO_NOTHING, db_column='_student_type', blank=True,
                                           null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_contract_price'
        db_table_comment = 'To`lov-shartnoma miqdorlari'


class EContractType(models.Model):
    field_contract_type = models.OneToOneField('HContractType', models.DO_NOTHING,
                                               db_column='_contract_type')  # Field renamed because it started with '_'.
    coef = models.DecimalField(max_digits=10, decimal_places=1)
    current_status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_contract_type'
        db_table_comment = 'Tolov-shartnoma turlari'


class ECounter(models.Model):
    identifier = models.CharField(unique=True, max_length=255, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_counter'


class ECriteriaTemplate(models.Model):
    field_publication_type_table = models.CharField(db_column='_publication_type_table',
                                                    max_length=64)  # Field renamed because it started with '_'.
    field_publication_methodical_type = models.ForeignKey('HMethodicalPublicationType', models.DO_NOTHING,
                                                          db_column='_publication_methodical_type', blank=True,
                                                          null=True)  # Field renamed because it started with '_'.
    field_publication_scientific_type = models.ForeignKey('HScientificPublicationType', models.DO_NOTHING,
                                                          db_column='_publication_scientific_type', blank=True,
                                                          null=True)  # Field renamed because it started with '_'.
    field_publication_property_type = models.ForeignKey('HPatientType', models.DO_NOTHING,
                                                        db_column='_publication_property_type', blank=True,
                                                        null=True)  # Field renamed because it started with '_'.
    field_in_publication_database = models.IntegerField(db_column='_in_publication_database', blank=True,
                                                        null=True)  # Field renamed because it started with '_'.
    exist_certificate = models.IntegerField(blank=True, null=True)
    mark_value = models.IntegerField()
    field_scientific_platform = models.ForeignKey('HScientificPlatform', models.DO_NOTHING,
                                                  db_column='_scientific_platform', blank=True,
                                                  null=True)  # Field renamed because it started with '_'.
    field_criteria_type = models.CharField(db_column='_criteria_type', max_length=64, blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    coefficient = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_criteria_template'
        db_table_comment = 'Kriteriylar shabloni'


class ECurriculum(models.Model):
    name = models.CharField(max_length=256)
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_marking_system = models.ForeignKey('HMarkingSystem', models.DO_NOTHING, db_column='_marking_system',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    semester_count = models.IntegerField()
    education_period = models.IntegerField()
    autumn_start_date = models.DateField()
    autumn_end_date = models.DateField()
    spring_start_date = models.DateField()
    spring_end_date = models.DateField()
    accepted = models.BooleanField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING, db_column='_specialty_id', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_qualification = models.ForeignKey('EQualification', models.DO_NOTHING, db_column='_qualification', blank=True,
                                            null=True)  # Field renamed because it started with '_'.

    def get_all_hsemestr(self):
        return self.hsemestr_set.filter(
            field_education_year='2023',
            code__regex='11|13|15|17|19',
            active=True
        )

    def get_all_groups(self):
        return self.egroup_set.all().filter(active=True)

    def get_all_cur_subjects(self):
        return self.ecurriculumsubject_set.filter(active=True,
                                                  field_semester__in=self.get_all_hsemestr().values('code'))

    class Meta:
        managed = False
        db_table = 'e_curriculum'
        db_table_comment = 'OTM o`quv rejalari'


class ECurriculumSubject(models.Model):
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_curriculum_subject_block = models.ForeignKey('HSubjectBlock', models.DO_NOTHING,
                                                       db_column='_curriculum_subject_block', blank=True,
                                                       null=True)  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject_type = models.ForeignKey('HSubjectType', models.DO_NOTHING, db_column='_subject_type', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_rating_grade = models.ForeignKey('HRatingGrade', models.DO_NOTHING, db_column='_rating_grade', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_exam_finish = models.ForeignKey('HExamFinish', models.DO_NOTHING, db_column='_exam_finish', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    total_acload = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    reorder = models.BooleanField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    at_semester = models.BooleanField(blank=True, null=True)
    in_group = models.CharField(max_length=64, blank=True, null=True)
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey('EEmployee', models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    resource_count = models.IntegerField(blank=True, null=True)
    field_employees = models.JSONField(db_column='_employees', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    accepted = models.BooleanField(blank=True, null=True)
    choice_accepted = models.BooleanField(blank=True, null=True)
    choice_start_date = models.DateTimeField(blank=True, null=True)
    choice_end_date = models.DateTimeField(blank=True, null=True)
    field_choice_created_by = models.ForeignKey('EEmployee', models.DO_NOTHING, db_column='_choice_created_by',
                                                related_name='ecurriculumsubject_field_choice_created_by_set',
                                                blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_curriculum_subject'
        unique_together = (('field_curriculum', 'field_subject', 'field_semester'),)
        db_table_comment = 'O`quv reja fanlari'


class ECurriculumSubjectBlock(models.Model):
    code = models.CharField(max_length=64)
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject_block = models.ForeignKey('HSubjectBlock', models.DO_NOTHING, db_column='_subject_block', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_curriculum_subject_block'
        db_table_comment = 'O`quv reja bloklari'


class ECurriculumSubjectDetail(models.Model):
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    academic_load = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_curriculum_subject_detail'
        unique_together = (('field_curriculum', 'field_subject', 'field_semester', 'field_training_type'),)
        db_table_comment = 'O`quv reja fanlari sillabuslari'


class ECurriculumSubjectExamType(models.Model):
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING, db_column='_exam_type', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    max_ball = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_curriculum_subject_exam_type'
        unique_together = (('field_curriculum', 'field_subject', 'field_semester', 'field_exam_type'),)
        db_table_comment = 'O`quv reja fanlarining nazorat turlari'


class ECurriculumSubjectResponsible(models.Model):
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING,
                                                 db_column='_curriculum_subject')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('EEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey('EEmployee', models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    students_count = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING, db_column='_training_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_curriculum_subject_detail = models.ForeignKey(ECurriculumSubjectDetail, models.DO_NOTHING,
                                                        db_column='_curriculum_subject_detail', blank=True,
                                                        null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_curriculum_subject_responsible'
        db_table_comment = 'O`quv reja fanlarining kafedra tomonidan belgilangan mas`ullari'


class ECurriculumSubjectTopic(models.Model):
    name = models.CharField(max_length=500)
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    topic_load = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_curriculum_subject_topic'
        db_table_comment = 'O`quv reja fanlari mavzulari'


class ECurriculumWeek(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING,
                                    db_column='_level')  # Field renamed because it started with '_'.
    field_education_week_type = models.ForeignKey('HEducationWeekType', models.DO_NOTHING,
                                                  db_column='_education_week_type')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_curriculum_week'
        db_table_comment = 'O`quv reja haftalari'


class EDecree(models.Model):
    field_department = models.ForeignKey('EDepartment', models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_decree_type = models.ForeignKey('HDecreeType', models.DO_NOTHING,
                                          db_column='_decree_type')  # Field renamed because it started with '_'.
    number = models.CharField(max_length=16)
    date = models.DateField()
    name = models.CharField(max_length=512)
    header = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    trailer = models.TextField(blank=True, null=True)
    file = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_decree'
        db_table_comment = 'Buyruqlar jadvali'


class EDecreeStudent(models.Model):
    field_decree = models.ForeignKey(EDecree, models.DO_NOTHING,
                                     db_column='_decree')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_admin = models.ForeignKey(EAdmin, models.DO_NOTHING,
                                    db_column='_admin')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING, db_column='_student_meta', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_decree_student'


class EDepartment(models.Model):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=256)
    field_university = models.ForeignKey('EUniversity', models.DO_NOTHING,
                                         db_column='_university')  # Field renamed because it started with '_'.
    field_structure_type = models.ForeignKey('HStructureType', models.DO_NOTHING,
                                             db_column='_structure_type')  # Field renamed because it started with '_'.
    parent = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_type = models.ForeignKey('HLocalityType', models.DO_NOTHING, db_column='_type', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_department'
        db_table_comment = 'OTM tuzilma nomlari'


class EDiplomaBlank(models.Model):
    type = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    number = models.CharField(max_length=64)
    reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    year = models.CharField(max_length=32, blank=True, null=True)
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_diploma_blank'
        db_table_comment = 'Diplom blanklari'


class EDissertationDefense(models.Model):
    field_doctorate_student = models.ForeignKey('EDoctorateStudent', models.DO_NOTHING,
                                                db_column='_doctorate_student')  # Field renamed because it started with '_'.
    field_science_branch = models.ForeignKey('HScienceBranch', models.DO_NOTHING, db_column='_science_branch_id',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty_id')  # Field renamed because it started with '_'.
    defense_date = models.DateField()
    defense_place = models.CharField(max_length=500)
    approved_date = models.DateField(blank=True, null=True)
    diploma_number = models.CharField(max_length=20)
    diploma_given_date = models.DateField(blank=True, null=True)
    diploma_given_by_whom = models.CharField(max_length=500)
    register_number = models.CharField(max_length=30)
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    scientific_council = models.CharField(max_length=1000, blank=True, null=True)
    field_second_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING, db_column='_second_specialty_id',
                                               related_name='edissertationdefense_field_second_specialty_set',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_dissertation_defense'
        db_table_comment = 'Dissertatsiya himoyalari to`g`risida ma`lumot'


class EDoctorateStudent(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    passport_number = models.CharField(max_length=14, blank=True, null=True)
    passport_pin = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField()
    dissertation_theme = models.CharField(max_length=500)
    home_address = models.CharField(max_length=255)
    accepted_date = models.DateField()
    student_id_number = models.CharField(max_length=14, blank=True, null=True)
    field_science_branch = models.ForeignKey('HScienceBranch', models.DO_NOTHING, db_column='_science_branch_id',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty_id')  # Field renamed because it started with '_'.
    field_payment_form = models.ForeignKey('HPaymentForm', models.DO_NOTHING,
                                           db_column='_payment_form')  # Field renamed because it started with '_'.
    field_citizenship = models.ForeignKey('HCitizenshipType', models.DO_NOTHING,
                                          db_column='_citizenship')  # Field renamed because it started with '_'.
    field_nationality = models.ForeignKey('HNationality', models.DO_NOTHING,
                                          db_column='_nationality')  # Field renamed because it started with '_'.
    field_gender = models.ForeignKey('HGender', models.DO_NOTHING,
                                     db_column='_gender')  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING, db_column='_country', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_province = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_province', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_district = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_district',
                                       related_name='edoctoratestudent_field_district_set', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_doctoral_student_type = models.ForeignKey('HDoctoralStudentType', models.DO_NOTHING,
                                                    db_column='_doctoral_student_type')  # Field renamed because it started with '_'.
    field_doctorate_student_status = models.ForeignKey('HDoctorateStudentStatus', models.DO_NOTHING,
                                                       db_column='_doctorate_student_status')  # Field renamed because it started with '_'.
    field_level = models.CharField(db_column='_level', max_length=64, blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    image = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_second_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING, db_column='_second_specialty_id',
                                               related_name='edoctoratestudent_field_second_specialty_set', blank=True,
                                               null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    passport_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_doctorate_student'
        db_table_comment = 'Muassasadagi doktorantlar to`g`risida ma`lumot'


class EEducationYear(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    current_status = models.IntegerField(blank=True, null=True)
    field_semestr_type = models.CharField(db_column='_semestr_type', max_length=64, blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_education_year'
        db_table_comment = 'Akademik o`quv yillari'


class EEmployee(models.Model):
    employee_id_number = models.CharField(max_length=14, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    field_gender = models.ForeignKey('HGender', models.DO_NOTHING, db_column='_gender', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    passport_number = models.CharField(unique=True, max_length=14, blank=True, null=True)
    passport_pin = models.CharField(unique=True, max_length=20, blank=True, null=True)
    field_academic_degree = models.ForeignKey('HAcademicDegree', models.DO_NOTHING, db_column='_academic_degree',
                                              blank=True, null=True)  # Field renamed because it started with '_'.
    field_academic_rank = models.ForeignKey('HAcademicRank', models.DO_NOTHING, db_column='_academic_rank', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    specialty = models.CharField(max_length=255, blank=True, null=True)
    image = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_admin = models.ForeignKey(EAdmin, models.DO_NOTHING, db_column='_admin', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    telephone = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    home_address = models.CharField(max_length=512, blank=True, null=True)
    field_citizenship = models.ForeignKey('HCitizenshipType', models.DO_NOTHING, db_column='_citizenship', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    year_of_enter = models.IntegerField(blank=True, null=True)
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    passport_date = models.DateField(blank=True, null=True)
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING, db_column='_country', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_province = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_province', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_district = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_district',
                                       related_name='eemployee_field_district_set', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_nationality = models.ForeignKey('HNationality', models.DO_NOTHING, db_column='_nationality', blank=True,
                                          null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_employee'


class EEmployeeAcademicDegree(models.Model):
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_academic_degree = models.ForeignKey('HAcademicDegree', models.DO_NOTHING, db_column='_academic_degree',
                                              blank=True, null=True)  # Field renamed because it started with '_'.
    field_academic_rank = models.ForeignKey('HAcademicRank', models.DO_NOTHING, db_column='_academic_rank', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    diploma_type = models.CharField(max_length=64)
    diploma_number = models.CharField(max_length=40, blank=True, null=True)
    diploma_date = models.DateField()
    specialty_code = models.CharField(max_length=20)
    specialty_name = models.CharField(max_length=512)
    council_date = models.DateField()
    council_number = models.CharField(max_length=40, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING, db_column='_country', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    university = models.CharField(max_length=512, blank=True, null=True)
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_employee_academic_degree'
        db_table_comment = "O'qituvchilar ilmiy darajalari jadvali"


class EEmployeeCompetition(models.Model):
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_employee_position = models.ForeignKey('HTeacherPositionType', models.DO_NOTHING,
                                                db_column='_employee_position')  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    election_date = models.DateField()
    document = models.CharField(max_length=1024, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_employee_competition'
        db_table_comment = "O'qituvchilarni tanlovdan o'tishi"


class EEmployeeForeign(models.Model):
    full_name = models.CharField(max_length=512)
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING,
                                      db_column='_country')  # Field renamed because it started with '_'.
    work_place = models.CharField(max_length=512)
    specialty_name = models.CharField(max_length=512)
    subject = models.CharField(max_length=512)
    contract_data = models.CharField(max_length=512)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_employee_foreign'
        db_table_comment = "Xorijiy o'qituvchilar haqida malumot"


class EEmployeeMeta(models.Model):
    employee_id_number = models.CharField(max_length=14, blank=True, null=True)
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_position = models.ForeignKey('HTeacherPositionType', models.DO_NOTHING,
                                       db_column='_position')  # Field renamed because it started with '_'.
    field_employment_form = models.ForeignKey('HEmploymentForm', models.DO_NOTHING,
                                              db_column='_employment_form')  # Field renamed because it started with '_'.
    field_employment_staff = models.ForeignKey('HEmploymentStaff', models.DO_NOTHING,
                                               db_column='_employment_staff')  # Field renamed because it started with '_'.
    field_employee_status = models.ForeignKey('HTeacherStatus', models.DO_NOTHING,
                                              db_column='_employee_status')  # Field renamed because it started with '_'.
    contract_number = models.CharField(max_length=64)
    contract_date = models.DateField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_old_uid = models.CharField(db_column='_old_uid', unique=True, max_length=255, blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_employee_type = models.ForeignKey('HEmployeeType', models.DO_NOTHING, db_column='_employee_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    decree_number = models.CharField(max_length=64, blank=True, null=True)
    decree_date = models.DateField(blank=True, null=True)
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_employee_meta'


class EEmployeeProfessionalDevelopment(models.Model):
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_employee_position = models.ForeignKey('HTeacherPositionType', models.DO_NOTHING,
                                                db_column='_employee_position')  # Field renamed because it started with '_'.
    training_title = models.CharField(max_length=1024, blank=True, null=True)
    training_year = models.IntegerField()
    field_training_place = models.ForeignKey('HQualification', models.DO_NOTHING,
                                             db_column='_training_place')  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    begin_date = models.DateField()
    end_date = models.DateField()
    document = models.CharField(max_length=1024, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_employee_professional_development'
        db_table_comment = "O'qituvchilarni malaka oshirish faoliyati"


class EEmployeeTraining(models.Model):
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING,
                                      db_column='_country')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    university = models.CharField(max_length=512)
    specialty_name = models.CharField(max_length=512)
    training_contract = models.CharField(max_length=512)
    training_date_start = models.DateField()
    training_date_end = models.DateField()
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_employee_training'
        db_table_comment = "O'qituvchilarning xorijning top 1000 oliygohlarida o'tkizgan o'quv mashg'ulotlari"


class EExam(models.Model):
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester', max_length=64, blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING, db_column='_curriculum', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_exam_schedule = models.ForeignKey('ESubjectExamSchedule', models.DO_NOTHING, db_column='_exam_schedule',
                                            blank=True, null=True)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING, db_column='_subject', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING,
                                        db_column='_exam_type')  # Field renamed because it started with '_'.
    name = models.CharField(max_length=512)
    comment = models.TextField(blank=True, null=True)
    start_at = models.DateTimeField()
    question_count = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    max_ball = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    random = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    finish_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_exam'
        db_table_comment = 'Talaba imtixonlari'


class EExamExclude(models.Model):
    field_exam = models.ForeignKey(EExam, models.DO_NOTHING, db_column='_exam', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING, db_column='_student', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    excluded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_exam_exclude'
        unique_together = (('field_exam', 'field_student'),)


class EExamGroup(models.Model):
    field_exam = models.ForeignKey(EExam, models.DO_NOTHING, db_column='_exam', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    start_at = models.DateTimeField(blank=True, null=True)
    finish_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_exam_group'


class EExamQuestion(models.Model):
    field_exam = models.ForeignKey(EExam, models.DO_NOTHING, db_column='_exam', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    name = models.TextField()
    content = models.TextField()
    content_r = models.TextField()
    answers = models.JSONField(blank=True, null=True)
    field_answer = models.JSONField(db_column='_answer', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_exam_question'


class EExamStudent(models.Model):
    field_exam = models.ForeignKey(EExam, models.DO_NOTHING, db_column='_exam', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING, db_column='_student', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    time = models.IntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    mark = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    correct = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    percent = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    ip = models.CharField(max_length=16, blank=True, null=True)
    session = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_exam_student'


class EGraduateQualifyingWork(models.Model):
    field_faculty = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                      db_column='_faculty')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    work_name = models.CharField(max_length=500)
    supervisor_name = models.CharField(max_length=255)
    supervisor_work = models.CharField(max_length=255, blank=True, null=True)
    advisor_name = models.CharField(max_length=255, blank=True, null=True)
    advisor_work = models.CharField(max_length=255, blank=True, null=True)
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_group = models.ForeignKey('EGroup', models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING, db_column='_department',
                                         related_name='egraduatequalifyingwork_field_department_set', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_decree = models.ForeignKey(EDecree, models.DO_NOTHING, db_column='_decree', blank=True,
                                     null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_graduate_qualifying_work'
        db_table_comment = 'Bitiruv malakaviy ishi'


class EGroup(models.Model):
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    name = models.CharField(max_length=256)
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_education_lang = models.ForeignKey('HLanguage', models.DO_NOTHING, db_column='_education_lang', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING, db_column='_specialty_id', blank=True,
                                        null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_group'
        db_table_comment = 'OTM guruhlari'


class EIncreasedContractCoefficient(models.Model):
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_contract_type = models.ForeignKey(EContractType, models.DO_NOTHING, db_column='_contract_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    coefficient = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_education_type = models.CharField(db_column='_education_type', max_length=64, blank=True,
                                            null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_increased_contract_coefficient'
        unique_together = (('field_department', 'field_specialty'),)
        db_table_comment = 'Oshirilgan shartnoma summalarini hisoblash koeffisientlari'


class EIndividualTrainingSubjectSchedule(models.Model):
    field_individual_training_subject_student = models.ForeignKey('EIndividualTrainingSubjectStudent',
                                                                  models.DO_NOTHING,
                                                                  db_column='_individual_training_subject_student')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_auditorium = models.ForeignKey(EAuditorium, models.DO_NOTHING,
                                         db_column='_auditorium')  # Field renamed because it started with '_'.
    field_subject_topic = models.IntegerField(db_column='_subject_topic', blank=True,
                                              null=True)  # Field renamed because it started with '_'.
    field_week = models.ForeignKey(ECurriculumWeek, models.DO_NOTHING,
                                   db_column='_week')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair', max_length=64, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    lesson_date = models.DateField()
    additional = models.CharField(max_length=512, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    start_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_individual_training_subject_schedule'
        db_table_comment = 'Yakka dars jadvali'


class EIndividualTrainingSubjectStudent(models.Model):
    field_individual_training_subject_teacher = models.ForeignKey('EIndividualTrainingSubjectTeacher',
                                                                  models.DO_NOTHING,
                                                                  db_column='_individual_training_subject_teacher')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING, db_column='_training_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_individual_training_subject_student'
        db_table_comment = 'Talabalarning individual mashg`ulotlarga ro`yxatga olish jadvali'


class EIndividualTrainingSubjectTeacher(models.Model):
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING,
                                                 db_column='_curriculum_subject')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_curriculum_subject_detail = models.ForeignKey(ECurriculumSubjectDetail, models.DO_NOTHING,
                                                        db_column='_curriculum_subject_detail')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_individual_training_subject_teacher'
        db_table_comment = 'O`quv reja fanlariga kafedra mudiri tomonidan belgilangan o`qituvchilari'


class EInventory(models.Model):
    number = models.CharField(unique=True, max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1200, blank=True, null=True)
    field_inventory_category = models.ForeignKey('EInventoryCategory', models.DO_NOTHING,
                                                 db_column='_inventory_category', blank=True,
                                                 null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_inventory'


class EInventoryCategory(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    description = models.CharField(max_length=1200, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_inventory_category'


class EMinimumWage(models.Model):
    name = models.DecimalField(max_digits=10, decimal_places=1)
    begin_date = models.DateField(blank=True, null=True)
    document = models.CharField(max_length=1024, blank=True, null=True)
    current_status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_minimum_wage'
        db_table_comment = 'Mehnatga haq to`lashning eng kam miqdori'


class EPaidContractFee(models.Model):
    field_student_contract = models.ForeignKey('EStudentContract', models.DO_NOTHING, db_column='_student_contract',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    payment_number = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.DateField()
    payment_type = models.DateField(blank=True, null=True)
    summa = models.DecimalField(max_digits=19, decimal_places=4)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    payment_comment = models.CharField(max_length=2000, blank=True, null=True)
    field_manual_type = models.CharField(db_column='_manual_type', max_length=64, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_paid_contract_fee'


class EPerformance(models.Model):
    field_exam_schedule = models.ForeignKey('ESubjectExamSchedule', models.DO_NOTHING,
                                            db_column='_exam_schedule')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING,
                                        db_column='_exam_type')  # Field renamed because it started with '_'.
    exam_name = models.CharField(max_length=64, blank=True, null=True)
    exam_date = models.DateField()
    grade = models.DecimalField(max_digits=10, decimal_places=1)
    regrade = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_final_exam_type = models.CharField(db_column='_final_exam_type', max_length=64, blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    send_record_status = models.IntegerField(blank=True, null=True)
    send_record_date = models.DateTimeField(blank=True, null=True)
    passed_status = models.IntegerField(blank=True, null=True)
    finish_credit_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_performance'
        unique_together = (('field_student', 'field_education_year', 'field_semester', 'field_subject',
                            'field_exam_type', 'field_final_exam_type'),)
        db_table_comment = 'Baholash jadvali'


class EPerformanceControl(models.Model):
    field_exam_schedule = models.ForeignKey('ESubjectExamSchedule', models.DO_NOTHING,
                                            db_column='_exam_schedule')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING,
                                        db_column='_exam_type')  # Field renamed because it started with '_'.
    exam_name = models.CharField(max_length=64)
    exam_date = models.DateField()
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_performance_control'
        unique_together = (('field_employee', 'field_group', 'field_education_year', 'field_semester', 'field_subject',
                            'field_exam_type', 'exam_name', 'field_lesson_pair', 'exam_date'),)
        db_table_comment = 'Davomat kiritilish holati'


class EProject(models.Model):
    name = models.CharField(max_length=255)
    project_number = models.CharField(max_length=255)
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_project_type = models.ForeignKey('HProjectType', models.DO_NOTHING,
                                           db_column='_project_type')  # Field renamed because it started with '_'.
    field_locality = models.ForeignKey('HLocality', models.DO_NOTHING,
                                       db_column='_locality')  # Field renamed because it started with '_'.
    field_project_currency = models.ForeignKey('HProjectCurrency', models.DO_NOTHING,
                                               db_column='_project_currency')  # Field renamed because it started with '_'.
    contract_number = models.CharField(max_length=255)
    contract_date = models.DateField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_project'
        db_table_comment = 'Muassasadagi loyihalar to`g`risida ma`lumot'


class EProjectExecutor(models.Model):
    field_project = models.ForeignKey(EProject, models.DO_NOTHING,
                                      db_column='_project')  # Field renamed because it started with '_'.
    field_project_executor_type = models.ForeignKey('HProjectExecutorType', models.DO_NOTHING,
                                                    db_column='_project_executor_type')  # Field renamed because it started with '_'.
    field_executor_type = models.IntegerField(db_column='_executor_type')  # Field renamed because it started with '_'.
    field_id_number = models.IntegerField(db_column='_id_number', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    outsider = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_project_executor'
        db_table_comment = 'Loyihalarning ijrochilari to`g`risidagi ma`lumot'


class EProjectMeta(models.Model):
    field_project = models.ForeignKey(EProject, models.DO_NOTHING,
                                      db_column='_project')  # Field renamed because it started with '_'.
    fiscal_year = models.IntegerField()
    budget = models.DecimalField(max_digits=19, decimal_places=4)
    quantity_members = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_project_meta'
        db_table_comment = 'Loyihalarning yillik moliyalashtirilishi to`g`risidagi ma`lumot'


class EPublicationAuthorMeta(models.Model):
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    is_main_author = models.IntegerField()
    field_publication_type_table = models.CharField(db_column='_publication_type_table',
                                                    max_length=64)  # Field renamed because it started with '_'.
    field_publication_methodical = models.ForeignKey('EPublicationMethodical', models.DO_NOTHING,
                                                     db_column='_publication_methodical', blank=True,
                                                     null=True)  # Field renamed because it started with '_'.
    field_publication_scientific = models.ForeignKey('EPublicationScientific', models.DO_NOTHING,
                                                     db_column='_publication_scientific', blank=True,
                                                     null=True)  # Field renamed because it started with '_'.
    field_publication_property = models.ForeignKey('EPublicationProperty', models.DO_NOTHING,
                                                   db_column='_publication_property', blank=True,
                                                   null=True)  # Field renamed because it started with '_'.
    is_checked_by_author = models.BooleanField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_publication_author_meta'
        unique_together = (('field_employee', 'field_publication_type_table', 'field_publication_methodical'),
                           ('field_employee', 'field_publication_type_table', 'field_publication_property'),
                           ('field_employee', 'field_publication_type_table', 'field_publication_scientific'),)
        db_table_comment = 'Ilmiy nashrlarning mualliflari to`g`risida ma`lumot'


class EPublicationCriteria(models.Model):
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_publication_type_table = models.CharField(db_column='_publication_type_table',
                                                    max_length=64)  # Field renamed because it started with '_'.
    field_publication_methodical_type = models.ForeignKey('HMethodicalPublicationType', models.DO_NOTHING,
                                                          db_column='_publication_methodical_type', blank=True,
                                                          null=True)  # Field renamed because it started with '_'.
    field_publication_scientific_type = models.ForeignKey('HScientificPublicationType', models.DO_NOTHING,
                                                          db_column='_publication_scientific_type', blank=True,
                                                          null=True)  # Field renamed because it started with '_'.
    field_publication_property_type = models.ForeignKey('HPatientType', models.DO_NOTHING,
                                                        db_column='_publication_property_type', blank=True,
                                                        null=True)  # Field renamed because it started with '_'.
    field_in_publication_database = models.IntegerField(db_column='_in_publication_database', blank=True,
                                                        null=True)  # Field renamed because it started with '_'.
    mark_value = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    exist_certificate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_publication_criteria'
        db_table_comment = 'Nashr ishlarini baholash mezonlari'


class EPublicationMethodical(models.Model):
    name = models.CharField(max_length=500)
    authors = models.CharField(max_length=255)
    author_counts = models.IntegerField()
    publisher = models.CharField(max_length=500)
    issue_year = models.IntegerField()
    source_name = models.CharField(max_length=500, blank=True, null=True)
    parameter = models.CharField(max_length=500)
    field_methodical_publication_type = models.ForeignKey('HMethodicalPublicationType', models.DO_NOTHING,
                                                          db_column='_methodical_publication_type')  # Field renamed because it started with '_'.
    field_publication_database = models.ForeignKey('HPublicationDatabase', models.DO_NOTHING,
                                                   db_column='_publication_database', blank=True,
                                                   null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_checked = models.BooleanField(blank=True, null=True)
    is_checked_date = models.DateTimeField(blank=True, null=True)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    certificate_number = models.CharField(max_length=64, blank=True, null=True)
    certificate_date = models.DateField(blank=True, null=True)
    field_language = models.ForeignKey('HLanguage', models.DO_NOTHING, db_column='_language', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_publication_methodical'
        db_table_comment = 'Uslubiy nashrlar to`g`risida ma`lumot'


class EPublicationProperty(models.Model):
    name = models.CharField(max_length=500)
    numbers = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    author_counts = models.IntegerField()
    parameter = models.CharField(max_length=500, blank=True, null=True)
    property_date = models.DateField()
    field_patient_type = models.ForeignKey('HPatientType', models.DO_NOTHING,
                                           db_column='_patient_type')  # Field renamed because it started with '_'.
    field_publication_database = models.ForeignKey('HPublicationDatabase', models.DO_NOTHING,
                                                   db_column='_publication_database', blank=True,
                                                   null=True)  # Field renamed because it started with '_'.
    field_locality = models.ForeignKey('HLocality', models.DO_NOTHING, db_column='_locality', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING, db_column='_country', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_checked = models.BooleanField(blank=True, null=True)
    is_checked_date = models.DateTimeField(blank=True, null=True)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_language = models.ForeignKey('HLanguage', models.DO_NOTHING, db_column='_language', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_publication_property'
        db_table_comment = 'Intellektual muhofaza hujjatlari to`g`risida ma`lumot'


class EPublicationScientific(models.Model):
    name = models.CharField(max_length=500)
    keywords = models.CharField(max_length=500)
    authors = models.CharField(max_length=255)
    author_counts = models.IntegerField()
    source_name = models.CharField(max_length=500)
    issue_year = models.IntegerField()
    parameter = models.CharField(max_length=500)
    doi = models.CharField(max_length=255, blank=True, null=True)
    field_scientific_publication_type = models.ForeignKey('HScientificPublicationType', models.DO_NOTHING,
                                                          db_column='_scientific_publication_type')  # Field renamed because it started with '_'.
    field_publication_database = models.ForeignKey('HPublicationDatabase', models.DO_NOTHING,
                                                   db_column='_publication_database', blank=True,
                                                   null=True)  # Field renamed because it started with '_'.
    field_locality = models.ForeignKey('HLocality', models.DO_NOTHING, db_column='_locality', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING, db_column='_country', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_checked = models.BooleanField(blank=True, null=True)
    is_checked_date = models.DateTimeField(blank=True, null=True)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_language = models.ForeignKey('HLanguage', models.DO_NOTHING, db_column='_language', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_publication_scientific'
        db_table_comment = 'Ilmiy nashrlar to`g`risida ma`lumot'


class EQualification(models.Model):
    field_specialty = models.ForeignKey('ESpecialty', models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1700)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_qualification'
        db_table_comment = 'Kvalifikatsiyalar'


class ERetraining(models.Model):
    name = models.CharField(max_length=256)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    application_count = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    accepted = models.BooleanField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_retraining'
        db_table_comment = 'Qayta o`qish davrini registratsiya qilish'


class ERetrainingExamSchedule(models.Model):
    field_retraining = models.ForeignKey(ERetraining, models.DO_NOTHING,
                                         db_column='_retraining')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_retraining_subject_group = models.ForeignKey('ERetrainingSubjectGroup', models.DO_NOTHING,
                                                       db_column='_retraining_subject_group', blank=True,
                                                       null=True)  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING,
                                        db_column='_exam_type')  # Field renamed because it started with '_'.
    field_auditorium = models.ForeignKey(EAuditorium, models.DO_NOTHING,
                                         db_column='_auditorium')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    exam_date = models.DateField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING, db_column='_curriculum_subject',
                                                 blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_retraining_exam_schedule'
        unique_together = (('field_retraining', 'field_subject', 'field_education_year',
                            'field_retraining_subject_group', 'field_exam_type'),)
        db_table_comment = 'Qayta topshirish uchun nazorat jadvali'


class ERetrainingPerformance(models.Model):
    field_retraining_exam_schedule = models.ForeignKey(ERetrainingExamSchedule, models.DO_NOTHING,
                                                       db_column='_retraining_exam_schedule')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING,
                                        db_column='_exam_type')  # Field renamed because it started with '_'.
    exam_name = models.CharField(max_length=64, blank=True, null=True)
    exam_date = models.DateField()
    grade = models.DecimalField(max_digits=10, decimal_places=1)
    regrade = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    send_record_status = models.IntegerField(blank=True, null=True)
    send_record_date = models.DateTimeField(blank=True, null=True)
    passed_status = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_retraining_performance'
        unique_together = (
            ('field_student', 'field_education_year', 'field_semester', 'field_subject', 'field_exam_type'),)
        db_table_comment = 'Qayta o`qish baholash jadvali'


class ERetrainingPerformanceControl(models.Model):
    field_retraining_exam_schedule = models.ForeignKey(ERetrainingExamSchedule, models.DO_NOTHING,
                                                       db_column='_retraining_exam_schedule')  # Field renamed because it started with '_'.
    field_retraining_subject_group = models.ForeignKey('ERetrainingSubjectGroup', models.DO_NOTHING,
                                                       db_column='_retraining_subject_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester', max_length=64, blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING,
                                        db_column='_exam_type')  # Field renamed because it started with '_'.
    exam_name = models.CharField(max_length=64)
    exam_date = models.DateField()
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_retraining_performance_control'
        unique_together = (
            ('field_retraining_exam_schedule', 'field_employee', 'field_retraining_subject_group', 'field_exam_type'),)
        db_table_comment = 'Qayta o`qish bahosini kiritilish holati'


class ERetrainingStudent(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    field_retraining = models.ForeignKey(ERetraining, models.DO_NOTHING,
                                         db_column='_retraining')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_education_lang = models.ForeignKey('HLanguage', models.DO_NOTHING,
                                             db_column='_education_lang')  # Field renamed because it started with '_'.
    subjects_count = models.IntegerField(blank=True, null=True)
    credit_count = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_retraining_student'
        db_table_comment = 'Talabaning qayta o`qish uchun arizalari'


class ERetrainingSubject(models.Model):
    field_retraining_student = models.ForeignKey(ERetrainingStudent, models.DO_NOTHING,
                                                 db_column='_retraining_student')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING,
                                                 db_column='_curriculum_subject')  # Field renamed because it started with '_'.
    total_acload = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_retraining = models.ForeignKey(ERetraining, models.DO_NOTHING, db_column='_retraining', blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_retraining_subject'
        db_table_comment = 'Talabaning qayta o`qish uchun fanlari'


class ERetrainingSubjectGroup(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    field_retraining = models.ForeignKey(ERetraining, models.DO_NOTHING,
                                         db_column='_retraining')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_education_lang = models.ForeignKey('HLanguage', models.DO_NOTHING,
                                             db_column='_education_lang')  # Field renamed because it started with '_'.
    field_retraining_subject = models.ForeignKey(ERetrainingSubject, models.DO_NOTHING,
                                                 db_column='_retraining_subject')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_retraining_subject_group'
        db_table_comment = 'Talabani qayta o`qish uchun fan guruhlariga biriktirish'


class ERetrainingSubjectGroupStudent(models.Model):
    field_retraining = models.ForeignKey(ERetraining, models.DO_NOTHING,
                                         db_column='_retraining')  # Field renamed because it started with '_'.
    field_retraining_student = models.ForeignKey(ERetrainingStudent, models.DO_NOTHING,
                                                 db_column='_retraining_student')  # Field renamed because it started with '_'.
    field_retraining_subject_group = models.ForeignKey(ERetrainingSubjectGroup, models.DO_NOTHING,
                                                       db_column='_retraining_subject_group')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey('EStudent', models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING, db_column='_subject', blank=True,
                                      null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_retraining_subject_group_student'
        unique_together = (('field_retraining', 'field_student', 'field_retraining_subject_group'),
                           ('field_retraining', 'field_student', 'field_subject'),)


class ERetrainingSubjectSchedule(models.Model):
    field_retraining = models.ForeignKey(ERetraining, models.DO_NOTHING,
                                         db_column='_retraining')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING, db_column='_curriculum_subject',
                                                 blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_retraining_subject_group = models.ForeignKey(ERetrainingSubjectGroup, models.DO_NOTHING,
                                                       db_column='_retraining_subject_group', blank=True,
                                                       null=True)  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_auditorium = models.ForeignKey(EAuditorium, models.DO_NOTHING,
                                         db_column='_auditorium')  # Field renamed because it started with '_'.
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING, db_column='_subject_topic',
                                            blank=True, null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    lesson_date = models.DateField()
    additional = models.CharField(max_length=512, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_retraining_subject_schedule'
        db_table_comment = 'Qayta o`qish uchun dars jadvali'


class EScientificPlatformCriteria(models.Model):
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_publication_type_table = models.CharField(db_column='_publication_type_table',
                                                    max_length=64)  # Field renamed because it started with '_'.
    field_scientific_platform = models.ForeignKey('HScientificPlatform', models.DO_NOTHING,
                                                  db_column='_scientific_platform')  # Field renamed because it started with '_'.
    field_criteria_type = models.CharField(db_column='_criteria_type',
                                           max_length=64)  # Field renamed because it started with '_'.
    mark_value = models.IntegerField()
    coefficient = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_scientific_platform_criteria'
        unique_together = (('field_education_year', 'field_scientific_platform', 'field_criteria_type'),)
        db_table_comment = 'Xalqaro platformalardagi faolligini baholash mezonlari'


class EScientificPlatformProfile(models.Model):
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_scientific_platform = models.ForeignKey('HScientificPlatform', models.DO_NOTHING,
                                                  db_column='_scientific_platform')  # Field renamed because it started with '_'.
    profile_link = models.CharField(max_length=512)
    h_index = models.IntegerField(blank=True, null=True)
    publication_work_count = models.IntegerField(blank=True, null=True)
    citation_count = models.IntegerField(blank=True, null=True)
    is_checked = models.BooleanField(blank=True, null=True)
    is_checked_date = models.DateTimeField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_scientific_platform_profile'
        unique_together = (('field_employee', 'field_scientific_platform', 'field_education_year'),)
        db_table_comment = 'Xodimlarning xalqaro platformalardagi profillari to`g`risida ma`lumot'


class ESmsLog(models.Model):
    ip = models.CharField(max_length=64, blank=True, null=True)
    number = models.CharField(max_length=12)
    type = models.CharField(max_length=16)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_sms_log'


class ESpecialty(models.Model):
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    parent_code = models.CharField(max_length=64, blank=True, null=True)
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_knowledge_type = models.CharField(db_column='_knowledge_type', max_length=64, blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_type = models.ForeignKey('HLocalityType', models.DO_NOTHING, db_column='_type', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_bachelor_specialty = models.ForeignKey('HBachelorSpeciality', models.DO_NOTHING,
                                                 db_column='_bachelor_specialty', blank=True,
                                                 null=True)  # Field renamed because it started with '_'.
    field_master_specialty = models.ForeignKey('HMasterSpeciality', models.DO_NOTHING, db_column='_master_specialty',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_doctorate_specialty = models.ForeignKey('HScienceBranch', models.DO_NOTHING, db_column='_doctorate_specialty',
                                                  blank=True, null=True)  # Field renamed because it started with '_'.
    field_ordinature_specialty = models.ForeignKey('HSpecialityOrdinatura', models.DO_NOTHING,
                                                   db_column='_ordinature_specialty', blank=True,
                                                   null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_specialty'
        db_table_comment = 'OTMdagi ta`lim yo`nalishlari va ixtisosliklari'


class EStipendValue(models.Model):
    field_stipend_rate = models.ForeignKey('HStipendRate', models.DO_NOTHING,
                                           db_column='_stipend_rate')  # Field renamed because it started with '_'.
    stipend_value = models.DecimalField(max_digits=10, decimal_places=1)
    begin_date = models.DateField(blank=True, null=True)
    document = models.CharField(max_length=1024, blank=True, null=True)
    current_status = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_stipend_value'
        db_table_comment = 'Stipendiya miqdorlari'


class EStudent(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    student_id_number = models.CharField(max_length=14, blank=True, null=True)
    passport_number = models.CharField(max_length=14, blank=True, null=True)
    passport_pin = models.CharField(max_length=20, blank=True, null=True)
    field_gender = models.ForeignKey('HGender', models.DO_NOTHING,
                                     db_column='_gender')  # Field renamed because it started with '_'.
    field_nationality = models.ForeignKey('HNationality', models.DO_NOTHING,
                                          db_column='_nationality')  # Field renamed because it started with '_'.
    field_citizenship = models.ForeignKey('HCitizenshipType', models.DO_NOTHING, db_column='_citizenship', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING, db_column='_country', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_province = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_province', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_district = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_district',
                                       related_name='estudent_field_district_set', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_accommodation = models.ForeignKey('HAccommodation', models.DO_NOTHING, db_column='_accommodation', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_social_category = models.ForeignKey('HSocialCategory', models.DO_NOTHING, db_column='_social_category',
                                              blank=True, null=True)  # Field renamed because it started with '_'.
    home_address = models.CharField(max_length=255)
    current_address = models.CharField(max_length=255)
    year_of_enter = models.IntegerField()
    other = models.CharField(max_length=1024, blank=True, null=True)
    image = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    password = models.CharField(max_length=256, blank=True, null=True)
    auth_key = models.CharField(max_length=32, blank=True, null=True)
    access_token = models.CharField(max_length=32, blank=True, null=True)
    password_reset_token = models.CharField(max_length=32, blank=True, null=True)
    password_reset_date = models.DateTimeField(blank=True, null=True)
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    pin_verified = models.IntegerField(blank=True, null=True)
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_decree_enroll = models.ForeignKey(EDecree, models.DO_NOTHING, db_column='_decree_enroll', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    uzasbo_id_number = models.CharField(unique=True, max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    field_current_province = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_current_province',
                                               related_name='estudent_field_current_province_set', blank=True,
                                               null=True)  # Field renamed because it started with '_'.
    field_current_district = models.ForeignKey('HSoato', models.DO_NOTHING, db_column='_current_district',
                                               related_name='estudent_field_current_district_set', blank=True,
                                               null=True)  # Field renamed because it started with '_'.
    password_valid = models.BooleanField(blank=True, null=True)
    password_date = models.DateTimeField(blank=True, null=True)
    field_student_type = models.ForeignKey('HStudentType', models.DO_NOTHING, db_column='_student_type', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    person_phone = models.CharField(max_length=20, blank=True, null=True)
    parent_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    geo_location = models.CharField(max_length=2000, blank=True, null=True)
    roommate_count = models.IntegerField(blank=True, null=True)
    field_student_living_status = models.ForeignKey('HStudentLivingStatus', models.DO_NOTHING,
                                                    db_column='_student_living_status', blank=True,
                                                    null=True)  # Field renamed because it started with '_'.
    field_student_roommate_type = models.ForeignKey('HStudentRoommateType', models.DO_NOTHING,
                                                    db_column='_student_roommate_type', blank=True,
                                                    null=True)  # Field renamed because it started with '_'.
    total_acload = models.IntegerField(blank=True, null=True)
    total_credit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    avg_grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    passport_date = models.DateField(blank=True, null=True)
    avg_gpa = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    user_uuid = models.UUIDField(unique=True, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    account_active = models.BooleanField(blank=True, null=True)
    is_graduate = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student'
        unique_together = (('passport_number', 'year_of_enter'), ('passport_pin', 'year_of_enter'),)
        db_table_comment = 'Xodim shaxsiy ma`lumotlari'


class EStudentApiToken(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    token = models.CharField(unique=True, max_length=12000, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    user_agent = models.CharField(max_length=1024, blank=True, null=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_api_token'


class EStudentAward(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_student_level = models.ForeignKey('HCourse', models.DO_NOTHING,
                                            db_column='_student_level')  # Field renamed because it started with '_'.
    field_student_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                            db_column='_student_group')  # Field renamed because it started with '_'.
    field_award_group = models.ForeignKey('HStudentSuccess', models.DO_NOTHING,
                                          db_column='_award_group')  # Field renamed because it started with '_'.
    field_award_category = models.ForeignKey('HStudentSuccess', models.DO_NOTHING, db_column='_award_category',
                                             related_name='estudentaward_field_award_category_set')  # Field renamed because it started with '_'.
    award_document = models.CharField(max_length=1024)
    award_year = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    active = models.BooleanField(blank=True, null=True)
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING, db_column='_education_type',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING, db_column='_education_form',
                                             blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_award'
        db_table_comment = 'Student yutuqlari'


class EStudentContract(models.Model):
    number = models.CharField(max_length=64, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    summa = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    field_student_contract_type = models.ForeignKey('EStudentContractType', models.DO_NOTHING,
                                                    db_column='_student_contract_type', blank=True,
                                                    null=True)  # Field renamed because it started with '_'.
    field_contract_summa_type = models.ForeignKey('HContractSummaType', models.DO_NOTHING,
                                                  db_column='_contract_summa_type', blank=True,
                                                  null=True)  # Field renamed because it started with '_'.
    contract_form_type = models.CharField(max_length=64, blank=True, null=True)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    university_code = models.CharField(max_length=10, blank=True, null=True)
    rector = models.CharField(max_length=255, blank=True, null=True)
    mailing_address = models.TextField(blank=True, null=True)
    bank_details = models.TextField(blank=True, null=True)
    contract_status = models.CharField(max_length=64, blank=True, null=True)
    customer = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_department = models.IntegerField(db_column='_department', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_curriculum = models.IntegerField(db_column='_curriculum', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_group = models.IntegerField(db_column='_group', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    field_contract_type = models.CharField(db_column='_contract_type', max_length=64, blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    filename = models.JSONField(blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    month_count = models.IntegerField(blank=True, null=True)
    different = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    different_status = models.CharField(max_length=64, blank=True, null=True)
    accepted = models.BooleanField(blank=True, null=True)
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING, db_column='_level', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_manual_type = models.CharField(db_column='_manual_type', max_length=64, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_graduate_type = models.CharField(db_column='_graduate_type', max_length=64, blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)
    education_period = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    field_contract_class = models.ForeignKey('HContractClass', models.DO_NOTHING, db_column='_contract_class',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    credit_amount = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    field_created_self = models.BooleanField(db_column='_created_self', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    real_summa = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student_contract'
        db_table_comment = 'Talabalarning shartnoma to`lovlari'


class EStudentContractInvoice(models.Model):
    field_student_contract = models.ForeignKey(EStudentContract, models.DO_NOTHING, db_column='_student_contract',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING,
                                    db_column='_level')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    invoice_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    invoice_date = models.DateField()
    invoice_summa = models.DecimalField(max_digits=19, decimal_places=4)
    invoice_status = models.CharField(max_length=64, blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student_contract_invoice'
        db_table_comment = 'Talabalarning shartnomalari uchun hisob fakturalar'


class EStudentContractTemplate(models.Model):
    contract_type = models.CharField(max_length=64, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_contract_template'
        db_table_comment = 'Shartnomalar shabloni'


class EStudentContractType(models.Model):
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_contract_summa_type = models.ForeignKey('HContractSummaType', models.DO_NOTHING,
                                                  db_column='_contract_summa_type', blank=True,
                                                  null=True)  # Field renamed because it started with '_'.
    contract_form_type = models.CharField(max_length=64, blank=True, null=True)
    field_created_self = models.BooleanField(db_column='_created_self', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    contract_status = models.CharField(max_length=64, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_department = models.IntegerField(db_column='_department', blank=True,
                                           null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_contract_type'
        unique_together = (('field_specialty', 'field_student', 'field_education_year', 'field_education_form'),)
        db_table_comment = 'Talabalarning shartnoma summasi turi bo`yicha tanlovlari'


class EStudentData(models.Model):
    type = models.CharField(max_length=32)
    key = models.CharField(max_length=32)
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_data = models.JSONField(db_column='_data', blank=True,
                                  null=True)  # Field renamed because it started with '_'.
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student_data'
        unique_together = (('type', 'key'),)


class EStudentDiploma(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    specialty_name = models.CharField(max_length=256)
    student_name = models.CharField(max_length=256)
    student_id_number = models.CharField(max_length=20, blank=True, null=True)
    diploma_number = models.CharField(unique=True, max_length=20)
    register_number = models.CharField(max_length=30)
    register_date = models.DateField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    department_name = models.CharField(max_length=256)
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING, db_column='_specialty_id', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_university = models.ForeignKey('EUniversity', models.DO_NOTHING, db_column='_university', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    university_name = models.CharField(max_length=256, blank=True, null=True)
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING, db_column='_education_type',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    education_type_name = models.CharField(max_length=256, blank=True, null=True)
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING, db_column='_education_form',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    education_form_name = models.CharField(max_length=256, blank=True, null=True)
    specialty_code = models.CharField(max_length=64, blank=True, null=True)
    field_qualification = models.ForeignKey(EQualification, models.DO_NOTHING, db_column='_qualification', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    qualification_name = models.CharField(max_length=256, blank=True, null=True)
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    group_name = models.CharField(max_length=256, blank=True, null=True)
    student_birthday = models.DateField(blank=True, null=True)
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING, db_column='_education_year',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    education_year_name = models.CharField(max_length=256, blank=True, null=True)
    diploma_category = models.CharField(max_length=64, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    rector_fullname = models.CharField(max_length=256, blank=True, null=True)
    given_city = models.CharField(max_length=256, blank=True, null=True)
    post_address = models.CharField(max_length=256, blank=True, null=True)
    education_language = models.CharField(max_length=64, blank=True, null=True)
    education_period = models.CharField(max_length=30, blank=True, null=True)
    last_education = models.CharField(max_length=255, blank=True, null=True)
    marking_system = models.TextField(blank=True, null=True)
    university_accreditation = models.CharField(max_length=255, blank=True, null=True)
    diploma_link = models.CharField(max_length=256, blank=True, null=True)
    suplement_link = models.CharField(max_length=256, blank=True, null=True)
    diploma_status = models.CharField(max_length=20, blank=True, null=True)
    admission_information = models.CharField(max_length=1000, blank=True, null=True)
    qualification_data = models.CharField(max_length=1700, blank=True, null=True)
    next_edu_information = models.CharField(max_length=1000, blank=True, null=True)
    given_hei_information = models.CharField(max_length=1000, blank=True, null=True)
    professional_activity = models.CharField(max_length=1000, blank=True, null=True)
    graduate_qualifying_work = models.CharField(max_length=500, blank=True, null=True)
    moved_hei = models.CharField(max_length=1000, blank=True, null=True)
    accepted = models.BooleanField(blank=True, null=True)
    published = models.BooleanField(blank=True, null=True)
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)
    additional_info = models.CharField(max_length=1000, blank=True, null=True)
    total_acload = models.IntegerField(blank=True, null=True)
    total_credit = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    avg_grade = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    version = models.CharField(max_length=16, blank=True, null=True)
    diploma_type = models.CharField(max_length=32, blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_diploma'
        db_table_comment = 'Bitiruvchi talabalarning diplomlari'


class EStudentEmployment(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    student = models.CharField(max_length=256)
    student_id_number = models.CharField(max_length=20, blank=True, null=True)
    employment_doc_number = models.CharField(max_length=20, blank=True, null=True)
    employment_doc_date = models.DateField(blank=True, null=True)
    company_name = models.CharField(max_length=256, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    position_name = models.CharField(max_length=256, blank=True, null=True)
    field_employment_status = models.CharField(db_column='_employment_status', max_length=64, blank=True,
                                               null=True)  # Field renamed because it started with '_'.
    field_graduate_fields_type = models.ForeignKey('HGraduateFieldsType', models.DO_NOTHING,
                                                   db_column='_graduate_fields_type', blank=True,
                                                   null=True)  # Field renamed because it started with '_'.
    workplace_compatibility = models.CharField(max_length=64, blank=True, null=True)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING, db_column='_education_type',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING, db_column='_education_form',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_gender = models.ForeignKey('HGender', models.DO_NOTHING, db_column='_gender', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING, db_column='_specialty', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING, db_column='_level', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_graduate_inactive = models.CharField(db_column='_graduate_inactive', max_length=64, blank=True,
                                               null=True)  # Field renamed because it started with '_'.
    field_payment_form = models.ForeignKey('HPaymentForm', models.DO_NOTHING, db_column='_payment_form', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_employment'


class EStudentExchange(models.Model):
    full_name = models.CharField(max_length=512)
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING,
                                      db_column='_country')  # Field renamed because it started with '_'.
    university = models.CharField(max_length=512)
    specialty_name = models.CharField(max_length=512)
    exchange_document = models.CharField(max_length=512)
    exchange_type = models.CharField(max_length=64)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_exchange'
        db_table_comment = 'Talabalarning xorijiy almashinuv dasturlari'


class EStudentGpa(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_student_meta = models.ForeignKey('EStudentMeta', models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING,
                                    db_column='_level')  # Field renamed because it started with '_'.
    data = models.JSONField(blank=True, null=True)
    subjects = models.IntegerField(blank=True, null=True)
    credit_sum = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    gpa = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    debt_subjects = models.IntegerField(blank=True, null=True)
    can_transfer = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student_gpa'
        unique_together = (('field_student', 'field_education_year'),)
        db_table_comment = 'Talabalarning GPA ballari'


class EStudentGrade(models.Model):
    field_subject_schedule = models.ForeignKey('ESubjectSchedule', models.DO_NOTHING,
                                               db_column='_subject_schedule')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    lesson_date = models.DateField()
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    grade = models.IntegerField()
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING, db_column='_subject_topic',
                                            blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_grade'
        unique_together = (('field_student', 'field_employee', 'field_subject_schedule', 'field_subject_topic'),)
        db_table_comment = 'Baholar jadvali'


class EStudentMeta(models.Model):
    student_id_number = models.CharField(max_length=14, blank=True, null=True)
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING, db_column='_department', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING, db_column='_education_form',
                                             blank=True, null=True)  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING, db_column='_curriculum', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_semestr = models.CharField(db_column='_semestr', max_length=64, blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING, db_column='_level', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_subgroup = models.IntegerField(db_column='_subgroup', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_payment_form = models.ForeignKey('HPaymentForm', models.DO_NOTHING,
                                           db_column='_payment_form')  # Field renamed because it started with '_'.
    field_student_status = models.ForeignKey('HStudentStatus', models.DO_NOTHING,
                                             db_column='_student_status')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    diploma_registration = models.IntegerField(blank=True, null=True)
    employment_registration = models.IntegerField(blank=True, null=True)
    order_number = models.CharField(max_length=32, blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)
    field_status_change_reason = models.CharField(db_column='_status_change_reason', max_length=64, blank=True,
                                                  null=True)  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING, db_column='_specialty_id', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    accreditation_accepted = models.BooleanField(blank=True, null=True)
    field_decree = models.ForeignKey(EDecree, models.DO_NOTHING, db_column='_decree', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_restore_meta = models.ForeignKey('self', models.DO_NOTHING, db_column='_restore_meta_id', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    subjects_map = models.CharField(max_length=4095, blank=True, null=True)
    field_academic_mobile = models.ForeignKey('HAcademicMobileType', models.DO_NOTHING, db_column='_academic_mobile',
                                              blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_meta'
        unique_together = (('field_curriculum', 'field_student', 'field_education_type', 'field_education_year',
                            'field_semestr', 'field_student_status'),)
        db_table_comment = 'Talaba akademik ma`lumotlari'


class EStudentOlympiad(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_country = models.ForeignKey('HCountry', models.DO_NOTHING,
                                      db_column='_country')  # Field renamed because it started with '_'.
    olympiad_type = models.CharField(max_length=64)
    olympiad_place = models.CharField(max_length=512)
    olympiad_name = models.CharField(max_length=512)
    olympiad_section_name = models.CharField(max_length=512, blank=True, null=True)
    olympiad_date = models.DateField()
    student_place = models.IntegerField(blank=True, null=True)
    diploma_serial = models.CharField(max_length=32, blank=True, null=True)
    diploma_number = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_olympiad'
        db_table_comment = 'Talabalar qatnashgan musobaqalar'


class EStudentPtt(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.ForeignKey('HSemestr', models.DO_NOTHING,
                                       db_column='_semester')  # Field renamed because it started with '_'.
    field_decree = models.ForeignKey(EDecree, models.DO_NOTHING,
                                     db_column='_decree')  # Field renamed because it started with '_'.
    subjects_count = models.IntegerField(blank=True, null=True)
    graded_count = models.IntegerField(blank=True, null=True)
    number = models.CharField(unique=True, max_length=64)
    date = models.DateTimeField()
    data = models.JSONField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_ptt'
        unique_together = (('field_student', 'field_semester'),)
        db_table_comment = 'Talabalarning shaxsiy jadvali'


class EStudentPttSubject(models.Model):
    field_student_ptt = models.ForeignKey(EStudentPtt, models.DO_NOTHING,
                                          db_column='_student_ptt')  # Field renamed because it started with '_'.
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING,
                                                 db_column='_curriculum_subject')  # Field renamed because it started with '_'.
    total_acload = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_point = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_ptt_subject'
        unique_together = (('field_student_ptt', 'field_curriculum_subject'),)


class EStudentReference(models.Model):
    field_student_meta = models.ForeignKey(EStudentMeta, models.DO_NOTHING,
                                           db_column='_student_meta')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING, db_column='_curriculum', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_level = models.ForeignKey('HCourse', models.DO_NOTHING,
                                    db_column='_level')  # Field renamed because it started with '_'.
    university_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    second_name = models.CharField(max_length=100, blank=True, null=True)
    third_name = models.CharField(max_length=100, blank=True, null=True)
    passport_pin = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    year_of_enter = models.IntegerField()
    field_citizenship = models.ForeignKey('HCitizenshipType', models.DO_NOTHING,
                                          db_column='_citizenship')  # Field renamed because it started with '_'.
    field_payment_form = models.ForeignKey('HPaymentForm', models.DO_NOTHING,
                                           db_column='_payment_form')  # Field renamed because it started with '_'.
    reference_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reference_date = models.DateField()
    hash = models.CharField(unique=True, max_length=36, blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    department_name = models.CharField(max_length=255, blank=True, null=True)
    specialty_name = models.CharField(max_length=255, blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    education_type_name = models.CharField(max_length=255, blank=True, null=True)
    education_form_name = models.CharField(max_length=255, blank=True, null=True)
    education_year_name = models.CharField(max_length=255, blank=True, null=True)
    curriculum_name = models.CharField(max_length=255, blank=True, null=True)
    semester_name = models.CharField(max_length=255, blank=True, null=True)
    level_name = models.CharField(max_length=255, blank=True, null=True)
    citizenship_name = models.CharField(max_length=255, blank=True, null=True)
    payment_form_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student_reference'
        unique_together = (
            ('field_student', 'field_specialty', 'field_education_year', 'field_semester', 'field_education_form'),)
        db_table_comment = 'Talabalarning o`qish joyidan ma`lumotnomalari'


class EStudentRefreshToken(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    token = models.CharField(unique=True, max_length=200, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    user_agent = models.CharField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_refresh_token'


class EStudentScholarship(models.Model):
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_specialty = models.ForeignKey(ESpecialty, models.DO_NOTHING,
                                        db_column='_specialty')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey('HEducationForm', models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_payment_form = models.ForeignKey('HPaymentForm', models.DO_NOTHING,
                                           db_column='_payment_form')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_stipend_rate = models.ForeignKey('HStipendRate', models.DO_NOTHING,
                                           db_column='_stipend_rate')  # Field renamed because it started with '_'.
    field_decree = models.ForeignKey(EDecree, models.DO_NOTHING, db_column='_decree', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    summa = models.DecimalField(max_digits=19, decimal_places=4)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_scholarship'
        unique_together = (('field_student', 'field_semester', 'field_education_year'),)
        db_table_comment = 'Talabalarning stipendiya miqdorlari'


class EStudentScholarshipMonth(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_student_scholarship = models.ForeignKey(EStudentScholarship, models.DO_NOTHING,
                                                  db_column='_student_scholarship')  # Field renamed because it started with '_'.
    field_stipend_rate = models.ForeignKey('HStipendRate', models.DO_NOTHING,
                                           db_column='_stipend_rate')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING, db_column='_education_year', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    month_name = models.DateField()
    summa = models.DecimalField(max_digits=19, decimal_places=4)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_scholarship_month'
        unique_together = (('field_student', 'field_semester', 'field_education_year', 'month_name'),)
        db_table_comment = 'Talabalarning stipendiya miqdorlarining oylar bo`yicha taqsimoti'


class EStudentSport(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey('HEducationYear', models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_sport_type = models.ForeignKey('HSportType', models.DO_NOTHING,
                                         db_column='_sport_type')  # Field renamed because it started with '_'.
    record_type = models.CharField(max_length=64, blank=True, null=True)
    sport_date = models.DateField(blank=True, null=True)
    sport_rank = models.CharField(max_length=32, blank=True, null=True)
    sport_rank_document = models.CharField(max_length=32, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_sport'
        db_table_comment = 'Talabalarning sport seksiyalari va razryadlari'


class EStudentSubject(models.Model):
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    created_self = models.BooleanField(blank=True, null=True)
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    absents_count = models.IntegerField(blank=True, null=True)
    absent_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_student_subject'
        unique_together = (
            ('field_curriculum', 'field_student', 'field_education_year', 'field_semester', 'field_subject'),)
        db_table_comment = 'Talabalarning semestrda o`qiydigan fanlari'


class EStudentSubjectChoice(models.Model):
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING,
                                                 db_column='_curriculum_subject')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING, db_column='_training_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING, db_column='_group', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_created_self = models.BooleanField(db_column='_created_self', blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_student_subject_choice'
        unique_together = (('field_curriculum_subject', 'field_student'),)
        db_table_comment = 'Talabalarning fan tanlovi jadvali'


class EStudentTaskActivity(models.Model):
    field_subject_task_student = models.ForeignKey('ESubjectTaskStudent', models.DO_NOTHING,
                                                   db_column='_subject_task_student')  # Field renamed because it started with '_'.
    field_subject_task = models.ForeignKey('ESubjectTask', models.DO_NOTHING,
                                           db_column='_subject_task')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey('ESubject', models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    send_date = models.DateTimeField(blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    attempt_count = models.IntegerField()
    mark = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    marked_date = models.DateTimeField(blank=True, null=True)
    marked_comment = models.TextField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_task_type = models.CharField(db_column='_task_type', max_length=64, blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING, db_column='_subject_topic',
                                            blank=True, null=True)  # Field renamed because it started with '_'.
    data = models.JSONField(blank=True, null=True)
    percent_b = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    percent_c = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    correct = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    status = models.CharField(max_length=64, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    field_final_exam_type = models.CharField(db_column='_final_exam_type', max_length=64, blank=True,
                                             null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_student_task_activity'
        db_table_comment = 'Talabalarning topshiriqlarga bergan javoblari'


class ESubgroup(models.Model):
    name = models.CharField(max_length=256)
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_subgroup'
        db_table_comment = 'Kichik guruh ma`lumotlari'


class ESubject(models.Model):
    code = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=256)
    field_subject_group = models.ForeignKey('HSubjectGroup', models.DO_NOTHING,
                                            db_column='_subject_group')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey('HEducationType', models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    in_curriculum = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_subject'
        db_table_comment = 'OTMdagi fanlar ro`yxati'


class ESubjectExamSchedule(models.Model):
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING, db_column='_exam_type', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_auditorium = models.ForeignKey(EAuditorium, models.DO_NOTHING, db_column='_auditorium', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_week = models.ForeignKey(ECurriculumWeek, models.DO_NOTHING, db_column='_week', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    exam_name = models.CharField(max_length=64, blank=True, null=True)
    exam_date = models.DateField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    final_exam_type = models.CharField(max_length=64, blank=True, null=True)
    field_permission = models.BooleanField(db_column='_permission', blank=True,
                                           null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_subject_exam_schedule'
        db_table_comment = 'Nazorat jadvali'


class ESubjectFileResource(models.Model):
    title = models.CharField(max_length=256)
    comment = models.CharField(max_length=2000, blank=True, null=True)
    field_curriculum_subject = models.ForeignKey(ECurriculumSubject, models.DO_NOTHING,
                                                 db_column='_curriculum_subject')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING, db_column='_training_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING, db_column='_employee', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    language = models.JSONField(blank=True, null=True)
    files = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    url = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_subject_file_resource'


class ESubjectResource(models.Model):
    name = models.CharField(max_length=256)
    comment = models.TextField()
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_language = models.ForeignKey('HLanguage', models.DO_NOTHING,
                                       db_column='_language')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING,
                                            db_column='_subject_topic')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    filename = models.JSONField(blank=True, null=True)
    path = models.CharField(max_length=500, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    published_at = models.DateTimeField(blank=True, null=True)
    resource_type = models.IntegerField(blank=True, null=True)
    test_duration = models.IntegerField(blank=True, null=True)
    test_questions = models.IntegerField(blank=True, null=True)
    test_attempt_count = models.IntegerField(blank=True, null=True)
    test_question_count = models.IntegerField(blank=True, null=True)
    test_random = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_subject_resource'
        db_table_comment = 'O`qituvchilarning fan bo`yicha resurslari'


class ESubjectResourceQuestion(models.Model):
    name = models.TextField()
    content = models.TextField()
    content_r = models.TextField()
    answers = models.JSONField(blank=True, null=True)
    field_answer = models.JSONField(db_column='_answer', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_language = models.ForeignKey('HLanguage', models.DO_NOTHING,
                                       db_column='_language')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING, db_column='_subject_topic',
                                            blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_subject_resource = models.ForeignKey(ESubjectResource, models.DO_NOTHING, db_column='_subject_resource',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    field_subject_task = models.ForeignKey('ESubjectTask', models.DO_NOTHING, db_column='_subject_task', blank=True,
                                           null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_subject_resource_question'
        db_table_comment = 'O`qituvchilarning fan bo`yicha kiritgan test savollari'


class ESubjectSchedule(models.Model):
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING, db_column='_training_type', blank=True,
                                            null=True)  # Field renamed because it started with '_'.
    field_auditorium = models.ForeignKey(EAuditorium, models.DO_NOTHING, db_column='_auditorium', blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING, db_column='_subject_topic',
                                            blank=True, null=True)  # Field renamed because it started with '_'.
    field_week = models.ForeignKey(ECurriculumWeek, models.DO_NOTHING, db_column='_week', blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_lesson_pair = models.CharField(db_column='_lesson_pair',
                                         max_length=64)  # Field renamed because it started with '_'.
    lesson_date = models.DateField()
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    additional = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_subject_schedule'
        db_table_comment = 'Dars jadvali'


class ESubjectTask(models.Model):
    name = models.CharField(max_length=256)
    comment = models.TextField()
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_language = models.ForeignKey('HLanguage', models.DO_NOTHING,
                                       db_column='_language')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_subject_topic = models.ForeignKey(ECurriculumSubjectTopic, models.DO_NOTHING, db_column='_subject_topic',
                                            blank=True, null=True)  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_marking_category = models.CharField(db_column='_marking_category',
                                              max_length=64)  # Field renamed because it started with '_'.
    max_ball = models.IntegerField()
    deadline = models.DateTimeField()
    attempt_count = models.IntegerField(blank=True, null=True)
    filename = models.JSONField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    published_at = models.DateTimeField(blank=True, null=True)
    field_exam_type = models.ForeignKey('HExamType', models.DO_NOTHING, db_column='_exam_type', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_task_type = models.CharField(db_column='_task_type', max_length=64, blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    test_duration = models.IntegerField(blank=True, null=True)
    question_count = models.IntegerField(blank=True, null=True)
    random = models.BooleanField(blank=True, null=True)
    field_final_exam_type = models.CharField(db_column='_final_exam_type', max_length=64, blank=True,
                                             null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_subject_task'
        db_table_comment = 'O`qituvchilarning fan bo`yicha talabalarga beradigan vazifalari'


class ESubjectTaskStudent(models.Model):
    field_subject_task = models.ForeignKey(ESubjectTask, models.DO_NOTHING, db_column='_subject_task', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    field_training_type = models.ForeignKey('HTrainingType', models.DO_NOTHING,
                                            db_column='_training_type')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_employee = models.ForeignKey(EEmployee, models.DO_NOTHING,
                                       db_column='_employee')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_group = models.ForeignKey(EGroup, models.DO_NOTHING,
                                    db_column='_group')  # Field renamed because it started with '_'.
    field_task_status = models.CharField(db_column='_task_status', max_length=64, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    published_at = models.DateTimeField(blank=True, null=True)
    attempt_count = models.IntegerField(blank=True, null=True)
    field_task_type = models.CharField(db_column='_task_type', max_length=64, blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_subject_resource = models.ForeignKey(ESubjectResource, models.DO_NOTHING, db_column='_subject_resource',
                                               blank=True, null=True)  # Field renamed because it started with '_'.
    data = models.TextField(blank=True, null=True)  # This field type is a guess.
    correct = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    percent = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    field_final_exam_type = models.CharField(db_column='_final_exam_type', max_length=64, blank=True,
                                             null=True)  # Field renamed because it started with '_'.
    deadline = models.DateTimeField(blank=True, null=True)
    final_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_subject_task_student'
        unique_together = (('field_subject_task', 'field_student', 'field_education_year', 'field_semester',
                            'field_subject', 'field_final_exam_type'),)
        db_table_comment = 'Fan bo`yicha talabalarga biriktirilgan vazifalar'


class ESystemClassifier(models.Model):
    classifier = models.CharField(unique=True, max_length=64)
    name = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    options = models.JSONField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_system_classifier'


class ESystemConfig(models.Model):
    path = models.CharField(unique=True, max_length=256, blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_system_config'


class ESystemLog(models.Model):
    field_admin = models.ForeignKey(EAdmin, models.DO_NOTHING, db_column='_admin', blank=True,
                                    null=True)  # Field renamed because it started with '_'.
    admin_name = models.CharField(max_length=255)
    action = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=16000, blank=True, null=True)
    get = models.JSONField(blank=True, null=True)
    post = models.JSONField(blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    x_ip = models.CharField(max_length=64, blank=True, null=True)
    query = models.CharField(max_length=2048, blank=True, null=True)
    created_at = models.DateTimeField()
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING, db_column='_student', blank=True,
                                      null=True)  # Field renamed because it started with '_'.
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_system_log'


class ESystemLogin(models.Model):
    login = models.CharField(max_length=32)
    status = models.CharField(max_length=16, blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    query = models.CharField(max_length=256, blank=True, null=True)
    created_at = models.DateTimeField()
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_system_login'


class ESystemMessage(models.Model):
    category = models.CharField(max_length=32, blank=True, null=True)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'e_system_message'


class ESystemMessageTranslation(models.Model):
    id = models.OneToOneField(ESystemMessage, models.DO_NOTHING, db_column='id',
                              primary_key=True)  # The composite primary key (id, language) found, that is not supported. The first column is selected.
    language = models.CharField(max_length=16)
    translation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_system_message_translation'
        unique_together = (('id', 'language'),)


class ESystemSyncLog(models.Model):
    model = models.CharField(max_length=256)
    model_id = models.CharField(max_length=64)
    description = models.CharField(max_length=256, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    error = models.CharField(max_length=2048, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    delete = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_system_sync_log'


class ESystemSyncModel(models.Model):
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'e_system_sync_model'


class ETranscriptSubject(models.Model):
    field_academic_information = models.ForeignKey(EAcademicInformation, models.DO_NOTHING,
                                                   db_column='_academic_information')  # Field renamed because it started with '_'.
    field_student = models.ForeignKey(EStudent, models.DO_NOTHING,
                                      db_column='_student')  # Field renamed because it started with '_'.
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_semester = models.CharField(db_column='_semester',
                                      max_length=64)  # Field renamed because it started with '_'.
    field_subject = models.ForeignKey(ESubject, models.DO_NOTHING,
                                      db_column='_subject')  # Field renamed because it started with '_'.
    curriculum_name = models.CharField(max_length=256)
    education_year_name = models.CharField(max_length=255)
    semester_name = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    subject_name = models.CharField(max_length=255)
    total_acload = models.IntegerField(blank=True, null=True)
    credit = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_point = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'e_transcript_subject'


class EUniversity(models.Model):
    code = models.CharField(unique=True, max_length=10)
    tin = models.CharField(max_length=255)
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=255)
    field_ownership = models.ForeignKey('HOwnership', models.DO_NOTHING, db_column='_ownership', blank=True,
                                        null=True)  # Field renamed because it started with '_'.
    field_university_form = models.ForeignKey('HUniversityForm', models.DO_NOTHING, db_column='_university_form',
                                              blank=True, null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    field_soato = models.CharField(db_column='_soato', max_length=64, blank=True,
                                   null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_diff = models.JSONField(db_column='_sync_diff', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    mailing_address = models.TextField(blank=True, null=True)
    bank_details = models.TextField(blank=True, null=True)
    accreditation_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_university'
        db_table_comment = 'OTM ma`lumotlari'


class HAcademicDegree(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_academic_degree'
        db_table_comment = 'Ilmiy darajalar turlari'


class HAcademicMobileType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_academic_mobile_type'
        db_table_comment = 'Akademik mobillik turlari'


class HAcademicRank(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_academic_rank'
        db_table_comment = 'Ilmiy unvonlar turlari'


class HAcademicReason(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_academic_reason'
        db_table_comment = 'Akademik taСtil berish sabablari'


class HAccommodation(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_accommodation'
        db_table_comment = 'Talabalar yashash joylari turlari'


class HAttendanceSetting(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_attendance_setting'
        db_table_comment = 'Davomat chegaralari'


class HAuditoriumType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_auditorium_type'
        db_table_comment = 'OСquv auditoriyalari turlari'


class HBachelorSpeciality(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_bachelor_speciality'


class HBuilding(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=500)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_building'
        db_table_comment = 'OTMdagi binolar ro`yxati'


class HCitizenshipType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_citizenship_type'
        db_table_comment = 'Fuqarolik holatlari turlari'


class HContractClass(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_contract_class'
        db_table_comment = 'Shartnoma toifalari'


class HContractSummaType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_contract_summa_type'
        db_table_comment = 'Shartnoma summasi turlari'


class HContractType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_contract_type'
        db_table_comment = 'Shartnoma turlari'


class HCountry(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_country'
        db_table_comment = 'Davlatlar nomlari'


class HCourse(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_course'
        db_table_comment = 'OСquv kurslari'


class HDecreeType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_decree_type'
        db_table_comment = 'Buyruq turlari'


class HDeviceType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_device_type'
        db_table_comment = 'AKT qurilmalari turlari'


class HDiplomBlankCategory(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_diplom_blank_category'
        db_table_comment = 'Diplom blankalari kategoriyalari turlari'


class HDiplomBlankStatus(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_diplom_blank_status'
        db_table_comment = 'Diplom blankalari statuslari turlari'


class HDoctoralStudentType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_doctoral_student_type'
        db_table_comment = 'Doktorant talabalar toifalari'


class HDoctorateStudentStatus(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_doctorate_student_status'
        db_table_comment = 'Doktorant statusi turlari'


class HEducationForm(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_education_form'
        db_table_comment = 'TaТlim shakllari'


class HEducationType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_education_type'
        db_table_comment = 'TaТlim turlari'


class HEducationWeekType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_education_week_type'
        db_table_comment = 'OСquv grafigi xaftalarining turlari'


class HEducationYear(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_education_year'
        db_table_comment = "O'quv yillari"


class HEmployeeType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_employee_type'
        db_table_comment = 'Xodimlar toifalari'


class HEmploymentForm(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_employment_form'
        db_table_comment = 'Mehnat shakllari turlari'


class HEmploymentStaff(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_employment_staff'
        db_table_comment = 'Mehnat stavkalari turlari'


class HExamFinish(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_exam_finish'
        db_table_comment = 'Fanning yakuniy nazorat shakli'


class HExamType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_exam_type'
        db_table_comment = 'Nazorat turlari'


class HExpelReason(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_expel_reason'
        db_table_comment = 'Talabalarni chetlashtirish sabablari'


class HFinalExamType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_final_exam_type'
        db_table_comment = 'Qaydnoma turlari'


class HGender(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_gender'
        db_table_comment = 'Jins turlari'


class HGradeType(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    field_marking_system = models.ForeignKey('HMarkingSystem', models.DO_NOTHING,
                                             db_column='_marking_system')  # Field renamed because it started with '_'.
    min_border = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_border = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_grade_type'
        unique_together = (('code', 'field_marking_system'),)
        db_table_comment = 'Baho turlarining nomlari'


class HGraduateFieldsType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_graduate_fields_type'
        db_table_comment = 'Bitiruvchilarning iqtisodiyot sohalari va tarmoqlari boСyicha ishga joylashishi'


class HGraduateInactiveType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_graduate_inactive_type'
        db_table_comment = 'Iqtisodiy faol boСlmagan bitiruvchilar turlari'


class HLanguage(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_language'
        db_table_comment = 'TaТlim tillari'


class HLessonPair(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_lesson_pair'
        unique_together = (('code', 'field_education_year'),)
        db_table_comment = 'Juftliklar (paralar)'


class HLocality(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_locality'
        db_table_comment = 'Loyihalar toifalari'


class HLocalityType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_locality_type'
        db_table_comment = 'Fakultet turlari'


class HMarkingSystem(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    minimum_limit = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    count_final_exams = models.IntegerField(blank=True, null=True)
    gpa_limit = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_marking_system'
        db_table_comment = 'Baholash tizimlari'


class HMasterSpeciality(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_master_speciality'


class HMethodicalPublicationType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_methodical_publication_type'
        db_table_comment = 'Uslubiy ishlar turlari'


class HNationality(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_nationality'
        db_table_comment = 'Millatlar nomlari'


class HOwnership(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_ownership'
        db_table_comment = 'OTM mulkchilik shakllari'


class HPatientType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_patient_type'
        db_table_comment = 'Intellektual mulk turlari'


class HPaymentForm(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_payment_form'
        db_table_comment = 'ToСlov turlari'


class HProjectCurrency(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_project_currency'
        db_table_comment = 'Ilmiy loyiha valyutasi turlari'


class HProjectExecutorType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_project_executor_type'
        db_table_comment = 'Ilmiy loyiha ijrochilari turlari'


class HProjectType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_project_type'
        db_table_comment = 'Ilmiy loyihalar turlari'


class HPublicationDatabase(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_publication_database'
        db_table_comment = 'Ilmiy ishlar bazalari turlari'


class HQualification(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_qualification'
        db_table_comment = 'Malaka oshirish joylari'


class HRatingGrade(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    template = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_rating_grade'


class HScienceBranch(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_science_branch'


class HScientificPlatform(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_scientific_platform'
        db_table_comment = 'Ilmiy platforma turlari'


class HScientificPublicationType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_scientific_publication_type'
        db_table_comment = 'Ilmiy ishlar turlari'


class HSemester(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_semester'
        db_table_comment = 'Semestr nomlari'


class HSemestr(models.Model):
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    field_curriculum = models.ForeignKey(ECurriculum, models.DO_NOTHING,
                                         db_column='_curriculum')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(EEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    start_date = models.DateField()
    end_date = models.DateField()
    accepted = models.BooleanField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    last = models.BooleanField(blank=True, null=True)
    field_level = models.ForeignKey(HCourse, models.DO_NOTHING, db_column='_level', blank=True,
                                    null=True)  # Field renamed because it started with '_'.

    # def get_all_cur(self):
    #     return self.field_curriculum.field_department.ef

    class Meta:
        managed = False
        db_table = 'h_semestr'
        unique_together = (('code', 'field_curriculum'),)
        db_table_comment = 'O`zlashtirish qaydnomasi shakllari'


class HSemestrType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_semestr_type'
        db_table_comment = 'Semestr turlari'


class HSoato(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_soato'
        db_table_comment = 'Viloyat, tuman va shaharlar'


class HSocialCategory(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_social_category'
        db_table_comment = 'Talabalarning ijtimoiy toifalari'


class HSpecialityOrdinatura(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_speciality_ordinatura'


class HSportType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_sport_type'
        db_table_comment = 'Sport turlari'


class HStipendRate(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_stipend_rate'
        db_table_comment = 'Stipendiya turlari'


class HStructureType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_structure_type'
        db_table_comment = 'OTM boСlinmalari turlari'


class HStudentLivingStatus(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_student_living_status'
        db_table_comment = 'Talaba yashash joyining statusi'


class HStudentRoommateType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_student_roommate_type'
        db_table_comment = 'Talaba birgalikda yashaydiganlar toifasi'


class HStudentStatus(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_student_status'
        db_table_comment = 'Talaba statusi turlari'


class HStudentSuccess(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_student_success'
        db_table_comment = 'Talaba yutuqlari turlari'


class HStudentType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_student_type'
        db_table_comment = 'Talaba toifasi turlari'


class HSubjectBlock(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_subject_block'
        db_table_comment = 'OСquv reja fanlar bloklari'


class HSubjectGroup(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_subject_group'


class HSubjectType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_subject_type'
        db_table_comment = 'Fanlar toifalari'


class HTeacherPositionType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_teacher_position_type'
        db_table_comment = 'OTMdagi lavozimlar turlari'


class HTeacherStatus(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_teacher_status'
        db_table_comment = 'OСqituvchi statuslari turlari'


class HTeacherSuccess(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_teacher_success'
        db_table_comment = 'OСqituvchilar yutuqlari turlari'


class HTrainingType(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_training_type'
        db_table_comment = 'OСquv mashgСulotlari turlari'


class HUniversity(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_university'
        db_table_comment = 'Oliy taТlim muassasalari roСyxati'


class HUniversityForm(models.Model):
    code = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=256)
    position = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    field_parent = models.ForeignKey('self', models.DO_NOTHING, db_column='_parent', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    field_translations = models.JSONField(db_column='_translations', blank=True,
                                          null=True)  # Field renamed because it started with '_'.
    field_options = models.JSONField(db_column='_options', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'h_university_form'
        db_table_comment = 'Oliy taТlim muassasasi tashkiliy shakllari'


class HomeFakultet(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'home_fakultet'


class HomeGuruh(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    fakultet = models.ForeignKey(HomeFakultet, models.DO_NOTHING, blank=True, null=True)
    kafedra = models.ForeignKey('HomeKafedra', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'home_guruh'


class HomeKafedra(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    fakultet = models.ForeignKey(HomeFakultet, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'home_kafedra'


class HomeKafedraHujjatlar(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'home_kafedra_hujjatlar'


class HomeTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    test = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'home_test'


class Migration(models.Model):
    version = models.CharField(primary_key=True, max_length=180)
    apply_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migration'


class NewsPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    titel = models.CharField(max_length=150)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'news_post'


class OauthAccessToken(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    field_client = models.ForeignKey('OauthClient', models.DO_NOTHING,
                                     db_column='_client')  # Field renamed because it started with '_'.
    field_user = models.IntegerField(db_column='_user', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    revoked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'oauth_access_token'


class OauthAccessTokenScope(models.Model):
    field_access_token = models.ForeignKey(OauthAccessToken, models.DO_NOTHING,
                                           db_column='_access_token')  # Field renamed because it started with '_'.
    field_scope = models.ForeignKey('OauthScope', models.DO_NOTHING,
                                    db_column='_scope')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'oauth_access_token_scope'


class OauthAuthCode(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    field_client = models.ForeignKey('OauthClient', models.DO_NOTHING,
                                     db_column='_client')  # Field renamed because it started with '_'.
    field_user = models.IntegerField(db_column='_user', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    expires_at = models.DateTimeField()
    revoked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'oauth_auth_code'


class OauthAuthCodeScope(models.Model):
    field_auth_code = models.ForeignKey(OauthAuthCode, models.DO_NOTHING,
                                        db_column='_auth_code')  # Field renamed because it started with '_'.
    field_scope = models.ForeignKey('OauthScope', models.DO_NOTHING,
                                    db_column='_scope')  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'oauth_auth_code_scope'


class OauthClient(models.Model):
    field_user = models.IntegerField(db_column='_user', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    secret = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)
    redirect = models.TextField(blank=True, null=True)
    token_type = models.SmallIntegerField(blank=True, null=True)
    grant_type = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    revoked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_client'


class OauthRefreshToken(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    field_access_token = models.BigIntegerField(db_column='_access_token')  # Field renamed because it started with '_'.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    expires_at = models.DateTimeField()
    revoked = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'oauth_refresh_token'


class OauthScope(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_scope'


class RContract(models.Model):
    total = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    field_department = models.ForeignKey(EDepartment, models.DO_NOTHING,
                                         db_column='_department')  # Field renamed because it started with '_'.
    field_education_year = models.ForeignKey(HEducationYear, models.DO_NOTHING,
                                             db_column='_education_year')  # Field renamed because it started with '_'.
    field_education_type = models.ForeignKey(HEducationType, models.DO_NOTHING,
                                             db_column='_education_type')  # Field renamed because it started with '_'.
    field_education_form = models.ForeignKey(HEducationForm, models.DO_NOTHING,
                                             db_column='_education_form')  # Field renamed because it started with '_'.
    field_course = models.ForeignKey(HCourse, models.DO_NOTHING,
                                     db_column='_course')  # Field renamed because it started with '_'.
    date = models.DateField()
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField(blank=True, null=True)
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    last = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_contract'
        unique_together = (('field_department', 'field_education_year', 'field_education_type', 'field_education_form',
                            'field_course', 'date'),)
        db_table_comment = 'Shartnomalar hisoboti'


class REmployment(models.Model):
    qty = models.IntegerField(blank=True, null=True)
    field_department = models.IntegerField(db_column='_department')  # Field renamed because it started with '_'.
    field_education_year = models.CharField(db_column='_education_year',
                                            max_length=6)  # Field renamed because it started with '_'.
    field_education_type = models.CharField(db_column='_education_type',
                                            max_length=6)  # Field renamed because it started with '_'.
    field_education_form = models.CharField(db_column='_education_form',
                                            max_length=6)  # Field renamed because it started with '_'.
    field_payment_form = models.CharField(db_column='_payment_form',
                                          max_length=6)  # Field renamed because it started with '_'.
    field_gender = models.CharField(db_column='_gender', max_length=6)  # Field renamed because it started with '_'.
    workplace_compatibility = models.CharField(max_length=6)
    field_graduate_fields_type = models.CharField(db_column='_graduate_fields_type', max_length=6, blank=True,
                                                  null=True)  # Field renamed because it started with '_'.
    field_graduate_inactive_type = models.CharField(db_column='_graduate_inactive_type', max_length=6, blank=True,
                                                    null=True)  # Field renamed because it started with '_'.
    field_qid = models.BigIntegerField(db_column='_qid', blank=True,
                                       null=True)  # Field renamed because it started with '_'.
    field_uid = models.CharField(db_column='_uid', unique=True, max_length=255, blank=True,
                                 null=True)  # Field renamed because it started with '_'.
    field_sync = models.BooleanField(db_column='_sync', blank=True,
                                     null=True)  # Field renamed because it started with '_'.
    updated_at = models.DateTimeField(blank=True, null=True)
    field_sync_date = models.DateTimeField(db_column='_sync_date', blank=True,
                                           null=True)  # Field renamed because it started with '_'.
    field_sync_status = models.CharField(db_column='_sync_status', max_length=16, blank=True,
                                         null=True)  # Field renamed because it started with '_'.
    last = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'r_employment'
        unique_together = (('field_department', 'field_education_year', 'field_education_type', 'field_education_form',
                            'field_payment_form', 'field_gender', 'field_graduate_fields_type',
                            'field_graduate_inactive_type', 'workplace_compatibility'),)
        db_table_comment = 'Bandlik hisoboti'
