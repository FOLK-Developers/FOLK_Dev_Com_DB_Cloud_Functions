
arr=('createLinkedProfile'
'addContributions'
'addEducationData'
'addLoginInfo'	
'addProfessionalDetails'
'addProjects'
'addSkills'
'addActivity'
'addDocuments' 
'addMeeting'
'addNotifications'
'addRewards'
'addFollowUps'
'addFollowUpDetails'
'linkedProfileExists'
'createProfile'
'verifyLinkedProfile'
'sendMergeRequest'
'updatePrimaryInfo'
'updatePrePrimaryInfo'
'updateSecondaryInfo'
'updateTertiaryInfo'
'mergeAccounts'
'updateTaskStatus'
'addTasks'
'updateLinkedProfileVerificationStatus' )

for i in ${arr[*]}
do
	if [[ ! -d $i ]]
	then
    	cp -r cloud-function-template/ $i
	fi
	

done
