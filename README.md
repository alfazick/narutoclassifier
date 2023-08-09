
---

## Deployment Instructions for TensorFlow Model on Azure

### **Prerequisites: Setting Up Git**

#### 1. Suppress Local Git
- Use the command provided by Azure (it will start with `git config --global --add ...`).

#### 2. Set Up Git Credentials
```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

#### 3. Clone the Repository
Replace `repotoclone` with the URL of the repository you wish to clone.
```bash
git clone https://github.com/alfazick/classifiermodel computervision
```

#### 4. Navigate to Cloned Repository
Replace `path_to_cloned_repository` with the appropriate path.
```bash
cd path_to_cloned_repository
```

#### 5. Reinitialize Git
```bash
rm -rf .git
git init
```

#### 6. Add, Commit, and Push to New Repository
```bash
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/alfazick/narutoclassifier.git
git branch -M main
git push -u origin main
```

---

### **Block #1: App Service Plan and App Service**

#### **1. Create an App Service Plan**
- Sign in to the Azure portal.
- Click on "Create a resource".
- Search for "App Service Plan" and select it.
- Click "Create" and fill in the required details:
  - **Subscription**: Your Azure subscription.
  - **Resource Group**: Choose an existing one or create a new one.
  - **Name**: A unique name for the App Service Plan.
  - **Operating System**: Linux.
  - **Region**: Closest to you or your customers.
  - **Pricing tier**: Based on your needs (Free or Shared for testing).
- Click "Review + create" and then "Create".

#### **2. Create an App Service**
- In the Azure portal, click on "Create a resource".
- Search for "Web App" and select it.
- Click "Create" and fill in the required details:
  - **Subscription**: Your Azure subscription.
  - **Resource Group**: As used for the App Service Plan.
  - **Name**: Unique name for the web app.
  - **Publish**: Code.
  - **Runtime stack**: Python version (e.g., 3.8).
  - **Operating System**: Linux.
  - **Region**: Same as App Service Plan.
  - **App Service Plan**: The one you created earlier.
- Click "Review + create" and then "Create".

---

### **Block #2: Deploy to Azure App Service**

#### 1. Deploy GitHub Repository to Azure App Service
- Go to your Web App in the Azure portal.
- Click on "Deployment Center".
- For "Source Control", select "GitHub".
- Connect to GitHub and choose your repository and branch.
- For "Build Provider", select "App Service Build Service".
- Click "Continue", review, then click "Finish".

Once deployed, access your Flask app via the URL shown in the "Overview" tab of your Web App.

---

After following these steps, your code should be deployed to Azure App Service, and you should be able to 
access your Flask app at the URL shown in the "Overview" tab of your Web App. 
This will look something like https://<your-app-name>.azurewebsites.net.

# classifiermodel
# computervision
# computervision
# computervision
# computervision
# computervision
