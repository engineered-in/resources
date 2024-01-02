GitLab
======

`GitLab <https://gitlab.com/>`_ is an instance of 
`GitLab (DevSecOps platform) <https://about.gitlab.com/>`_ for streamlining
and management of Software Development.

Learn more about GitLab
-----------------------

- `GitLab Tutorials <https://gitlab.com/help/tutorials/index.md>`_

- `GitLab Courses <https://about.gitlab.com/learn/>`_

Signin to GitLab
----------------

GitLab is available for use by anyone with a valid email id.

- Visit `https://gitlab.com/users/sign_in <https://gitlab.com/users/sign_in>`_

- Click Sign in (blue button) after entering the Username and Password.

.. note:: 

   In case if you do not have an account, visit `Sign Up for free here<https://gitlab.com/users/sign_up>`_

   Click on the "Remember me" check box if you plan to use GitLab frequently.

Configuring GitLab
------------------

A one time configuration is required for the following:

- Updating your `Profile <https://gitlab.com/-/profile>`_ (Photo, Full name)

- Adding your `public SSH key <https://gitlab.com/-/profile/keys>`_ for 
  easy communication

- Storing your `public GPG key <https://gitlab.com/-/profile/gpg_keys>`_ 
  for Code Signing

- Optionally you can `change your username <https://gitlab.com/-/profile/account>`_ 
  to customize your personal project URLs

Update GitLab Profile
----------------------------

- Visit https://gitlab.com/-/profile after Signing in

- Upload your Avatar to help your colleagues to easily identify you.

- Update your Full Name to your Name (same as Git Configuration)

- Update your Email and Commit Email to your Email address (same as in Git Configuration)

- Scroll below and Click **Update profile settings** (blue button)

Add your SSH Public key to GitLab
---------------------------------

- Open Git-bash (or cmd if you have completed 
  `Environment Setup <https://engineered-in.pages.gitlab.com/resources/environment.html#user-environment-variable>`_)

- Paste the below code into Git-bash (use **Copy button** instead of manual select)
  and press Enter key::

    cat ~/.ssh/id_ed25519.pub | clip

- The above command will **Automatically Copy** your SSH public key to **Clipboard**

- Open in a **new tab**, https://gitlab.com/-/profile/keys (Signin if required)

- Place the cursor inside the Key input field and press ``Ctrl + V`` to paste your 
  SSH public key

- Click on ``Add Key`` blue button to associate your SSH public key with GitLab

Add your GPG Public key to GitLab
---------------------------------

- Open Git-bash (or cmd if you have completed 
  `Environment Setup <https://engineered-in.pages.gitlab.com/resources/environment.html#user-environment-variable>`_)

- Paste the below code into Git-bash (use **Copy button** instead of manual select)
  and press Enter key::

    v=$(gpg --list-secret-keys --keyid-format LONG | awk '/sec/ {print $2}' | awk -F/ '{print $2}')
    gpg --armor --export $v | clip

- The above command will **Automatically Copy** your GPG public key to **Clipboard**

- Open in a **new tab**, https://gitlab.com/-/profile/gpg_keys (Signin if required)

- Place the cursor inside the Key input field and press ``Ctrl + V`` to paste your GPG public key

- Click on ``Add Key`` blue button to associate your GPG public key with GitLab

