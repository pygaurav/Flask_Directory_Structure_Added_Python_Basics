from app import app
from app import security
import app.admin.admin_panel as ad

# abs = security.Student("The text is overflowing !",email="gb@gb.com")
# abs.create_ticket()
abp = ad.AnotherStudent("The text is overflowing !",email="gb@gb.com")
abp.getTimeofTicket()
abp.create_ticket()

ad.hello(1,2,name="Gaurav")
ad.hellyeah()
app.run(port=5000)