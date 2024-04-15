from django.urls import reverse
from django.db import models

# Create your models here.

class TblUser(models.Model):
    BLOCK_VERSION_0 = 0
    BLOCK_VERSION_1 = 1
    BLOCK_VERSION_2 = 2
    BLOCK_VERSION_3 = 3

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    password_hash = models.CharField(max_length=60, blank=True, null=True)
    auth_key = models.CharField(max_length=32, blank=True, null=True)
    access_token = models.CharField(max_length=40)
    logged_at = models.IntegerField(blank=True, null=True)
    created_at = models.IntegerField(blank=True, null=True)
    updated_at = models.IntegerField(blank=True, null=True)
    is_new_user = models.BooleanField(default=False)
    block_version = models.SmallIntegerField(default=1)
    accepted_terms_id = models.IntegerField(default=None)
    accepted_terms_date = models.IntegerField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    @property
    def login_url(self):
        url = reverse('login_user_by_access_token')
        return '{}?username={}&token={}'.format(url, self.username, self.access_token)

    def __str__(self):
        return self.username

    # @property
    # def get_block_version(self):
    #     if self.block_version == self.BLOCK_VERSION_0:
    #         return self.BLOCK_VERSION_0
    #     if self.block_version == self.BLOCK_VERSION_1:
    #         return self.BLOCK_VERSION_1
    #     if self.block_version == self.BLOCK_VERSION_2:
    #         return self.BLOCK_VERSION_2
    #     if self.block_version == self.BLOCK_VERSION_3:
    #         return self.BLOCK_VERSION_3

    class Meta:
        managed = True
        db_table = 'tbl_user'



# class TblCountry(models.Model):
#     id = models.AutoField(primary_key=True)
#     code = models.CharField(max_length=50, blank=True, null=True)
#     is_enabled = models.IntegerField(blank=True, null=True)
#     top_receivers_limit = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tbl_country'
#         verbose_name = "Country"
#         verbose_name_plural = "Countries"
#
#
# class TblProvince(models.Model):
#     id = models.AutoField(primary_key=True)
#     country = models.ForeignKey(TblCountry, models.DO_NOTHING)
#     type = models.CharField(max_length=50, blank=True, null=True)
#     code = models.CharField(max_length=50, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     top_receivers_limit = models.IntegerField(default=0, null=False)
#     min_received_amount = models.IntegerField(default=0, null=False)
#     language = models.CharField(max_length=255, blank=True, null=True)
#     abbreviation = models.CharField(max_length=255, blank=True, null=False, default='')
#     stateUniqueId = models.CharField(max_length=255, blank=True, default=0)
#
#     class Meta:
#         managed = True
#         db_table = 'tbl_province'
#         verbose_name = "State"
#         verbose_name_plural = "States"
#
#     def __str__(self):
#         return self.name
#
#
# # model for district
# class TblZone(models.Model):
#     id = models.AutoField(primary_key=True)
#     code = models.CharField(max_length=50, blank=True, null=True)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     top_receivers_limit = models.IntegerField(default=0, null=False)
#     min_received_amount = models.IntegerField(default=0, null=False)
#     enabled_silver_package = models.SmallIntegerField(blank=True, null=True)
#     type = models.CharField(max_length=50, blank=True, null=True)
#     districtUniqueId = models.CharField(max_length=255, blank=True, default=0)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         managed = True
#         db_table = 'tbl_zone'
#         verbose_name = "District"
#         verbose_name_plural = "Districts"

# class TblMember(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey('TblUser', models.DO_NOTHING, blank=True, null=True)
#     package_code = models.CharField(max_length=50, blank=True, null=True)
#     reference_user_id = models.IntegerField(blank=True, null=True)
#     # parent_user_id = models.ForeignKey(
#     #     'self', related_name='children', to_field='user_id', on_delete=models.SET_NULL,
#     #     blank=True, null=True, db_column='parent_user_id')
#     parent_user_id = models.IntegerField(blank=True, null=True, db_index=True)
#     give_level = models.SmallIntegerField(blank=True, null=True)
#     receive_level = models.SmallIntegerField(blank=True, null=True)
#     total_received = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     # ninety_pmf_blocked_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     blocked_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     first_name = models.CharField(max_length=255, blank=True, null=True)
#     last_name = models.CharField(max_length=255, blank=True, null=True)
#     address_line_1 = models.CharField(max_length=255, blank=True, null=True)
#     address_line_2 = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     postal_code = models.CharField(max_length=50, blank=True, null=True)
#     country_code = models.CharField(max_length=50, blank=True, null=True)
#     zone_name = models.CharField(max_length=100, blank=True, null=True)
#     mobile = models.CharField(max_length=50, blank=True, null=True)
#     blood_group_code = models.CharField(max_length=50, blank=True, null=True)
#     gender = models.SmallIntegerField(blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)
#     payment_info = models.TextField(blank=True, null=True)
#     account_type_code = models.SmallIntegerField()
#     child_members_count = models.SmallIntegerField(blank=True, null=True)
#     direct_member_count = models.SmallIntegerField(blank=True, null=True)
#     status_code = models.SmallIntegerField(blank=True, null=True)
#     created_at = models.IntegerField(blank=True, null=True)
#     updated_at = models.IntegerField(blank=True, null=True)
#     paypal = models.CharField(max_length=150, blank=True, null=True)
#     paytm = models.CharField(max_length=100, blank=True, null=True)
#     phonepe = models.CharField(max_length=100, blank=True, null=True)
#     bhim_upi = models.CharField(max_length=100, blank=True, null=True)
#     google_pay = models.CharField(max_length=100, blank=True, null=True)
#     truecaller = models.CharField(max_length=150, blank=True, null=True)
#     profile_status_code = models.SmallIntegerField(blank=True, null=True)
#     whatsapp_number = models.CharField(max_length=255, blank=True, null=True)
#     telegram = models.CharField(max_length=100, blank=True, null=True)
#     # btc = models.TextField(blank=True, null=True)
#     # xrp = models.TextField(blank=True, null=True)
#     # xlm = models.TextField(blank=True, null=True)
#     # ncash = models.TextField(blank=True, null=True)
#     # trx = models.TextField(blank=True, null=True)
#     # btc_id = models.TextField(blank=True, null=True)
#     # xrp_id = models.TextField(blank=True, null=True)
#     # xlm_id = models.TextField(blank=True, null=True)
#     # ncash_id = models.TextField(blank=True, null=True)
#     # trx_id = models.TextField(blank=True, null=True)
#     district_id = models.SmallIntegerField(blank=True, null=True)
#     avatar = models.FileField(blank=True, null=True)
#     country_id = models.SmallIntegerField(blank=True, null=True)
#     state_id = models.SmallIntegerField(blank=True, null=True)
#     achiever_updated = models.SmallIntegerField(blank=True, null=True)
#     contact_number = models.CharField(max_length=20, blank=True, null=True)
#     upi_registered_account_number = models.CharField(max_length=20, blank=True, null=True)
#     upi_registered_bank_ifsc = models.CharField(max_length=20, blank=True, null=True)
#     account_holder_name = models.CharField(max_length=255, blank=True, null=True)
#     # upi_registered_mobile_number = models.CharField(max_length=20, blank=True, null=True)
#     adharcard_number = models.CharField(max_length=20, blank=True, null=True)
#     adharcard_image = models.FileField(blank=True, null=True)
#     pancard_number = models.CharField(max_length=20, blank=True, null=True)
#     pancard_image = models.FileField(blank=True, null=True)
#     nominee_name = models.CharField(max_length=255, blank=True, null=True)
#     nominee_contact_number = models.CharField(max_length=20, blank=True, null=True)
#     nominee_relationship = models.CharField(max_length=10, blank=True, null=True)
#     nominee_adharcard_number = models.CharField(max_length=20, blank=True, null=True)
#     nominee_adharcard_image = models.FileField(blank=True, null=True)
#     nominee_image = models.TextField(blank=True, null=True)
#     # is_interested = models.SmallIntegerField(blank=True, null=True)
#     deactivation_status = models.SmallIntegerField(blank=True, null=True)
#     card_avatar = models.TextField(blank=True, null=True)
#     fb_id = models.CharField(max_length=100, blank=True, null=True, default='')
#     bankUpiId = models.CharField(max_length=100, blank=True, null=True, default='')
#     houseNo = models.CharField(max_length=255, blank=True, null=True, default='')
#     nominee_adharcard_image_back = models.FileField(blank=True, null=True)
#     wardNo = models.CharField(max_length=100, blank=True, null=True, default='')
#     whatsapp = models.TextField(blank=True, null=True, default='')
#     upi_registered_bank_name = models.CharField(max_length=20, blank=True, null=True, default='')
#     upi_registered_bank_branch = models.CharField(max_length=20, blank=True, null=True, default='')
#     permanent_address_same_as_living = models.BooleanField(default=False)
#     living_address_line_1 = models.CharField(max_length=255, blank=True, null=True)
#     living_address_line_2 = models.CharField(max_length=255, blank=True, null=True)
#     living_address_house_no = models.CharField(max_length=255, blank=True, null=True)
#     living_address_ward_no = models.CharField(max_length=255, blank=True, null=True)
#     living_address_postal_code = models.CharField(max_length=255, blank=True, null=True)
#     activated_at = models.IntegerField(blank=True, null=True)
#     total_received_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     invitation_count = models.SmallIntegerField(default=0)
#     is_pending_genealogy = models.BooleanField(default=False)
#     is_refund_policy_active = models.BooleanField(default=False)
#     refund_policy_ends_at = models.DateField(null=True, blank=True)
#     total_spend_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     accumulated_received_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     # member current total spend
#     total_spend = models.DecimalField(max_digits=15, decimal_places=2, default=0)
#     last_seen = models.CharField(max_length=100, null=True, blank=True)
#     total_joined_givers = models.SmallIntegerField(default=0)
#     is_whatsapp_number_verified = models.BooleanField(default=False)
#     blocking_exception = models.BooleanField(default=False)
#     exception_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
#     is_profile_updated = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.first_name
#
#     class Meta:
#         managed = True
#         db_table = 'tbl_member'
#         verbose_name = "Base Member"
#         verbose_name_plural = "Base Members"
#
#     @property
#     def is_inactive(self):
#         return not self.parent_user_id


class Members(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(TblUser, on_delete=models.CASCADE, blank=True, null=True)
    package_code = models.CharField(max_length=255, null=True)
    reference_user_id = models.ForeignKey(
        TblUser, on_delete=models.CASCADE, blank=True, null=True, related_name='reference_user')
    parent_user_id = models.ForeignKey(
        TblUser, on_delete=models.CASCADE, blank=True, null=True, related_name='parent_user')
    give_level = models.SmallIntegerField(null=True)
    receive_level = models.SmallIntegerField(null=True)
    total_received = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    blocked_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    account_type_code = models.SmallIntegerField(null=True)
    child_members_count = models.SmallIntegerField(null=True)
    direct_member_count = models.SmallIntegerField(null=True)
    status_code = models.SmallIntegerField(null=True)
    created_at = models.IntegerField(null=True)
    updated_at = models.IntegerField(null=True)
    profile_status_code = models.SmallIntegerField(null=True)
    contact_number = models.CharField(max_length=30, null=True)
    deactivation_status = models.SmallIntegerField(null=True)
    card_avatar = models.CharField(max_length=255, null=True)
    permanent_address_same_as_living = models.BooleanField(null=True)
    activated_at = models.IntegerField(null=True)
    total_received_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    invitation_count = models.SmallIntegerField(default=0)
    is_pending_genealogy = models.BooleanField(default=False)
    is_refund_policy_active = models.BooleanField(default=False)
    refund_policy_ends_at = models.DateField(null=True)
    total_spend_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    accumulated_received_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_spend = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    last_seen = models.CharField(max_length=100, null=True)
    total_joined_givers = models.SmallIntegerField(default=0)
    is_whatsapp_number_verified = models.BooleanField(default=False)
    blocking_exception = models.BooleanField(default=False)
    exception_amount = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    is_profile_updated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class MemberNomineeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='nominee')
    nominee_name = models.CharField(max_length=255)
    nominee_contact_number = models.CharField(max_length=255)
    nominee_relationship = models.CharField(max_length=255)
    nominee_adharcard_number = models.CharField(max_length=255)
    nominee_adharcard_image = models.CharField(max_length=255)
    nominee_image = models.CharField(max_length=255)
    nominee_adharcard_image_back = models.CharField(max_length=255)

class MemberPersonalInfo(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='personal')
    first_name = models.CharField(max_length=255,null=True, blank=True)
    last_name = models.CharField(max_length=255,null=True, blank=True)
    mobile = models.CharField(max_length=30,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    blood_group_code = models.CharField(max_length=25, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    fb_id = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.CharField(max_length=255, null=True, blank=True)

class MemberAddress(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='address')
    address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country_code = models.CharField(max_length=5, null=True, blank=True)
    zone_name = models.CharField(max_length=100, null=True, blank=True)
    house_no = models.CharField(max_length=20, null=True, blank=True)
    ward_no = models.CharField(max_length=20, null=True, blank=True)
    living_address_house_no = models.CharField(max_length=20, null=True, blank  =True)
    living_address_line_1 = models.CharField(max_length=255, null=True, blank=True)
    living_address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    living_address_postal_code = models.CharField(max_length=20, null=True, blank=True)
    living_address_ward_no = models.CharField(max_length=20, null=True, blank=True)

        # state,district,panchayath/muncipality
class MemberPaymentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    member_id = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='payment_info')
    payment_info = models.CharField(max_length=255, null=True, blank=True)
    paypal = models.CharField(max_length=255, null=True, blank=True)
    paytm = models.CharField(max_length=255, null=True, blank=True)
    phonepe = models.CharField(max_length=255, null=True, blank=True)
    bhim_upi = models.CharField(max_length=255, null=True, blank=True)
    whatsapp_pay = models.CharField(max_length=255, null=True, blank=True)
    google_pay = models.CharField(max_length=255, null=True, blank=True)
    upi_registered_account_number = models.CharField(max_length=50, null=True, blank=True)
    upi_registered_bank_ifsc = models.CharField(max_length=20, null=True, blank=True)
    account_holder_name = models.CharField(max_length=255, null=True, blank=True)
    bank_upi_id = models.CharField(max_length=255, null=True, blank=True)
    upi_registered_bank_branch = models.CharField(max_length=255, null=True, blank=True)
    upi_registered_bank_name = models.CharField(max_length=255, null=True, blank=True)
#     # adharcard_number = models.CharField(max_length=20, null=True, blank=True)
#     # adharcard_image = models.CharField(max_length=255, null=True, blank=True)
#     # pancard_number = models.CharField(max_length=20, null=True, blank=True)
#     # pancard_image = models.CharField(max_length=255, null=True, blank=True)
