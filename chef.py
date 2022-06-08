import boto3

chefClient = boto3.client('opsworkscm')
response = chefClient.create_server(
        AssociatePublicIpAddress=True,
        DisableAutomatedBackup=False,
        Engine="ChefAutomate",
        EngineModel="Single",
        EngineVersion="12",
        EngineAttributes=[
            {
                "Name": "UI_SUBNET_AZ",
                "Value": "us-east-1d"
            },
        ],
        BackupRetentionCount=10,
        ServerName="sampleBoto3",
        InstanceProfileArn="arn:aws:iam::<accountID>:instance-profile/aws-opsworks-cm-ec2-role",
        InstanceType="m5.large",
        KeyPair="yourKeyPair",
        PreferredMaintenanceWindow="Mon:22:00",
        PreferredBackupWindow="06:00",
        ServiceRoleArn="arn:aws:iam::<accountID>:role/service-role/aws-opsworks-cm-service-role",
        SubnetIds=[
            "YourSubnetId",
        ]
    )
