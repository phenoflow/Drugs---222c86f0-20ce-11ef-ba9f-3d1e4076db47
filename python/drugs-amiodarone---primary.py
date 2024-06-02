# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"56034","system":"readv2"},{"code":"17119","system":"readv2"},{"code":"53658","system":"readv2"},{"code":"35517","system":"readv2"},{"code":"33119","system":"readv2"},{"code":"41551","system":"readv2"},{"code":"32553","system":"readv2"},{"code":"58033","system":"readv2"},{"code":"46938","system":"readv2"},{"code":"763","system":"readv2"},{"code":"32164","system":"readv2"},{"code":"188","system":"readv2"},{"code":"53666","system":"readv2"},{"code":"41530","system":"readv2"},{"code":"34751","system":"readv2"},{"code":"29456","system":"readv2"},{"code":"50241","system":"readv2"},{"code":"55845","system":"readv2"},{"code":"49376","system":"readv2"},{"code":"12322","system":"readv2"},{"code":"31209","system":"readv2"},{"code":"34515","system":"readv2"},{"code":"8832","system":"readv2"},{"code":"27161","system":"readv2"},{"code":"34851","system":"readv2"},{"code":"27193","system":"readv2"},{"code":"54224","system":"readv2"},{"code":"54608","system":"readv2"},{"code":"7445","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-amiodarone---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-amiodarone---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-amiodarone---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
