superfishy
==========

Archive of software, links and other data involved in the Superfish / Komodia incident

warning and password
====================

You don't want to install any of the software here if you are not doing this
for security research. All provided downloads contain dangerous software, if
you use them you will endanger the security of your system. To make sure
nobody accidently installs it they are packed in password-protected zip
files. The password for all files is

 iknowwhatimdoing

background / links
==================

Test if you are affected (currently only Superfish):
* https://filippo.io/Badfish/
* https://www.canibesuperphished.com/

My own news coverage in german media:

* [Golem.de / Adware: Lenovo-Laptops durch Superfish-Adware angreifbar](http://www.golem.de/news/adware-lenovo-laptops-durch-superfish-adware-angreifbar-1502-112460.html)
* [Golem.de / Komodia-Filter: Superfish-Affäre weitet sich aus](http://www.golem.de/news/komodia-filter-superfish-affaere-weitet-sich-aus-1502-112502.html)
* [Zeit Online / Superfish: Lenovo steckt gefährliche Adware in seine Laptops](http://www.zeit.de/digital/datenschutz/2015-02/superfish-lenovo-adware-hebelt-https-aus)

Some english news articles:

* [Arstechnica / Lenovo PCs ship with man-in-the-middle adware that breaks HTTPS connections ](http://arstechnica.com/security/2015/02/lenovo-pcs-ship-with-man-in-the-middle-adware-that-breaks-https-connections/)
* [Wired / Lenovo’s Response to Its Dangerous Adware Is Astonishingly Clueless](http://www.wired.com/2015/02/lenovo-superfish/)

Background / sources:

* [Extracting the SuperFish certificate](http://blog.erratasec.com/2015/02/extracting-superfish-certificate.html)
* [It's not just superfish that's the problem](https://gist.github.com/Wack0/17c56b77a90073be81d3)
* [Mirror of Komodia webpage including various software pieces](https://github.com/cryptostorm/komodia)

what?
=====

Lenovo delivered Laptops with a preinstalled Adware called Superfish in 2014.
Superfish created a severe security hole in all affected devices. Later it
turned out that several other Internet filtering products were affected by the
same issue.

The software installs a root certificate into the browser which allows
Man-in-the-Middle-attacks.

I am collecting all the software, the extracted certificates and private keys
to make sure they stay available.

Please send pull requests, mail me interesting items or upload them
[here](https://briefkasten.hboeck.de).

Hanno Böck, https://hboeck.de/
