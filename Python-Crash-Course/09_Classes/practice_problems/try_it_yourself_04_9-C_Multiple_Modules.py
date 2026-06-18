# 9-12 Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is working correctly.

from admin_standalone import Admin

sattire = Admin('Sattire', 729, 20, 'cuttingbudgets@gmail.com')
sattire.privileges.show_privileges()   