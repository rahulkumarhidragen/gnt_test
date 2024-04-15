from django.core.management.base import BaseCommand
from django.db import transaction
from gnt_app.models import Members, MemberPersonalInfo, MemberAddress, MemberPaymentInfo, TblMember, TblUser


class Command(BaseCommand):
    help = 'Migrates old member data to new structured models'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting migration process...'))
        self.migrate_member_data()

    def migrate_member_data(self):
        old_members = TblMember.objects.using('mysql').iterator()
        try:

            with transaction.atomic():
                for old_member in old_members:
                    if old_member.id > 95250:
                        print("Contact Number:", old_member.contact_number)
                        print("WhatsApp Number:", old_member.whatsapp_number)
                        print("Postal Code:", old_member.postal_code)
                        print("House Number:", old_member.house_no)
                        print("Ward Number:", old_member.ward_no)
                        print("Living Address House Number:", old_member.living_address_house_no)
                        print("UPI Registered Bank IFSC:", old_member.upi_registered_bank_ifsc)
                    # Creating Member instance
                    new_member = Members.objects.create(
                        user=self.get_user_reference(old_member.user_id),  # Ensure the user exists in your new system or map it appropriately
                        package_code=old_member.package_code,
                        reference_user_id=self.get_user_reference(old_member.reference_user_id),  # Ensure the user exists or is null
                        parent_user_id=self.get_user_reference(old_member.parent_user_id),  # Ensure the user exists or is null
                        give_level=old_member.give_level,
                        receive_level=old_member.receive_level,
                        total_received=old_member.total_received,
                        blocked_amount=old_member.blocked_amount,
                        account_type_code=old_member.account_type_code,
                        child_members_count=old_member.child_members_count,
                        direct_member_count=old_member.direct_member_count,
                        status_code=old_member.status_code,
                        created_at=old_member.created_at,
                        updated_at=old_member.updated_at,
                        profile_status_code=old_member.profile_status_code,
                        contact_number=old_member.contact_number,
                        deactivation_status=old_member.deactivation_status,
                        card_avatar=old_member.card_avatar,
                        permanent_address_same_as_living=old_member.permanent_address_same_as_living,
                        activated_at=old_member.activated_at,
                        total_received_amount=old_member.total_received_amount,
                        invitation_count=old_member.invitation_count,
                        is_pending_genealogy=old_member.is_pending_genealogy,
                        is_refund_policy_active=old_member.is_refund_policy_active,
                        refund_policy_ends_at=old_member.refund_policy_ends_at,
                        total_spend_amount=old_member.total_spend_amount,
                        accumulated_received_amount=old_member.accumulated_received_amount,
                        total_spend=old_member.total_spend,
                        last_seen=old_member.last_seen,
                        total_joined_givers=old_member.total_joined_givers,
                        is_whatsapp_number_verified=old_member.is_whatsapp_number_verified,
                        blocking_exception=old_member.blocking_exception,
                        exception_amount=old_member.exception_amount,
                        is_profile_updated=old_member.is_profile_updated
                    )

                    # Creating MemberPersonalInfo instance
                    MemberPersonalInfo.objects.create(
                        member=new_member,
                        first_name=old_member.first_name,
                        last_name=old_member.last_name,
                        mobile=old_member.mobile,
                        dob=old_member.dob,
                        gender=old_member.gender,
                        blood_group_code=old_member.blood_group_code,
                        whatsapp_number=old_member.whatsapp_number,
                        telegram=old_member.telegram,
                        fb_id=old_member.fb_id,
                        avatar=old_member.avatar
                    )

                    # Creating MemberAddress instance
                    MemberAddress.objects.create(
                        member_id=new_member,
                        address_line_1=old_member.address_line_1,
                        address_line_2=old_member.address_line_2,
                        city=old_member.city,
                        postal_code=old_member.postal_code,
                        country_code=old_member.country_code,
                        zone_name=old_member.zone_name,
                        house_no=old_member.houseNo,
                        ward_no=old_member.wardNo,
                        living_address_house_no=old_member.living_address_house_no,
                        living_address_line_1=old_member.living_address_line_1,
                        living_address_line_2=old_member.living_address_line_2,
                        living_address_postal_code=old_member.living_address_postal_code,
                        living_address_ward_no=old_member.living_address_ward_no
                    )

                    # Creating MemberPaymentInfo instance
                    MemberPaymentInfo.objects.create(
                        member_id=new_member,
                        payment_info=old_member.payment_info,
                        paypal=old_member.paypal,
                        paytm=old_member.paytm,
                        phonepe=old_member.phonepe,
                        bhim_upi=old_member.bhim_upi,
                        whatsapp_pay=old_member.whatsapp,
                        google_pay=old_member.google_pay,
                        upi_registered_account_number=old_member.upi_registered_account_number,
                        upi_registered_bank_ifsc=old_member.upi_registered_bank_ifsc,
                        account_holder_name=old_member.account_holder_name,
                        bank_upi_id=old_member.bankUpiId,
                        upi_registered_bank_branch=old_member.upi_registered_bank_branch,
                        upi_registered_bank_name=old_member.upi_registered_bank_name
                    )

                    # Optionally log each batch or give some output to monitor the progress
                    self.stdout.write(self.style.SUCCESS(f'Migrated member ID: {new_member.id if new_member else None }'))
        except Exception as e:
            print(e)

    def get_user_reference(self, user_id):
        return TblUser.objects.filter(id=user_id).first()



# This script should efficiently handle the migration of your member data, assuming all referenced fields in `TblMember` directly map to your new model fields. Make sure the necessary user and reference entities exist or are correctly handled before running this script, especially in production environments.

