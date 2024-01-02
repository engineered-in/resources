Configure Git
=============

Git Bash is the ideal command line interface for configuring Git.

You can also use command prompt or powershell if you have already 
`configured user environment variable <https://engineered-in.gitlab.io/resources/environment.html#user-environment-variable>`_

Git needs to be configured for the following

- User name
- Email address
- SSH key
- GPG key
- Auto Signing
- Default Branch Name

Launching Git Bash
++++++++++++++++++

Git Bash could be launched clicking:

- Start --> Git Bash


Configuring User Name
+++++++++++++++++++++

Use the below command in Git Bash to configure your name
(use **Copy button** instead of manual select)::

    git config --global user.name "<YOUR_NAME_HERE>"

.. note:: Replace <YOUR_NAME_HERE> with your Name

Configuring Email Address
+++++++++++++++++++++++++

Use the below command in Git Bash to configure your email
(use **Copy button** instead of manual select)::

    git config --global user.email "<YOUR_EMAIL_HERE>"

.. note:: Replace <YOUR_EMAIL_HERE> with your Email Address

SSH Key Generation
++++++++++++++++++
SSH protocol enables us to connect and authenticate to remote servers (GitLab)
and services without supplying username and personal access token at each visit.

Use the below command in Git Bash to generate SSH public and private key pair
(use **Copy button** instead of manual select)::

    ssh-keygen -t ed25519 -C "<YOUR_EMAIL_HERE>"

- Hit enter to use the default file name.  

- Provide a PassPhrase to encrypt your private. It is essential to remember your PassPhrase.  

- Confirm your PassPhrase by retyping it in the confirmation prompt
    
.. note:: 
   Leave the PassPhrase **blank** and click OK, if you do not wish to setup passphrase 
   (recommended for ease of use).

GPG Key Generation
++++++++++++++++++

`GPG <https://en.wikipedia.org/wiki/GNU_Privacy_Guard>`_ signing is a
cryptographic method to verify that commits are actually from
a trusted source.

Use the below command in Git Bash to generate GPG public and private key pair
(use **Copy button** instead of manual select)::

    gpg --full-gen-key

- Type 1 and press Enter to select RSA type key
- Type 4096 and press Enter to set a RSA keysize of 4096 bits
- Type 0 and press Enter to specify the key does not expire
- Type y at the confirmation prompt to confirm the key does not expire
- In the Real name prompt, enter your **name**
- In the Email address prompt, enter your **email address**
- In the Comment prompt, enter your comments (if any) and press Enter
- In the change prompt, Type "O" for selecting (O)kay and press Enter key
- In the Pinentry prompt enter a PassPhrase of atleast 8 characters containing at least 1 digit or special character and click OK
- In the re-enter passphrase prompt, re-enter your PassPhrase for confirmation and click OK

.. note:: Leave the PassPhrase blank if you do not wish to setup passphrase (recommended for ease of use)

Configuring Auto Signing
++++++++++++++++++++++++

Automatic Signing of commits with GPG key is the certificate of origin of the
source code.

Use the below command in Git Bash to enable Automatic Signing of commits using
your GPG key (use **Copy button** instead of manual select)::

    v=$(gpg --list-secret-keys --keyid-format LONG | awk '/sec/ {print $2}' | awk -F/ '{print $2}')
    git config --global user.signingkey $v
    git config --global gpg.program "C:/Users/$(whoami)/AppData/Local/Programs/Git/usr/bin/gpg.exe"
    git config --global commit.gpgSign true

Configuring Default Branch Name
+++++++++++++++++++++++++++++++

Use the below command in Git Bash to change the default branch name from
**master** to **main** (use **Copy button** instead of manual select)::

    git config --global init.defaultBranch main
