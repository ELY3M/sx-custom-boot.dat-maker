Thank you for CTCaer for this code.  
I grabbed this code from his gist at https://gist.github.com/CTCaer/13c02c05daec9e674ba00ce5ac35f5be


due to more people switching to atmosphere from SXOS and wanting to keep using their sxos pro dongle to boot up atmosphere.  

I did some research and found CTCaer's code.  it is best situation is to create boot.dat to boot up atmosphere.  
just need to put boot.dat on root of your sd card. just replace old sx boot.dat with this one.  

to make your own boot.dat  
you need python 3 installed on your computer.  
in cmd line, just run python build_boot.dat.py fusee-primary.bin

have to make new boot.dat everytime atmosphere get new release with new fusee-primary.bin


ELY M.  



