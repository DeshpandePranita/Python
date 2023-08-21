#r= "\\\\cw01.contiwan.com\\root\\Loc\\ulm2\\didt6448\\Recordings\\01_nightly\\mfc521_bsigs\\temp_Ravi\\ABA500_Najmus\\LCA\\BSIG\\2022.09.30 06.55.0100_LCA_Warning_LH_LCA_W4_Vego20.0kph_Vtgt30.0.testrun.bsig"
#filename = r.split("\\")[-1].replace(".bsig", "").split("LCA")[-1]
#filename = r.split("\\")[-1][26:].replace(".bsig", "")
r="\\lufs009x.li.de.conti.de\prj\SYS\LU\205\E26\0B4\6A4\764\EFA\70E\4A5\DAE\AAE\0F3\4A6\7EC\464\9B7\FAF\740\C74\2C0\2022.11.01_at_00.10.26_radar-mi_593.rrec"
    
  
#time_stamp = r.split("\\")[-1].split("_r")[0]
time_stamp = "20"+ r[89:]
new=time_stamp[:23]
print(new)


# a_string = "2022.09.30 06.55.010_LCA_nonWarning_LH_LCA_W4_Vego20.0kph_Vtgt30.0.testrun"
# reduced_string = a_string[26:]
# print(reduced_string)