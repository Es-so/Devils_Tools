import urllib2
 
list=[".backup",".bck",".old",".save",".bak",".sav","~",".copy",".old",".orig",".tmp",".txt",".back",".bkp",".bac",".tar",".gz",".tar.gz",".zip",".rar"]
 
hote = sys.argv[1] #url

fichier = sys.argv[2] #file name ec: index

ext = sys.argv[3] #.php .html ...
 
for item in list:
 
   try:
        url = hote + "" + fichier + "" + ext + item
        result = urllib2.urlopen(url)
        print url + " Code : "+str(result.getcode())
 
   except urllib2.HTTPError as e:
            print url+" Code :  " + str(e)