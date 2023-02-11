import smtplib as smt

#  Call the class fo the smtplib and connect it to server with its ports number
obj = smt.SMTP("smtp.gmail.com", 587)
# connect it
obj.ehlo()
obj.starttls()
obj.login("mahnoorshoukat626@gmail.com", "95119511")
subject = "Wordpress Developer"
body = "Get your online store up and running with our e-commerce services on Fiverr. Our team of experts will help you set up a user-friendly, customized e-commerce platform to help you sell your products or services online. We specialize in popular platforms such as Shopify, WooCommerce, and Magento, and can provide everything from setup and configuration to theme customization and payment gateway integration. Trust us to deliver a seamless online shopping experience for your customers."


message = "subject{}\n\n{}".format(subject, body)
# you can gave multiple emails here
list_address = ["abdullahniaz424@gmail.com"]

obj.sendmail("mahnoorshoukat626@gmail.com", list_address, message)
print("Send Email")
obj.quit()
