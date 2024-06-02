# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"34707","system":"readv2"},{"code":"56136","system":"readv2"},{"code":"51751","system":"readv2"},{"code":"53195","system":"readv2"},{"code":"55006","system":"readv2"},{"code":"3350","system":"readv2"},{"code":"39427","system":"readv2"},{"code":"44903","system":"readv2"},{"code":"38508","system":"readv2"},{"code":"60102","system":"readv2"},{"code":"1550","system":"readv2"},{"code":"41137","system":"readv2"},{"code":"38939","system":"readv2"},{"code":"6711","system":"readv2"},{"code":"2822","system":"readv2"},{"code":"36634","system":"readv2"},{"code":"39550","system":"readv2"},{"code":"49923","system":"readv2"},{"code":"2082","system":"readv2"},{"code":"60332","system":"readv2"},{"code":"44472","system":"readv2"},{"code":"39279","system":"readv2"},{"code":"3733","system":"readv2"},{"code":"16609","system":"readv2"},{"code":"39930","system":"readv2"},{"code":"8885","system":"readv2"},{"code":"584","system":"readv2"},{"code":"40395","system":"readv2"},{"code":"3107","system":"readv2"},{"code":"39276","system":"readv2"},{"code":"3731","system":"readv2"},{"code":"35755","system":"readv2"},{"code":"56076","system":"readv2"},{"code":"39039","system":"readv2"},{"code":"39452","system":"readv2"},{"code":"33106","system":"readv2"},{"code":"3845","system":"readv2"},{"code":"42038","system":"readv2"},{"code":"35747","system":"readv2"},{"code":"38949","system":"readv2"},{"code":"53524","system":"readv2"},{"code":"53197","system":"readv2"},{"code":"43178","system":"readv2"},{"code":"3734","system":"readv2"},{"code":"7011","system":"readv2"},{"code":"44718","system":"readv2"},{"code":"37584","system":"readv2"},{"code":"43648","system":"readv2"},{"code":"45344","system":"readv2"},{"code":"34120","system":"readv2"},{"code":"43387","system":"readv2"},{"code":"30081","system":"readv2"},{"code":"45419","system":"readv2"},{"code":"11075","system":"readv2"},{"code":"7064","system":"readv2"},{"code":"34883","system":"readv2"},{"code":"9759","system":"readv2"},{"code":"24153","system":"readv2"},{"code":"34414","system":"readv2"},{"code":"6305","system":"readv2"},{"code":"45106","system":"readv2"},{"code":"33058","system":"readv2"},{"code":"43742","system":"readv2"},{"code":"34632","system":"readv2"},{"code":"4502","system":"readv2"},{"code":"40070","system":"readv2"},{"code":"34178","system":"readv2"},{"code":"35024","system":"readv2"},{"code":"20004","system":"readv2"},{"code":"17152","system":"readv2"},{"code":"53211","system":"readv2"},{"code":"5848","system":"readv2"},{"code":"36633","system":"readv2"},{"code":"37306","system":"readv2"},{"code":"34626","system":"readv2"},{"code":"40400","system":"readv2"},{"code":"36318","system":"readv2"},{"code":"4195","system":"readv2"},{"code":"37611","system":"readv2"},{"code":"4495","system":"readv2"},{"code":"34150","system":"readv2"},{"code":"46774","system":"readv2"},{"code":"35471","system":"readv2"},{"code":"6560","system":"readv2"},{"code":"34151","system":"readv2"},{"code":"9281","system":"readv2"},{"code":"38507","system":"readv2"},{"code":"42090","system":"readv2"},{"code":"53501","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('drugs-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["drugs-semisodium---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["drugs-semisodium---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["drugs-semisodium---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
