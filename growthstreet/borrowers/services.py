from growthstreet.borrowers.models import Borrower, Company


class BorrowerService(object):
    def create_new_borrower(self, phonenumber, borrow_amount, loan_days, loan_reason, user):
        new_borrower = Borrower.objects.create(
            phonenumber=phonenumber,
            borrow_amount=borrow_amount,
            loan_days=loan_days,
            loan_reason=loan_reason,
            user=user
        )
        return new_borrower

    def get_borrower_by_user_id(self, user_id):
        return Borrower.objects.get(user_id=user_id)


class CompanyService(object):
    def create_new_company(self, name, address, registered_number, sector, user_pk):
        borrower = BorrowerService().get_borrower_by_user_id(user_pk)
        new_company = Company.objects.create(
            name=name,
            address=address,
            registered_number=registered_number,
            sector=sector
        )
        new_company.borrower_set.add(borrower)
        return new_company
