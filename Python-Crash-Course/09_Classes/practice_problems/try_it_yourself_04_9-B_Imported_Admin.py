# 9-11 Imported Admin: Start with your code from Exercise 9-8. Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

import admin
        
sattire = admin.Admin('Sattire', 729, 20, 'cuttingbudgets@gmail.com')
sattire.privileges.show_privileges()   