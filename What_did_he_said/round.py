from rsa import rsa
from Crypto.Util.number import *
#from gmpy2 import *
import binascii
from random import *
enc = 15507598298834817042463704681892573844935925207353671096676527782423920390858333417805014479686241766827314370902570869063203100704151010294869728739155779685640415815492312661653450808873691693721178331336833872996692091804443257630828512131569609704473214724551132715672202671586891813211353984388741035474991608860773895778988812691240069777435969326282770350038882767450912160134013566175657336041694882842590560100668789803775001750959648059363722039014522592751510672658328196379883088392541680852726136345115484827400366869810045573176782889745710174383221427352027041590910694360773085666697865554456816396551
p1 = 14606124773267989759790608461455191496412830491696356154942727371283685352374696106605522295947073718389291445222948819019827919548861779448943538887273671755720708995173224464135442610773913398114765000584117906488005860577777765761976598659759965848699728860137999472734199231263583504465555230926206555745572068651194660027408008664437845821585312159573051601404228506302601502000674242923654458940017954149007122396560597908895703129094329414813271877228441216708678152764783888299324278380566426363579192681667090193538271960774609959694372731502799584057204257039655016058403786035676376493785696595207371994520
q1 = 14606124773267989759790608461455191496412830491696356154942727371283685352374696106605522295947073718389291445222948819019827919548861779448943538887273671755720708995173224464135442610773913398114765000584117906488005860577777765761976598659759965848699728860137999472734199231263583504465555230926206555745568763680874120108583912617489933976894172558366109559645634758298286470207143481537561897150407972412540709976696855267154744423609260252738825337344339874487812781362826063927023814123654794249583090654283919689841700775405866650720124813397785666726161029434903581762204459888078943696756054152989895680616

t = (p1 - q1) * 2

a = 1
b = t - 1
c = 2 - p1 * 2
def sqrt(x):
	l = 0
	r = x
	while (l<=r):
		g = (l+r) / 2
		t = g * g
		if ( t ==x):
			return g
		if  (t < x):
			l = g+1
		if (t>x):
			r = g-1
	return -1

#delta = b * b - 4 * a * c
#p = (-b + sqrt(delta)) / 2 / a
#q = p + t
#e = (1<<16) + 1
#t = rsa(p,q,e,enc)
#res = binascii.unhexlify(hex(t)[2:-1])
#print(res)
s = 'WIN 💎'
print(s)
m = [ bytes_to_long(['WIN 💎', 'LOSE 💩'][bool(i)].encode() + randrange(256 ** 200 - 1).to_bytes(200, 'big')) for i in range(3) ]
m = [(['WIN 💎', 'LOSE 💩'][bool(i)].encode() + randrange(256 ** 200 - 1).to_bytes(200, 'big')) for i in range(3)] 

print(m)