# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"11237","system":"readv2"},{"code":"59058","system":"readv2"},{"code":"61630","system":"readv2"},{"code":"57670","system":"readv2"},{"code":"795","system":"readv2"},{"code":"9823","system":"readv2"},{"code":"12821","system":"readv2"},{"code":"5830","system":"readv2"},{"code":"13890","system":"readv2"},{"code":"55649","system":"readv2"},{"code":"53779","system":"readv2"},{"code":"60156","system":"readv2"},{"code":"51839","system":"readv2"},{"code":"44719","system":"readv2"},{"code":"46572","system":"readv2"},{"code":"61198","system":"readv2"},{"code":"61770","system":"readv2"},{"code":"59051","system":"readv2"},{"code":"7108","system":"readv2"},{"code":"16262","system":"readv2"},{"code":"7073","system":"readv2"},{"code":"54245","system":"readv2"},{"code":"53780","system":"readv2"},{"code":"52751","system":"readv2"},{"code":"13608","system":"readv2"},{"code":"5874","system":"readv2"},{"code":"60878","system":"readv2"},{"code":"58137","system":"readv2"},{"code":"58019","system":"readv2"},{"code":"18077","system":"readv2"},{"code":"6820","system":"readv2"},{"code":"15851","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-topiramate---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-topiramate---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-topiramate---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
