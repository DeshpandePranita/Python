#r="\\lufs009x.li.de.conti.de\prj\SYS\LU\205\E26\0B4\6A4\764\EFA\70E\4A5\DAE\AAE\0F3\4A6\7EC\464\9B7\FAF\740\C74\2C0\2022.11.01_at_00.10.26_radar-mi_593.rrec"
r=["//lufs003x.li.de.conti.de/prj/SYS/LU/834/BCE/089/438/F99/E61/253/FC7/6E2/E69/C1E/489/92C/BE3/5EC/543/CF5/1C2/510/2022.10.12_at_15.01.52_radar-mi_5019.rrec",
  "\\lufs009x.li.de.conti.de\prj\SYS\LU\0C1\51D\496\98B\FCB\C45\4AC\695\85B\3C4\095\A45\BC5\FDD\CFF\DB5\2AA\25B\CD0\2022.11.01_at_02.06.17_radar-mi_593.rrec",
  "\\lufs009x.li.de.conti.de\prj\SYS\LU\205\E26\0B4\6A4\764\EFA\70E\4A5\DAE\AAE\0F3\4A6\7EC\464\9B7\FAF\740\C74\2C0\2022.11.01_at_00.10.26_radar-mi_593.rrec"
  ]  
# time_stamp ="20"+r[89:]
# new=time_stamp[:23]
# print(time_stamp)

for time_stamp in r:
    time_stamp =time_stamp[89:]
    new=time_stamp[:23]
    print(new)