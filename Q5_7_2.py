members = [
        ['0001' , 'Male' , 'Yamada' , 'Tarou' , '25' , 'Tokyo'],
        ['0002' , 'Male' , 'Satou' , 'Takeshi' , '27' , 'Kanagawa'],
        ['0003' , 'Female' , 'Tanaka' , 'Yuko' , '25', 'Saitama'],
        ['0004' , 'Male' , 'Suzuki' , 'Ichirou' , '35' , 'Hokkaido']
        ]

member_dict = {}

for member in members:
    member_id = member[0]
    member_info = member[1:]
    member_dict[member_id] = member_info
print(member_dict)
