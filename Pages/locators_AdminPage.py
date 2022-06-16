class locators():
    #Start from loginpage
    emailId_textbox="//input[@id='emailId']"
    password_textbox="//input[@id='password']"      #will work for signUp page also
    confirm_Password_textbox="//input[@id='confirmPassword']"   #will work for signUp page also
    login_button="//button[@type='submit']"                     #will work as signUp button
    signUp_link="//a[contains(text(),'Signup')]"


    #FoodSwipe Home
    accountHolder_nameIcon_button="//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-av538e-MuiButtonBase-root-MuiIconButton-root']"
    logout_link="//p[contains(text(),'Logout')]"
    settings_link="//p[contains(text(),'Settings')]"

    #Menu buttons
    allOtherItems_link="//span[contains(text(),'ALL OTHER ITEMS')]"
    breakfast_link="//span[contains(text(),'BREAKFAST')]"
    lunch_link="//span[contains(text(),'LUNCH')]"
    snacks_link="//span[contains(text(),'SNACKS')]"
    dinner_link="//span[contains(text(),'DINNER')]"


    #Add Item
    addItem_button="//b[contains(text(),'Add Item')]"
    itemName_textbox="//input[@id='itemName']"
    itemDesc_textbox="//input[@id='itemDesc']"
    Price_textbox="//input[@id='price']"
    category_dropdown="//div[@id='mui-component-select-menuCategory']"
    quantity_textbox="//input[@id='quantity']"
    mnuStatus_enable_radio="//span[@class='MuiRadio-root MuiRadio-colorPrimary MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary PrivateSwitchBase-root css-vqmohf-MuiButtonBase-root-MuiRadio-root']//input[@type='radio']"
    mnuStatus_disable_radio=""
    submit_button="//button[@type='submit']"

    successmsg_link="//div[@class='successMsg']"
    close_icon="//div[@class='btn-outline-secondary goBack justify-content-end']//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-i4bv87-MuiSvgIcon-root']"

    #Locators for searchItem
    searchItem_textbox="//input[@id='input-search-header']"

    #Add User
    addUser_button="//b[contains(text(),'Add User')]"
    firstName_textbox="//input[@id='firstName']"    #will work for signUp page also
    lastName_textbox="//input[@id='lastName']"      #will work for signUp page also
    emailAddr_textbox="//input[@id='emailId']"      #will work for signUp page also
    PhoneNo_textbox="//input[@id='contactNumber']"  #will work for signUp page also
    admin_radio="//span[@class='MuiRadio-root MuiRadio-colorPrimary MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary PrivateSwitchBase-root css-vqmohf-MuiButtonBase-root-MuiRadio-root']//input[@type='radio']"
    employee_radio="//span[@class='MuiRadio-root MuiRadio-colorPrimary MuiButtonBase-root MuiRadio-root MuiRadio-colorPrimary PrivateSwitchBase-root Mui-checked css-vqmohf-MuiButtonBase-root-MuiRadio-root']//input[@type='radio']"

    availability_checkbox1="//input[@type='checkbox']"













