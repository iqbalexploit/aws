import boto3

session = boto3.Session(profile_name='infra',region_name='ap-southeast-1')
route53 = session.client('route53')
domain = []

def get_zones():
    zones = []
    for zone in route53.list_hosted_zones()['HostedZones']:
        zones.append(zone['Id'])
    return zones

def list_record(zones):
    for HOST_ID in zones:
        paginator = route53.get_paginator('list_resource_record_sets')
        RECORDS = paginator.paginate(HostedZoneId=HOST_ID)
        for r in RECORDS:
            for rec in r.get("ResourceRecordSets"):
                if rec.get("Name") not in domain:
                    domain.append(rec["Name"])
    return domain

if __name__ == "__main__":
    zones = get_zones()
    print("\n".join(list_record(zones)))
