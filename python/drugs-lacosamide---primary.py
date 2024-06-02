# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"39356","system":"readv2"},{"code":"40372","system":"readv2"},{"code":"40658","system":"readv2"},{"code":"39615","system":"readv2"},{"code":"38789","system":"readv2"},{"code":"49084","system":"readv2"},{"code":"41162","system":"readv2"},{"code":"39952","system":"readv2"},{"code":"40291","system":"readv2"},{"code":"39259","system":"readv2"},{"code":"39126","system":"readv2"},{"code":"39385","system":"readv2"},{"code":"52473","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-lacosamide---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-lacosamide---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-lacosamide---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
