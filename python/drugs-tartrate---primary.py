# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"9454","system":"readv2"},{"code":"18616","system":"readv2"},{"code":"2065","system":"readv2"},{"code":"979","system":"readv2"},{"code":"15369","system":"readv2"},{"code":"1069","system":"readv2"},{"code":"49754","system":"readv2"},{"code":"8152","system":"readv2"},{"code":"24963","system":"readv2"},{"code":"34830","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-tartrate---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-tartrate---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-tartrate---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
