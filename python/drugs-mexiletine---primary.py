# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"12280","system":"readv2"},{"code":"25969","system":"readv2"},{"code":"10400","system":"readv2"},{"code":"11960","system":"readv2"},{"code":"50517","system":"readv2"},{"code":"40910","system":"readv2"},{"code":"608","system":"readv2"},{"code":"15459","system":"readv2"},{"code":"55769","system":"readv2"},{"code":"32351","system":"readv2"},{"code":"55553","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-mexiletine---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-mexiletine---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-mexiletine---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
