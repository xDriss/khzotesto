from selenium import webdriver

# Replace PATH_TO_CHROMEDRIVER with the path to your ChromeDriver executable
driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)

# Replace URL with the URL of the webpage you want to open
driver.get("https://yip.su/Winners")

# Print the title of the webpage
print(driver.title)

# Close the browser window
driver.quit()
