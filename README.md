# ansible-tower-samples
Ansible Tower Playbook Samples

## Using this Repo


### Step 1 - Install Ansible Automation Platform
Presumably you have already completed this step before arriving here, however the installation of Automation Controller needs to be completed before you continue.

### Step 2 - Edit the Demo Project
1. Login to your Automation Controller as the `admin` user and click on **Project** in the left hand sidebar.
2. Click on the **Demo Project** and edit it. Change the **Source Control URL** to `https://github.com/RedHatGov/ansible-tower-samples` and save the project.
3. Make sure the project sync completes.

### Step 3 - Create the Controller Credential
1. Navigate to the **Credentials** section in the left hand sidebar.
2. Click the **Add** button at the top of the screen and use the following values to create your credential.

|      |                       |
|------|-----------------------|
| Name | 'Controller Credential' |
| Organization | 'Default' |
| Credential Type | 'Red Hat Ansible Automation Platform' |
| Red Hat Ansible Automation Platform | *URL of Controller UI* |
| Username | 'admin' |
| Password | *admin password* |

### Step 4 - Edit the Demo Job Template
1. Navigate to the **Templates** section in the left hand sidebar.
2. Click on the **Demo Job Template** and edit it. Change the **playbook** field to `product_demos.yml`. If you do not see this option, go back to step 2 and ensure your project is configured and synced properly.
3. Click the magnifying glass on the **Credentials** field, change the dropdown in the top right to `Red Hat Ansible Automation Platform` and select `Controller Credential` from the list.
4. Save the job template and click **Launch**

#### Customization: If you have customized the product-demos project, now would be the time to update the source URL for your project.

### Step 5 - Launch the SETUP Job
1. Navigate back to the **Templates** section in the left hand sidebar.
2. Locate the **SETUP** job template and click the rocket ship icon on the right to launch the job.
3. Select the use case from the dropdown that you are interested in and continue.


#### You have now completed the setup. Refer to [ansible/product-demos](https://github.com/ansible/product-demos) for further documentation.

---

[Privacy statement](https://www.redhat.com/en/about/privacy-policy) | [Terms of use](https://www.redhat.com/en/about/terms-use) | [Security disclosure](https://www.ansible.com/security?hsLang=en-us) | [All policies and guidelines](https://www.redhat.com/en/about/all-policies-guidelines)
