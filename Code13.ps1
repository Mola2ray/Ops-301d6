#!/usr/bin/env python3
# Script: Ops301d6 Challenge-12
# Author: Lamin Touray
# Purpose: In your Windows Server, access Powershell ISE.
# Write a Powershell script that adds the below person to AD.
# Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.
# Test your script. Verify in ADAC that the user was created with the correct attributes. If anything is missing, delete the user in ADAC and re-attempt from Powershell ISE.



# Import the Active Directory module
Import-Module ActiveDirectory

# Define user properties
$givenName = "Franz"
$surname = "Ferdinand"
$displayName = "$givenName $surname"
$department = "TPS Department"
$title = "TPS Reporting Lead"
$company = "GlobeX USA"
$office = "Springfield, OR"
$mail = "ferdi@GlobeXpower.com"
$SamAccountName = "FFerdinand"
$UserPrincipalName = "FFerdinand@GlobeXpower.com"

# Create the user in the desired OU (change the OU path as needed)
$OUPath = "OU=Users,OU=GlobeX USA,DC=Corp,DC=globexpower,DC=com"
New-ADUser -Name $displayName -GivenName $givenName -Surname $surname `
    -DisplayName $displayName -Department $department -Title $title -Company $company `
    -Office $office -EmailAddress $mail -SamAccountName $SamAccountName `
    -UserPrincipalName $UserPrincipalName -AccountPassword (Read-Host -AsSecureString "Enter password") `
    -Enabled $true -Path $OUPath

# Verify the user is created and has the correct attributes
Get-ADUser -Identity $SamAccountName -Properties * | Format-List -Property Name, GivenName, Surname, DisplayName, Department, Title, Company, Office, EmailAddress
