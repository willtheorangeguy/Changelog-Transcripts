[0.00 --> 16.54]  let's do it it's go time welcome to go time your source for wide-ranging discussions from all
[16.54 --> 23.06]  around the go community check us out on the web at gotime.fm there you'll find our recommended
[23.06 --> 28.92]  episodes the most popular ones and a request form so you can let us know what you want to hear about
[28.92 --> 33.74]  on the pod thanks to our partners for helping us bring you go time each and every week
[33.74 --> 39.70]  fasi.com fly to io and typesense.org okay here we go
[39.70 --> 51.72]  so we are here for episode number two on the topic of what is new in the crypto library
[51.72 --> 57.36]  and we have a really long list of things that we did not cover in part one and to help us do this
[57.36 --> 62.90]  better this time we also brought on board nicola who is joining filippo and roland and for everybody
[62.90 --> 67.86]  who did not listen the first episode why don't we do another round of introductions thank you for
[67.86 --> 76.48]  inviting me i'm i help filippo and roland in maintaining the crypto ssh since july and i'm
[76.48 --> 84.04]  filippo i've been doing maintenance on the go cryptography libraries since 2018 i was doing it
[84.04 --> 91.02]  at google with roland and katie ochman and damien neal and plenty of others until 2022 and i'm now
[91.02 --> 96.96]  doing it as a independent maintainer and i'm roland i'm one of the people on the go security team
[96.96 --> 106.12]  i've been around for yeah some amount of time three three or so years i think but i've been working on
[106.12 --> 112.38]  go as an i worked on go as an outside maintainer for a while and before that as an engineer at the
[112.38 --> 116.42]  let's encrypt project filippo roland did you meet nicola at latin class
[116.42 --> 124.68]  we're just talking in the before the beginning of the episode how you all learned latin at school
[124.68 --> 128.88]  in italy it's a it's a very common thing and we're talking about the fact that it's you know not that
[128.88 --> 135.12]  hard when the language is so similar roland might have had a harder time yeah i think that i think the
[135.12 --> 141.26]  only latin i remember is rather rude so i won't repeat any of it i mean that's the secret though
[141.26 --> 148.98]  everybody thinks of studying latin as this rarefied high discussions about the maximum systems of that
[148.98 --> 155.68]  no no seriously they were pretty crude yeah i know a lot of ways to insult romans but
[155.68 --> 165.12]  like what well the there was a comic book that i read that had the um the explanation for the acronym
[165.12 --> 175.12]  spqr is sono porci questi romani which means which you know uh that that pinks these latins
[175.12 --> 178.18]  so these romans i am recording from rome
[178.18 --> 183.08]  what did you have for lunch
[183.08 --> 190.10]  yeah i guess the the that word is familiar from pizza menus
[190.10 --> 199.14]  okay so a brief recap of what we didn't cover in the first episode of what is new in the
[199.14 --> 206.64]  crypto library for go is a cls 1.0 we talked about math big about
[206.64 --> 214.40]  crypto ecdh about shao 1 and md5 deprecation maybe about goat bugs about
[214.40 --> 221.94]  um some things that are planned for the future like a safer higher level apis and we briefly
[221.94 --> 229.30]  touched the crypto the ssh library that is under x to which we will go back later but now we want
[229.30 --> 236.24]  to talk about moving from pre-quantum to post-quantum and before we talk into that
[236.24 --> 241.70]  i want to say that i looked up how to say the present the middle something what is between
[241.70 --> 248.32]  pre and post and this is nunc so let's talk about nunc quantum and then post-quantum
[248.32 --> 255.12]  um i think everybody is starting to not like post-quantum but by the way in the in the community
[255.12 --> 260.10]  and they're starting to look for the new suggestion new words so i'm going to suggest that
[260.10 --> 266.82]  what is the meaning of quantum in latin how does that translate i have chad gpt here so that's not
[266.82 --> 270.94]  a fair question it's okay if you don't say you don't know i think it's a small unit right it's a
[270.94 --> 277.74]  single singular unit often you will talk about a quantum of something a quantum of data but i don't
[277.74 --> 283.04]  think that has any relation to the actual technology i think they just pulled this because i think it
[283.04 --> 289.48]  comes from quantum mechanics right the mechanics of fundamental particles and using those you can
[289.48 --> 295.42]  make computers that do things a little weird and they're super positions and i'm not qualified to
[295.42 --> 303.18]  explain any of this in fact i think it is all beyond all of our pay grades so i mean yeah that's the fun
[303.18 --> 308.78]  thing about uh post-quantum cryptography is that we don't do it on quantum computers the point is that
[308.78 --> 313.56]  quantum computers might come and we don't understand much about them but when they come
[313.56 --> 318.88]  they might break all of the stuff we are currently doing with cryptography and so we have to implement
[318.88 --> 325.84]  some other cryptography that people who do know how quantum computers work think uh are not going to
[325.84 --> 331.76]  get broken by quantum computers and then there's you know bickering about what being broken means and
[331.76 --> 341.00]  how to measure that and we don't talk about that debate yeah it's all very theoretical but it's kind
[341.00 --> 347.32]  of if someone does come up with a good way to break the current cryptographic primitives we're in real
[347.32 --> 354.48]  trouble so just on the off chance there has been all of this work of trying to figure out new algorithms
[354.48 --> 361.70]  which will not be susceptible to this very specific things that quantum computers are good at
[361.70 --> 367.98]  doing which leads us to the new nist drafts i don't know if you want to talk a bit about that
[367.98 --> 375.70]  sure so nist has run a competition where a bunch of independent scientific groups submitted various
[375.70 --> 383.78]  proposals and then they run a bunch of selection rounds and they finally selected a key exchange
[383.78 --> 390.86]  two signatures two the nist is a national institute of standard and technology yes which does things
[390.86 --> 399.10]  like um specifying cryptography like aes and uh shot but also you can buy from this uh sample of the
[399.10 --> 403.96]  reference peanut butter it might be the most expensive peanut butter in the world and it's exactly the
[403.96 --> 410.28]  reference peanut butter that you can use to configure your machinery that needs to process peanut butter
[410.28 --> 417.36]  or something i don't know nist is a weird institution uh cool but yes so they just like they have the
[417.36 --> 423.24]  peanut butter person they also have the cryptography people and the cryptography people select algorithms
[423.24 --> 431.26]  and they then make uh standards which are the fips the federal information processing standards
[431.26 --> 439.24]  uh which define how the government the u.s government processes things that's a fairly u.s centric process
[439.24 --> 445.26]  but the community kind of came together around this one i think a bunch of the submissions are not even from
[445.26 --> 451.62]  u.s scientists and european governments already signaled that they like the things that nist selected
[451.62 --> 458.54]  and that they're going to implement the same things so good news is no brain pool this time no german only
[458.54 --> 466.02]  curves so no i'm sure i don't know uh there will be the chinese and the russian versions for uh but uh you know
[466.02 --> 474.30]  hopefully we'll standardize mostly on these a few algorithms and they do the things that our old algorithms did
[474.30 --> 481.04]  they just do it with a lot more bytes unfortunately but also hopefully they're not broken by quantum
[481.04 --> 487.62]  computers so pros and cons they're all significantly slower as well right you know i was about to say
[487.62 --> 495.64]  that but they're not like kyber no kyber is faster than x2519 i was under the impression that that they
[495.64 --> 503.14]  were slower but i don't actually think that's the case well that's good yeah i my very unoptimized
[503.14 --> 509.90]  kyber implementation is as fast as our very optimized x25519 implementation and the slowest
[509.90 --> 516.92]  thing in the in kyber is the hash because they selected shatree which is very slow for no good
[516.92 --> 523.58]  reason they made it do a lot of rounds of things and anyway that's that that's a whole story but yeah
[523.58 --> 529.28]  turns out it's at least the key exchange is actually faster i was kind of surprised by that however
[529.28 --> 535.60]  then uh with x25519 you had so these are key exchanges so they're the things where you have
[535.60 --> 541.88]  a connection like a tls connection or ssh connection and you want to establish keys to encrypt it and you
[541.88 --> 546.40]  want to make sure that somebody who's watching and trying to intercept it cannot figure out the key
[546.40 --> 552.28]  people might have heard about diffie hellman that's a key exchange so we don't get to do diffie hellman
[552.28 --> 559.12]  in a post-quantum world uh we thought we were going to and then somebody went and completely broke
[559.12 --> 565.84]  the algorithm that was closest to diffie hellman super singular isogenies we we loved them while
[565.84 --> 573.28]  they lasted and we have these things called chems which are key exchange mechanisms which do a thing
[573.28 --> 580.92]  that's close enough so just like we used to use curve25519 to exchange keys and diffie hellman we can now
[580.92 --> 586.66]  use things like kyber which is now called ml chem because we can't have nice things the two things
[586.66 --> 593.80]  selected were called kyber and dilithium such good names and then they went and called them ml chem
[593.80 --> 602.34]  and ml dsa which one do you want to be saying yeah the star wars star trek names are much better right
[602.34 --> 609.86]  i'm not even a star wars and star trek fan and i wanted those names nicola do you do you agree with
[609.86 --> 616.74]  the sentiment did you also prefer these names yes and uh philippo what uh what do you think would
[616.74 --> 626.02]  be the performance impact of all of using the sha3 on common operation for example an ssh connection
[626.02 --> 633.14]  do you think it's not easy because we did some benchmark in the past and we we chose to not
[633.14 --> 643.94]  include uh sha512 at base down because they are too slow so with the sha3 what is the situation
[643.94 --> 651.26]  so i think the sha512 algorithms were also using a larger diffie hellman group and that was the very
[651.26 --> 659.54]  slow one so the hashes i think are not generally speaking the slow parts uh here except sha3 is slow
[659.54 --> 665.94]  so it happens to dominate the key exchange uh step but to give some order of magnitude i think that
[665.94 --> 673.86]  both x25519 and kyber using sha3 take i don't know i want to say okay i don't actually remember
[673.86 --> 679.14]  actual number but let's say they take 10 finite field diffie hellman with a very large group is going
[679.14 --> 685.62]  to take like a thousand that's the the the gap uh there like there's a hundredfold difference there
[685.62 --> 693.86]  i think ssh is going to be fine actually i think that open ssh already has um post quantum key
[693.86 --> 700.42]  exchange except that they selected theirs before nist selected one so yeah it's not the one we're
[700.42 --> 705.22]  implementing in the costander library so we hopefully they they you know they introduce
[705.22 --> 711.78]  a kyber based one soonish it seems highly likely that they will just because that's what everyone else
[711.78 --> 717.78]  is implementing at this point yeah and also because you know fips 140 you want to be fips 140
[717.78 --> 723.78]  compliant yeah exactly fips 140 is one of the standards and it's the one that say it was written
[723.78 --> 731.78]  for hardware you know the the things you put in a rack uh and it said they have to be sealed and it has to
[731.78 --> 737.94]  have a led that does a certain thing and when you turn it on with a key it needs to check its circuits
[737.94 --> 742.50]  to make sure that it's not broken and then they went and said yeah that's the standard you should
[742.50 --> 749.62]  follow for um cryptographic libraries as well now does anybody can anybody think how do you implement
[749.62 --> 757.30]  the led in a library you just flip a bit you have a magic bit yeah no actually seriously there's a bit
[757.30 --> 762.90]  in memory nothing can read it but you set it to one when the led should be on and you set it to zero
[762.90 --> 768.10]  when the led should be off and then when the uh auditor comes and asks where is the led you go
[768.10 --> 773.38]  at that address in memory and the auditor says good good you are compliant and agreed to global
[773.38 --> 781.30]  mario one yes yes i'm not kidding i'm not kidding it's the worst it's absolutely the worst anyway
[781.30 --> 786.42]  and that's and that's how much i'll say about long life to global library to global mario one
[786.42 --> 795.54]  exactly exactly anyway um fist 140 is a standard you have to comply with if you want to sell your
[795.54 --> 800.50]  things to companies that want to sell their things to companies that want to sell their things to the
[800.50 --> 807.14]  us government that's a lot of people unfortunately yeah it turns out that's most people well the link
[807.14 --> 811.78]  is in the show notes in case anybody needs to meet that standard is not familiar with it just yet i i
[811.78 --> 819.86]  wouldn't wish that on anyone exactly anyway going back to uh to kyber um the very annoying thing about
[819.86 --> 826.82]  these new algorithms is that they are the keys and the signatures and the exchanged things are so much
[826.82 --> 833.30]  bigger and that's a problem like with kyber you're looking at sending on the wire something like
[833.30 --> 840.50]  1300 bytes you're sending a kilobyte of data where with x25519 you are sending 32 bytes
[840.50 --> 847.86]  like we used to be like ah what's another uh diffie hellman uh element just stick a few in there
[847.86 --> 852.74]  actually let's make a ratchet where we go from element to element to element to element and let's
[852.74 --> 858.26]  change keys all the time and let's stick keys inside of keys out of keys and now we can't do that we
[858.26 --> 865.78]  we we get one if we're lucky like a packet might fit one key now that's not great yeah this is going to be
[865.78 --> 870.02]  an even bigger problem for signature algorithms right like we've been trying to figure out
[870.66 --> 877.38]  what the pq the post-quantum approach to certificate signing is and there's still you know we've
[877.38 --> 881.94]  there's been the last decade or so has been spent trying to figure out how to make certificates
[881.94 --> 886.02]  smaller and smaller and smaller in terms of the number of bytes that need to be sent over the wire
[886.58 --> 892.98]  and now we're going you know all of the post-quantum signature algorithms result in keys that are
[893.62 --> 898.90]  keys and signatures which are orders of magnitude larger so all of those gains that were
[898.90 --> 904.02]  you know hard fork for over the last decade have just been completely lost and we now have
[904.02 --> 909.14]  certificates that are you know i think there were some suggestions where they would be megabytes in
[909.14 --> 915.94]  size yeah i don't think we're doing that no i i hope not uh but still like with things like
[915.94 --> 922.18]  certificate transparency we currently have what um three signatures in a certificate right there's the
[922.18 --> 926.98]  signature over the whole certificate and then there's the signature from two certificate
[926.98 --> 933.94]  transparency logs which are these public registries that sign a statement that says i will i promise i
[933.94 --> 939.54]  promise i promise i will publish this certificate so that anybody who wants to know what certificates
[939.54 --> 945.30]  exist can come look at the registry which is very useful because for example you can sign up for a service
[945.30 --> 952.26]  like search spotter which you know search spotter is not sponsoring this but uh we very much love the
[952.26 --> 957.54]  operator because he does great work for the community and you can sign up for that and say oh i would like
[957.54 --> 963.86]  to get an email every time a new certificate is issued anywhere in the world a certificate that would be trusted
[963.86 --> 972.42]  by browsers for filippo.io so that if you know my server gets hacked or a ca makes a mistake
[972.42 --> 979.30]  um and they issue uh not that ca's make mistakes to be clear yeah unheard of i don't know what you're
[979.30 --> 988.66]  talking about yeah no madness i i i i take it back but uh you can get an email and that's nice but that
[988.66 --> 996.10]  means there are you know these statements went in the certificate and since signatures were 32 64 bytes
[996.10 --> 1002.26]  we were like yeah just stick the 64 bytes in there what's the problem now signatures
[1002.26 --> 1009.14]  are going to be a thousand uh thousand bytes a kilobyte like uh or two and we must stop in
[1009.14 --> 1011.30]  improving speed of internet connection
[1015.62 --> 1017.14]  that's why berlin does letters with
[1019.22 --> 1024.10]  for security reasons you will never get like any password reset from your bank other than a
[1024.10 --> 1029.30]  lower credit card other than a paper letter because no not enough internet for those things
[1029.30 --> 1035.70]  not a joke this is real how you have to reset your credit card number oh boy cypher suite ordering
[1036.74 --> 1043.62]  tell us about that okay so this is a thing i'm like a big fan of and a lot of people hated me for it i
[1043.62 --> 1050.66]  think uh but this is about making things less configurable because that's that's been a theme right
[1050.66 --> 1057.30]  we talked about in the last episode we like to put fewer options in and take care of things for for
[1057.30 --> 1063.30]  the user for those who didn't listen one line recap what are we what are we not configuring oh because
[1063.30 --> 1068.34]  we should do our job and you know know things about cryptography so that uh go developers don't have to
[1068.34 --> 1074.82]  do our job and know things about cryptography so for example things that are right now configurable but
[1074.82 --> 1080.26]  you you're well you know this is making them less before you could decide whether um you wanted
[1080.26 --> 1093.38]  uh you liked better tls rsa with as 256 gcm shot 384 or tls ecdhe ecdsa with 3dcbc shot now that sounds
[1093.38 --> 1099.46]  like our next twitter poll better than unpopular opinion poll can you i will ask you to write that
[1099.46 --> 1105.14]  down in the show notes in the end and we will make that a poll just for the just for the trolling yes
[1105.14 --> 1112.10]  and these these cypher suites are so obscure and and you know which one is better than which is so
[1112.10 --> 1119.30]  obscure the basically you know one of and every guide of how to set up apache or any server one of
[1119.30 --> 1125.22]  the steps would be you go to the mozilla website and you there's a tool that they had which would
[1125.22 --> 1131.14]  generate the correct list of cypher suites in the correct order to put into your web server and
[1131.14 --> 1136.58]  everyone just went and used the list that they suggested because there's no reason for any normal
[1136.58 --> 1142.98]  person to either know about this or care but then sometimes something happens and then you have to
[1142.98 --> 1148.74]  change your mind because the list order has changed because i don't know something turned out to be more
[1148.74 --> 1154.66]  broken or less broken and so you have to update your conflicts because your opinion has changed right
[1154.66 --> 1160.34]  because you had an opinion on those and by the way i picked those two uh as a trick people might have
[1160.34 --> 1165.54]  heard three deaths and thought oh but that's from the 80s i know the answer it's the one without the
[1165.54 --> 1172.34]  thing from the 80s and you would be wrong the one with with the algorithm from the 80s is actually
[1172.34 --> 1176.74]  stronger than the other one why that's gonna be the second poll when you heard that did you think of
[1176.74 --> 1184.10]  the think of the 80s i don't know is three does from the 80s is three does uh something like that
[1184.10 --> 1191.70]  first published 1981 and yep still doing better than the other thing because the other thing doesn't
[1191.70 --> 1197.78]  have uh forward security which i you know could spend a bunch of time talking about or i could talk
[1197.78 --> 1204.02]  about how we took away the ability to choose the ordering uh for all of this stuff and now we decide
[1204.02 --> 1211.30]  which ones are better so for ts 1.3 i actually somehow succeeded at pulling off um not putting a config
[1211.30 --> 1218.18]  option in at all you can't turn them on off change the order there's just not a config option and
[1218.18 --> 1224.10]  people are kind of upset at me about that one that's that's much better much better in my opinion
[1224.10 --> 1230.74]  because for example when i i write a nap but my in the open source of my routine
[1231.62 --> 1239.46]  since uh the algorithm is very obscure even for me i simply exposed them to end users and all
[1239.46 --> 1248.82]  do and while in with tls 1.3 it's much more simple they are not configurable and default are chosen by
[1250.42 --> 1256.42]  by people who know what they do so it's much better i prefer i prefer this approach
[1257.06 --> 1266.10]  a lot and some people were upset but you know still i think i pulled it off for tls 1.0 to 1.2 it would
[1266.10 --> 1271.38]  break too many programs to say oh actually you know we'll pick which ones to enable and that's it
[1271.38 --> 1277.46]  however one thing we could take away was the order in which they're selected which might sound silly
[1277.46 --> 1282.82]  like what what does the order matter well the order matters because if you're selecting like five good
[1282.82 --> 1287.78]  ciphers uh and one bad one i have to worry that there are applications out there that might have put
[1287.78 --> 1294.34]  the bad one at the top of the preference list so any client that uh has support for that uh for
[1294.34 --> 1300.26]  backwards compatibility reasons will end up negotiating a very bad algorithm when it could use a good one
[1300.98 --> 1305.86]  and so we would have to have these conversations where we'd be like well do we remove it because
[1305.86 --> 1312.10]  it's kind of broken it's not so broken that you wouldn't want it ever but you would definitely not
[1312.10 --> 1317.54]  want it if you had any other option but we have no way to make sure if somebody is using it because
[1317.54 --> 1322.82]  they don't realize they put just they just sorted them alphabetically maybe or something and and so
[1322.82 --> 1327.46]  we would have all these difficult conversations around backwards compatibility because if you listen to
[1327.46 --> 1333.94]  the last episode you know that the hard part of our job is neither quantum computers nor algorithms but
[1333.94 --> 1340.58]  it is backwards compatibility uh uh so we have all these very difficult conversations
[1340.58 --> 1348.34]  and then instead now with this change the order is picked entirely by us you can select them but
[1348.34 --> 1355.62]  we know that if you selected anything else that's even slightly better than this it will be used before
[1355.62 --> 1360.26]  we fall back to that and that's important because for example there are some old android phones
[1360.98 --> 1368.98]  that will never get upgraded because they were sold before android knew how to force carriers to update phones
[1368.98 --> 1376.50]  uh and uh you want your server to still serve connections from them but you want to make sure that just
[1376.50 --> 1382.66]  because you serve connections to them you're not going to be less secure when somebody else connects right
[1383.22 --> 1388.10]  so with the fact that we handle the ordering we can make sure that we will only go to the terrible
[1388.10 --> 1395.86]  algorithm that uh android the only android phones that is the only thing android phones support only if it's the
[1395.86 --> 1401.38]  last resort so yes i get excited about the small things about backwards compatibility what can i say
[1401.38 --> 1408.82]  it also it also lets us do some fancy tricks about how we decide what the ordering is right we have we have
[1408.82 --> 1416.34]  special logic in to determine you know if your computer has hardware support for certain algorithms we can
[1416.34 --> 1422.58]  increase the priority of those algorithms in order to make you get better throughput on your connections
[1422.58 --> 1428.34]  whereas if if the user picked them it would be a bit awkward saying well actually we've decided that
[1429.54 --> 1433.94]  we are going to reorder your specific ordering decisions because we know better but now we can
[1433.94 --> 1441.62]  just say we always know better yes what ron is hinting at is that there's this uh cipher which is called aes
[1442.18 --> 1449.14]  which was selected by nist etc etc and back then cryptography was more about a thing you did in hardware with
[1449.14 --> 1456.90]  special chips and you know with machines with keys and leds and uh fips 140 certifications and all that
[1456.90 --> 1462.02]  and so they designed an algorithm that's uh pretty easy to implement in silicon where you have you know
[1462.02 --> 1468.50]  you can draw out a blueprint and make the paths go through here and you go like yeah you know electricity
[1468.50 --> 1473.86]  goes through here at the same time and that's how you make things go fast and simultaneously and then the
[1473.86 --> 1481.38]  world changed and now we implement most stuff in software and implementing aes in software turns out
[1481.38 --> 1488.82]  to be very difficult because you have to read something from a table but if you if the attacker can tell
[1488.82 --> 1497.14]  what slot in a table you read it from they can just divinate the key because as swift on security says
[1497.14 --> 1504.82]  uh cryptography is math that care what pen you use to write it and so the result is that what does
[1504.82 --> 1511.30]  that mean uh well you know normally if you just write the math it's correct regardless of what you
[1511.30 --> 1516.10]  used right and i think uh what swift on security was getting at is that in cryptography instead you
[1516.10 --> 1520.98]  have to worry sometimes about side channels and stuff like that where you might have written your program
[1520.98 --> 1529.22]  correctly but since you took more time or less time or maybe you accessed the cache or the memory in a
[1529.22 --> 1536.18]  certain order exactly now somebody who's observing what you did even if the result was right like you
[1536.18 --> 1541.94]  didn't throw an error you didn't do a panic your tests all passed there's no way to test this but
[1541.94 --> 1547.86]  since you did it in this way you touched memory over here and i know that if you touch memory over here
[1547.86 --> 1553.06]  it means that the first bit of your key is one and then if you touched memory over here it means that
[1553.06 --> 1557.94]  your the second bit of your key is zero and then you keep going like that and then you just extract
[1557.94 --> 1566.26]  the key and that's bad it's generally frowned upon so the result is that as is a major pain to implement
[1566.26 --> 1571.38]  in software we kind of figured it out now with a technique called bit slicing which is basically
[1571.38 --> 1578.42]  re-implementing a hardware cpu but in software it's madness it's like i don't know if you've ever seen
[1578.42 --> 1586.58]  those videos of computers inside minecraft you know people building computers by using redstone and
[1586.58 --> 1594.42]  and switches and and torches and so on right so the bit slicing it's sort of like that which really makes
[1594.42 --> 1600.10]  me think we should get all these kids uh who build this stuff in minecraft and ask them if they have nice
[1600.10 --> 1605.46]  ideas for fighting side channel attacks in cryptography algorithms but that's actually not a
[1605.46 --> 1612.74]  bad idea mindhive right right also lots of uh people who start by reverse engineering uh games or by
[1612.74 --> 1619.70]  doing game mods them turn out to be security engineers there's a pipeline right it turns out
[1619.70 --> 1625.94]  break breaking the controls that uh developers put on their video games is really good training to
[1625.94 --> 1632.66]  break controls people put on secure systems turns out and turns out if you can maintain software that's
[1632.66 --> 1638.74]  based on an undocumented api that you reverse engineer every time a new version of a game comes out
[1638.74 --> 1644.10]  and that is willing to break you without even looking back you actually can be pretty good at writing
[1644.10 --> 1649.38]  regular software too checks out and working on a version of java that's about 18 years old
[1649.38 --> 1656.50]  uh and patching the jvm so that you can you know make your shader go a little faster so that you can make
[1657.54 --> 1664.82]  your ore sparkle or something jvm is my key word to move to quick yes actually
[1667.62 --> 1673.86]  what is quick and what does it have to do with the go library i don't actually know what quick stands for
[1673.86 --> 1681.70]  it's an acronym but it is so there was a at some point people decided that the http
[1681.70 --> 1687.94]  quick udp internet connections not just any udp yeah that makes sense that is a nice trolling yeah
[1687.94 --> 1693.70]  it originates from there was a protocol written internally at google that was used as kind of a
[1693.70 --> 1700.74]  prototype for what became quick that was originally called speedy s-p-d-y oh man that takes me back
[1700.74 --> 1707.86]  a lot of people who worked on that protocol worked on quick and i think the the idea was it you know
[1707.86 --> 1715.70]  quick is open source speedy or you know um ietf speedy yeah ietf speedy exactly by the way i i googled
[1715.70 --> 1721.62]  quick uh to see what the uh acronym and the first result is an italian page that says the quick
[1721.62 --> 1723.70]  protocol what it is and how to turn it off
[1723.70 --> 1736.50]  yeah like mood a reasonable a reasonable approach but it's essentially the next version of it's
[1736.50 --> 1741.46]  often referred to as the next version of http i think it's really a more yeah i think how they
[1741.46 --> 1748.58]  ended up splitting it off is that quick is the underlying transport protocol of http 3 yeah and http
[1748.58 --> 1757.46]  3 is both the new http semantics and and a protocol and the quick uh underneath it right something like
[1757.46 --> 1763.70]  that yeah so it's a cake there's http on top and that's http 3 and then you have quick where you would
[1763.70 --> 1771.54]  have tcp a quick is basically a way to implement tcp because tcp is implemented by your kernel and people
[1771.54 --> 1777.14]  have opinions about that implementation and then the kernel you know doesn't change it and so they go like
[1777.14 --> 1785.22]  fine i'll reimplement uh tcp with black no no uh with uh with all of my features and encryption
[1785.22 --> 1791.30]  and implement it over udp which instead is just packets right right because the the internet uh
[1791.30 --> 1796.74]  ossified and now there are two internet protocols and those are udp and tcp and you cannot have another
[1796.74 --> 1802.90]  one if you want another one you build it on top of udp like we use to do in in the back of days no yeah
[1802.90 --> 1808.98]  it's like if you look at the old osi layer diagrams of of the internet i think the whole
[1808.98 --> 1815.38]  point of quick is that over time like yeah the layers became incredibly complicated and necessarily
[1815.38 --> 1820.42]  needed to be interconnected so quick just takes like three separate layers and squishes them all
[1820.42 --> 1825.62]  into a single layer the main useful thing to know about it is that it's encrypted by default i don't
[1825.62 --> 1830.74]  think you can have unencrypted quick i don't think you can yeah no uh yeah unlike http 2 which was supposed
[1830.74 --> 1834.90]  to also be encrypted by default but some people came along and figured out a way to make it
[1835.70 --> 1844.90]  unencrypted http 2 yeah quick is you know it's so ingrained that it is the perfect protocol i think
[1844.90 --> 1850.50]  this is called the end-to-end principle the concept that all the layers move to the end points because
[1850.50 --> 1856.34]  the end points have the most context about what you need to do so the tcp stack has to work for every
[1856.34 --> 1862.18]  application while the browser knows it wants to load a web page so it can make different choices
[1862.18 --> 1867.94]  one of my favorite facts about quick is that it encrypts the headers not for privacy but because
[1867.94 --> 1874.74]  they really don't want uh the network engineers to mess with them so they just went like you know what
[1874.74 --> 1879.78]  you know what we're gonna encrypt the hell out of the headers so that you don't get to have an
[1879.78 --> 1885.30]  opinion if that's not the end-to-end principle i does this in any way affect crawlers crawlers are
[1885.30 --> 1891.54]  probably not smart enough to use quick okay so like this hiding the headers is not not relevant
[1891.54 --> 1897.22]  oh no these are the headers that say things like how big the packets should be and how fast you should
[1897.22 --> 1903.38]  uh okay okay different completely ones yeah these are the things that like um flow control and all this
[1903.38 --> 1908.74]  stuff about tcp that i honestly don't understand what what it really messes with is middle boxes yes
[1908.74 --> 1916.58]  right these like hardware devices that awful companies sell well i i won't say awful the
[1916.58 --> 1924.74]  the companies you said it you're on the record google er ronan shoemaker said but they you know interfere
[1924.74 --> 1933.14]  with network traffic to do things often you know things you would rather they not do and that break
[1933.14 --> 1938.98]  everything uh and and quick very nicely makes it basically impossible for them to do that anyway
[1938.98 --> 1944.42]  bringing it back to go what are we doing with quick and go so what um at the bottom of this cake of
[1944.42 --> 1951.06]  layers there's uh tls uh because they very correctly did not reinvent cryptography and they just said so we
[1951.06 --> 1958.10]  need some keys so what we're gonna do is run a tls handshake over quick and then we'll take keys out of
[1958.10 --> 1962.90]  uh tls and then we'll reinvent cryptography and do our own cryptography for transport but
[1962.90 --> 1968.10]  they had good enough reasons for that and the hard part is the handshake once you've negotiated keys
[1968.10 --> 1975.06]  the rest yeah you know then you need to make a little wrapper packets and put a bow on it but it's easy
[1975.06 --> 1980.90]  enough so they run a tls handshake over quick and then they extract some stuff now the problem is that
[1980.90 --> 1990.10]  our crypto tls package was made to run tls handshakes over tls and over tcp and we didn't want to have a
[1990.10 --> 1995.54]  fork in the quick implementation because that's bad but we also didn't want to add a million options to
[1995.54 --> 2004.58]  the um to crypto tls so damien neal and martin from um protocol labs uh martin seaman who's the
[2005.46 --> 2010.82]  maintainer of quick go which was the external implementation that did have a fork of crypto tls
[2010.82 --> 2019.30]  which we did break regularly every release which did cause a lot of breakage in the ecosystem which
[2019.30 --> 2025.22]  was why homebrew couldn't update to their go version for a month every time a new go version came out
[2025.78 --> 2033.78]  so all of that was not great uh so now there's a bunch of crypto tls apis that are a very small
[2034.74 --> 2042.02]  hook into the crypto tls library and that don't make me terrified of the complexity that was added
[2042.02 --> 2048.90]  and they allow quick implementations both the one that is it coming in the standard library it's not
[2048.90 --> 2057.38]  it's in 122 i don't think you can really use it but oh wait the quick implementation or the tls apis
[2057.38 --> 2064.26]  oh the tls apis yeah the tls apis has been there for since 21 i think yeah yeah cool and also quick
[2064.26 --> 2070.98]  go now uses the uh the new tls api in go 121 so now you can upgrade quick go and it will not break
[2070.98 --> 2077.22]  and and well you can upgrade go and it will not break break quick go and we're all very happy about
[2077.22 --> 2084.18]  that now with that and the fact that brad's package that breaks no moving gc doesn't break anymore i think
[2084.18 --> 2089.86]  we can go back to upgrading go and nothing should explode fingers crossed because our job is about
[2090.10 --> 2097.62]  backwards compatibility correct and and now forwards compatibility as well oh boy
[2100.02 --> 2104.90]  just finding the right link because apparently when you search for the show notes if you want to add the
[2104.90 --> 2112.18]  the link to the go implementation or like the the official implementation it's not in the first five
[2112.18 --> 2118.50]  results but i i bet i will find this i find some i found something on a package tls i think uh yeah a
[2118.50 --> 2124.66]  lot of the quick stuff is currently hidden away in an internal package so that you can't mess with it too
[2124.66 --> 2131.38]  much uh because it is still it's still almost definitely a work in progress so what's the what would be a good
[2131.38 --> 2137.22]  practice for this i'm not sure i i think we have an issue somewhere that discusses the the roadmap for
[2137.22 --> 2143.86]  quick but it's a very good question i could find a link for you and send it to you later so just just
[2143.86 --> 2151.46]  not use this yet just know about this or what would be yeah i think it's yeah quick is unlikely to be
[2151.46 --> 2157.62]  something that most people directly interact with it is something that should mostly be completely
[2157.62 --> 2163.78]  transparent to users you will you know make an http request and our underlying implementation will use
[2163.78 --> 2168.98]  quick if the other endpoint also supports it for the network engineers i'll leave the link there
[2170.58 --> 2176.66]  yeah i suspect most people will just be happy that it's happening and won't have to do anything fingers
[2176.66 --> 2190.10]  crossed this is a changelog news break one year after chat gpt brought a seismic shift in the entire
[2190.10 --> 2196.50]  landscape of ai a group of researchers set out to test claims that its open source rivals had achieved
[2196.50 --> 2203.38]  parity or even better on certain tasks in the linked paper they provide an exhaustive overview of this
[2203.38 --> 2210.50]  success surveying all tasks where an open source llm has claimed to be on par or better than chat gpt
[2210.50 --> 2217.62]  their conclusion quote in this survey we deliver a systematical review on high-performing open source llms
[2217.62 --> 2225.46]  that surpass or catch up with chat gpt in various task domains in addition we provide insights analysis and
[2225.46 --> 2232.98]  potential issues of open source llms we believe that this survey sheds light on promising directions of open source
[2232.98 --> 2238.50]  llms and will serve to inspire further research and development helping to close the gap with their
[2238.50 --> 2245.38]  paying counterparts end quote it's becoming increasingly clear to me that the data models powering future ai
[2245.38 --> 2251.06]  rollouts will be commoditized and democratized thanks to the competitive nature and hard work of both
[2251.06 --> 2259.54]  academia and industry what a relief you just heard one of our five top stories from monday's changelog news
[2259.54 --> 2264.98]  subscribe to the podcast to get all of the week's top stories and pop your email address in at
[2264.98 --> 2271.86]  changelog.com slash news to also receive our free companion email with even more developer news worth your
[2271.86 --> 2284.66]  attention once again that's changelog.com slash news all right let's talk then about the new path builder
[2284.66 --> 2291.86]  and the parser we can do this very quickly roland all yours these are these are old old x5 and not old
[2291.86 --> 2300.66]  but these are were major x509 changes that we made for tls the authentication layer of tls uses x509
[2300.66 --> 2312.58]  certificates and x509 uses a encoding language called the distinguished encoding rules which we we had a you
[2312.58 --> 2320.02]  you know adam langley who wrote a lot of the original crypto libraries wrote a parser for that uses
[2320.02 --> 2329.38]  reflection which is you know something we offer in go but is i don't say terrible but it's quite slow
[2330.66 --> 2336.10]  it's a very interesting language feature but it's kind of painful and he wrote it using this because
[2336.10 --> 2341.54]  he said to me the reason he wrote it using reflection was he had never used the language that had reflection
[2341.54 --> 2347.22]  before and he thought it would be an interesting thing to use reflection for i did not know this
[2347.22 --> 2353.62]  unfortunately this turned out to have been a bad decision and was very slow in part because it did a
[2353.62 --> 2359.86]  lot of alloc you know it had to allocate a lot of small bits of memory all over the place so i think i
[2359.86 --> 2370.02]  think it was in 120 or 119 we changed i wrote a new we have this new library called cryptobyte which is a
[2370.02 --> 2375.62]  a it's a way to write explicit parsers where you know you know the structure of your data and you can
[2375.62 --> 2382.42]  very efficiently parse it so instead of using reflection and needing to support you know every
[2382.42 --> 2389.14]  single type in the go type system we could write an explicit parser that says like i know exactly
[2389.14 --> 2395.22]  what the format of this certificate should be and i can just pass it in one fell swoop yeah for comparison
[2395.22 --> 2401.94]  including asn1 you would make a struct with a int and a byte slice and with some tags which is like
[2401.94 --> 2408.18]  json does instead with cryptobyte there's a function that says hey read an integer from the string great
[2408.18 --> 2413.70]  now uh read this other thing from the string great now read another value from the string and you just
[2413.70 --> 2418.34]  call those one after the other and you put code in the middle if you need to check something and it's
[2418.90 --> 2424.66]  much more explicit little more boilerplate but this is go we like boilerplate yeah and because it knows
[2424.66 --> 2430.34]  exactly what it's doing it needs to allocate a lot less and it's a lot faster so this the top level
[2430.34 --> 2436.42]  takeaway here is that we managed to speed up certificate passing by something like 80 it got
[2436.42 --> 2442.10]  incredibly quick which took away a big amount of overhead from tls connections which was very nice
[2442.10 --> 2448.98]  and solved problems i had left behind like oh no we are parsing certificates in a hot path and we don't
[2448.98 --> 2454.34]  know what to do about that we'll have to add caches or do very smart things and then roland came along
[2454.34 --> 2459.78]  made it all faster and now it's not a problem anymore cheers well we still did some of those
[2459.78 --> 2467.54]  things anyway but that's another story uh but maybe we should move on to ssh i think you know x509 is my
[2467.54 --> 2474.74]  pet project but i think i am one of about 15 people in the world that finds it interesting so okay nicola
[2474.74 --> 2482.34]  what are you excited most about in the in the upcoming changes for ssh yes there are a lot of of change
[2482.34 --> 2491.30]  changes we added in in the last month for example we ssh is a suite of protocols allowing to connect
[2492.26 --> 2501.78]  our security of the network to to remote hosts for example to to login a typical example of use of ssh
[2501.78 --> 2510.10]  is to get the login shell to a remote server or to transfer the file so recently we added in
[2510.10 --> 2520.26]  and a new implementation to avoid a passive network of servers from detecting a keystroke because the
[2520.26 --> 2530.42]  idea is is simple because the client can just emulate keystroke at a fixed interval if there is no activity for
[2530.42 --> 2539.94]  example if you stop typing the client can send some packet so since ssh is a client server protocol there
[2539.94 --> 2550.58]  are already a lot of of message defined to exchange the data between client and server and the client may
[2550.58 --> 2558.74]  use one of the existing message to emulate keystroke this will be the the simplest thing unfortunately this
[2558.74 --> 2569.38]  does not work because the existing packet of existing message have two limitations the first one is is
[2569.38 --> 2581.78]  their size they are too big so a network of observer can detect if a data is a keystroke or not a keystroke another limitation
[2582.42 --> 2591.70]  is that there isn't a message allowing to send a sequence of bytes and returning the same sequence of bytes
[2591.70 --> 2602.02]  for this reason for this reason open ssh the leading ssh implementation added the protocol extension at the transport
[2602.02 --> 2611.14]  management you see a classical uh the classical ping you send uh some bytes and the the sender send back this
[2611.14 --> 2620.42]  uh this byte so uh we can we a client may use this ping message to emulate the keystroke
[2620.42 --> 2629.86]  obviously uh client cannot send can not send this ping message unconditionally there was there is the need to
[2629.86 --> 2636.02]  address this this feature because as usual our job is about backwards compatibility
[2638.74 --> 2645.46]  we cannot uh we cannot break things because people are very angry if they
[2645.46 --> 2655.06]  we we if we are broken so so we cannot do things like this and uh for this reason in the the the protocol
[2655.06 --> 2663.94]  the new this new extension is uh uh addressed i said using the standard uh extinfo message and the
[2663.94 --> 2673.86]  extension is called ping at open ssh.com with version zero soon after the this feature shipped in
[2673.86 --> 2684.42]  uh open ssh after a few days we uh we added it to to our crypto ssh library generally is we are not so
[2684.42 --> 2692.58]  fast so fast but that's something i'm i'm very proud of and you know for values of proud where i'm proud of
[2692.58 --> 2700.50]  the work other people are doing uh because uh the xcrypto ssh package didn't have a active maintainer i think for
[2700.50 --> 2708.34]  the past year uh year and a half couple years and so i think i think perhaps longer than that perhaps
[2708.34 --> 2714.74]  longer than that yeah and uh and so how it was maintained is uh was that i would just go and
[2714.74 --> 2721.54]  extinguish fires when they were like really really big and otherwise nothing was happening it was so far
[2721.54 --> 2729.78]  behind open ssh which as nicola was saying drives a lot of the progress of the protocol and instead this
[2729.78 --> 2736.58]  one i think we actually merged it we had the cl already before the uh open ssh release yes and merged
[2736.58 --> 2743.78]  it just a few days after it came out we started to go to work on this feature uh basically to get
[2743.78 --> 2752.50]  our open ssh team so the cn was ready before open ssh released this feature and was a merged
[2752.50 --> 2758.74]  just after the release of the rockets of the ssh base and the reason this is happening by the way is that
[2758.74 --> 2764.26]  nicola is uh is now uh working on maintaining that thanks also to all the funding from from my
[2764.26 --> 2770.10]  clients which sorry um i'm not going to say the whole names no i'm not this is not a sales pitch but
[2770.66 --> 2775.86]  yeah i'm i'm so happy we could get nicola to do that maintenance work of course i don't work alone on
[2775.86 --> 2784.10]  this filippo helped me a lot roland helped me uh russ other go team members uh helped me in the
[2784.10 --> 2792.26]  the process because there is a very formal approval process before shipping and fishing because we have
[2792.26 --> 2800.90]  to to to keep the required of compatibility because our job is about backwards compatibility sometimes
[2800.90 --> 2808.42]  we cannot be too too fast to ship a feature because we have to think about the impact on our user and
[2808.42 --> 2815.14]  if this feature uh introduce uh breaking change yeah before nicola was around one of the things that
[2815.14 --> 2822.98]  developed into a big fire uh was shatu support so basically ssh was the the protocol was hard coding
[2822.98 --> 2831.38]  sha1 in some places and sha1 is a hash that has a collision issue now you can make two things that
[2831.38 --> 2837.78]  hash to the same sha1 hash which might sound like a party trick it's actually very annoying because the
[2837.78 --> 2843.30]  security properties of some things rely on that not happening so we've been moving off sha1 for the
[2843.30 --> 2854.50]  past 20 years i think uh 25 by now and uh open ssh finally moved off and started turning off the the
[2854.50 --> 2860.90]  the sha1 things and guess who had not implemented sha2 yet well not sha2 sha2 in general we had sha2 for
[2860.90 --> 2867.70]  since the dawn of time uh but the did not implement the sha2 extensions to replace the sha1 in sssh
[2867.70 --> 2876.82]  or we use the ads of course and then at some point uh they i think it was uh github was about to
[2876.82 --> 2882.82]  turn off their sha1 support and they had these nice blog posts being like here's our roadmap
[2882.82 --> 2890.42]  if anybody's still not supporting sha2 they should probably do something about it and i i want to find
[2890.42 --> 2895.86]  the engineer who wrote those and ask if there was a you know between the lines looking at you go
[2895.86 --> 2904.74]  well it wasn't just github was it it was also open ssh that ended up removing open ssh had had
[2904.74 --> 2911.30]  turned it off like months earlier but all of the distros had turned it back on in their configs
[2911.94 --> 2918.66]  except fedora so we were actually already broken on fedora but turns out that being broken on fedora
[2918.66 --> 2924.18]  does not get people with the people with the pitchforks out but not being able to connect to github also
[2924.18 --> 2932.58]  arc linux on arc i was the first one who not i said this uh this brickage initially i didn't understand
[2932.58 --> 2939.38]  what what is happening i i thought but the test case the test case my test case on a continuous
[2939.38 --> 2944.66]  integration system works fine on my pc does that's not work anymore what's happening
[2944.66 --> 2952.26]  it was really funny and yeah also importantly the the version of open ssh bundled with mac os
[2952.82 --> 2961.94]  was updated to the yes in fact indeed philippo that this is a support as soon uh mac os because
[2962.74 --> 2969.30]  he was a blinker he was broken so yeah it turns out break the maintainer that that helps
[2969.30 --> 2977.06]  uh but yeah so you know i shipped initial support for that uh but then uh you know foreshadowing
[2977.06 --> 2981.14]  nicola you were the first one to notice the breakage but little did you know that it would become your
[2981.14 --> 2988.50]  job to then clean up because it was such a painful upgrade actually uh nicola want to tell us about it
[2988.50 --> 2997.38]  yes it was uh basically uh the first the first support was something workish because uh we we
[2997.38 --> 3005.54]  take it some time before people realized that there were there were uh another bridge so it was uh it
[3005.54 --> 3014.34]  was something to do in my defense um open ssh itself implemented this wrong for the first five versions
[3014.34 --> 3021.94]  this is this is the exactly the bridge i'm i'm thinking about because after the initial support we
[3021.94 --> 3030.98]  started to get the report because all the open ssh version doesn't work properly because their bug also
[3031.70 --> 3042.26]  gpg gpg agent some old version gpg agent stopped working and so we have a lot of of new issues basically
[3042.26 --> 3051.86]  our problem was that we have a senior interface that is we're unable to advertise
[3051.86 --> 3060.98]  the supported algorithm so we you can just assume that all algorithms are supported but this is not
[3060.98 --> 3068.58]  this is not applicable anymore so we need to introduce a new a new interface a multi-algorithm senior
[3068.58 --> 3076.66]  a multi-algorithm senior so uh address the supported algorithm so you can you know the the supported
[3076.66 --> 3083.78]  algorithm and you can choose the one to use for for singing this this is our way to fix the issue
[3083.78 --> 3090.50]  because we can with the multi with supporting the multi-algorithm senior allowing us to provide
[3090.50 --> 3097.46]  the happy to restrict and choose the client side center side and also certificate the singing algorithm
[3097.46 --> 3106.58]  because one of the biggest issue with open ssh other certificate that is a different standard from
[3106.58 --> 3116.58]  x509 certificate it's something different and this this introduced a lot of research with the with old open
[3116.58 --> 3125.70]  ssh version since a few days we merged at the last the latest fix so i think i hope we have no more
[3125.70 --> 3133.06]  regression on this area at least for a while don't say that don't say that don't say that i just check
[3133.06 --> 3139.46]  my mail to see if i get the help do not say that i mean we joke that our job christmas freeze is coming
[3140.74 --> 3147.06]  we joke that our job is backwards compatibility but the openness the ssh protocol has been at two point uh
[3147.06 --> 3153.70]  at two point something since 2006 i just checked so you know there's a reason they have so much
[3153.70 --> 3160.74]  complexity layering and layering and they did a better job than tls did at the time but some of the results
[3160.74 --> 3166.66]  are maddening because for example the the change nicola was talking about had to deal with the fact that
[3166.66 --> 3172.82]  there used to be just key types you know if you use a rsa key type you make rsa signature and that's it
[3172.82 --> 3177.78]  right if you use a ecdsa key you make a cdsa signature but then they went like well you might
[3177.78 --> 3186.10]  want to use a rsa key to make a signature that uses sha2 not sha1 and so we got key type algorithms and
[3186.10 --> 3192.98]  signature algorithms and those started being separate with a one-to-many mapping but then you know
[3192.98 --> 3198.10]  sometimes your that key is actually part of a certificate so are you negotiating the algorithm to
[3198.10 --> 3204.50]  say i support certificates or are you negotiating uh just the underlying key but when you make a
[3204.50 --> 3210.42]  signature it's not a special certificate signature it's just a signature so sometimes you refer to the
[3210.42 --> 3214.82]  key type sometimes you refer to the key type but also certificates sometimes you refer to the
[3215.38 --> 3220.18]  signature algorithm and sometimes you refer to the signal algorithm but also the certificate algorithms
[3220.18 --> 3222.98]  this is an evil i got mad the first time
[3222.98 --> 3231.94]  i might i wrote it at least two or three times before i started to understand something i don't
[3231.94 --> 3239.86]  i don't know if you remember why this period help help the case the house and i also remember that
[3239.86 --> 3245.30]  every time we go back and we change something similar we get on a call and we're like wait is this
[3245.30 --> 3252.42]  an underlying algorithm or is the key type wait no no this one can be a certificate right we absolutely need
[3252.42 --> 3260.10]  to do something to to fix this because it's really oh we have two choices the first one is
[3260.10 --> 3263.14]  don't don't change any order code never
[3266.42 --> 3274.74]  no more bug reports no more no more that sounds good to me done all right i think this this was quorum
[3274.74 --> 3282.42]  and uh majority for okay perfect we'll file a proposal that the whole libraries are now freeze
[3282.42 --> 3287.78]  frozen perfect so no back one no more make one compatibility
[3289.38 --> 3293.62]  oh actually perfect backwards compatibility we never change anything if you never implement anything
[3295.70 --> 3301.06]  throwback to kelsey hightower is no code yes that's the dream
[3301.06 --> 3310.34]  by the way um speaking of of changes this is a bit of a uh hopping topic but i i just saw an email
[3310.34 --> 3315.54]  uh arrive during the recording uh and you're doing something else filipo
[3316.50 --> 3318.50]  yes i cannot manage my attention
[3320.74 --> 3327.86]  but acl just got merged and now mathrand in go 122 is going to be cryptographically safe by default
[3327.86 --> 3334.02]  the the default uh random number generator is switching to cha cha eight so that if you by
[3334.02 --> 3339.86]  mistake use mathrand instead of cryptorand at least it will not explode in very pure technique
[3339.86 --> 3345.86]  ways it will not and for more details episode one we got a lot of information about that there
[3345.86 --> 3351.38]  exactly we talked about it but now the magic happened the merge happened exactly during the
[3351.38 --> 3354.66]  the episode sorry for the interruption but like i'm just so happy about this
[3354.66 --> 3360.66]  well that's that's great news shall we celebrate the end of the episode on this festive spirit
[3360.66 --> 3368.10]  saying uh in one i don't know in one feature no explanation what is your favorite uh change in ssh
[3368.66 --> 3374.66]  that is upcoming that we did not mention yet if we cover them all then we go to that popular opinion
[3374.66 --> 3382.66]  i think nicola probably has a list so we'll think about it well yes a feature i like i like a lot is
[3382.66 --> 3390.66]  the ability to to make we can now make every algorithm to configure more so for example there are many people that
[3390.66 --> 3400.02]  complain about fips we speak at the before we have to improve this we have to provide a fips mode also for
[3400.02 --> 3410.66]  uh for ssc for ssh but the fips uh can now be achieved because you can configure every algorithm you can also disable for example
[3410.66 --> 3418.66]  completely shao one even if for the quad compatibility we still use shao one by default for some for some
[3418.66 --> 3426.66]  for some algorithm but the the important thing is that you can you can configure all the algorithm as you want
[3426.66 --> 3436.66]  this is was important also for for my work as open source maintainer for my project i now can disable anything uh
[3436.66 --> 3443.14]  uh showing shao one repeated uh by default this is very important uh the project nicola is talking about
[3443.14 --> 3451.46]  is sftp go um yes i picked him out of sftp go maintainership and that's how i knew he could maintain
[3451.46 --> 3460.42]  expert ssh i got in touch with philippo with my project because i need some some features in openness in ssh
[3460.42 --> 3466.98]  library and i started to send some ssh and i got up and yoned by philippo
[3469.14 --> 3476.42]  he called me and he signed do you want to become the new antenna so it turns out if you get a bunch
[3476.42 --> 3484.74]  of bug reports you can make it that person's problem yes the next gpt is just saying thanks for your
[3484.74 --> 3491.94]  bug report please fix it oh by the way we are talking about how i think we started saying how
[3491.94 --> 3496.26]  not having configurability is good and we are closing with how we are happy that there's more
[3496.26 --> 3502.34]  configurability i want to call it out but there is an important difference in the first one that we like
[3502.34 --> 3507.62]  the defaults in the latter one the defaults were so bad that being able to configure them off is a
[3507.62 --> 3513.46]  step forward you know a v2 of the api can remove all of the configurability and leave only the good
[3513.46 --> 3519.22]  things behind but when you have so much bad stuff the fact that at least you can turn it off much big
[3519.86 --> 3529.62]  thumbs ups but another important difference and it is in ssh world there are more older device that
[3529.62 --> 3537.54]  never got up in a browser is all modern browsers are updated so you can remove all the algorithm
[3537.54 --> 3546.74]  more easily i frequently get reports of the clients unable to connect because they maybe use also
[3547.30 --> 3558.50]  something terrific algorithm for example ask for so there you are there are no more than one year ago i got
[3559.38 --> 3566.98]  people asking me to how they can enable ask for that is an algorithm from from at least
[3567.54 --> 3575.78]  another data 80s for sure 80s for sure yes yes all right i'll pick a very quick one one thing that
[3575.78 --> 3582.74]  i think might be waiting for my review so sorry about that but that's coming is much better tests that
[3582.74 --> 3590.98]  test xcrypto ssh against open ssh so that we don't have to wait until it breaks on my laptop or on
[3590.98 --> 3597.86]  on github to to figure out that it's not working with the latest open ssh nicole is building a whole
[3597.86 --> 3604.18]  harness that will run the ssh binary and like make recordings of the connection and make sure that
[3604.18 --> 3609.70]  it's always doing the thing that's expected and that's just great yeah i was going to say the exact
[3609.70 --> 3614.34]  same thing i think this is you know one of the greatest changes that this library is going to get
[3614.34 --> 3619.94]  because it will make our lives easier for the next you know next five years you can see how jaded
[3619.94 --> 3626.50]  ron and i have become where where we go oh yeah i mean i'm so excited about tests there's gonna be so
[3626.50 --> 3633.14]  many tests yes i mean i gave a whole go for a come uh talk and it was not about cryptography or post
[3633.14 --> 3637.22]  quantum or anything like that it was like want to see some really neat tests
[3637.22 --> 3646.90]  i also broke a test of windows there was a report on a windows test uh that is not only on windows 11
[3646.90 --> 3656.34]  it seems i cannot reproduce locally no i have um ashy the go maintainers uh no not i said it is uh this
[3656.34 --> 3665.70]  brigade so i have to investigate it there are some tests against ssh clear open ssh that does not does
[3665.70 --> 3672.66]  not work on windows 11 don't break the build hashy will find you but i think i think that this is
[3672.66 --> 3679.38]  uh this is not a bug in my code because it's related to the vision it's still your problem
[3681.06 --> 3688.50]  if you broke the problem i'm quite sure it's a problem if that if your commit is the one that
[3688.50 --> 3694.90]  broke the build your comment is the one that gets reverted no the build broken after my commit when
[3694.90 --> 3700.42]  after they updated the the the test in mind oh then it's definitely hashy's problem yes
[3702.34 --> 3710.26]  consensus so now let's move to an unpopular opinion
[3712.58 --> 3722.26]  i actually think she'd probably leave
[3724.90 --> 3732.42]  i'm i think i'm older here i'm very old more older than uh than all of you and so my unpopular
[3732.42 --> 3742.18]  opinion is using all the style keyboard instead instead only once the all the old style keyboard when you
[3742.18 --> 3750.50]  can hear the very very loudly when you when you do a keystroke for example
[3750.50 --> 3758.50]  is it good or bad for hacking hearing the keystroke very very good it's it's not uh good for your
[3758.50 --> 3765.14]  neighbors they exactly when when you have it to work that's what's unpopular about it
[3767.78 --> 3774.02]  yeah if you have any roommates so i like that we went immediately to roommates and we forgot the
[3774.02 --> 3779.86]  the existence of offices uh like i think all three of us have not worked in an office for years
[3780.98 --> 3783.86]  four four there you go
[3786.18 --> 3790.58]  yeah yeah my my cats get very annoyed at me but i type very loudly on my keyboard
[3792.66 --> 3795.30]  yeah if you interrupt their sleep i get that i'm on their side
[3795.30 --> 3804.42]  you should be considerate do you have an unpopular opinion oh i think i have a i have a
[3805.14 --> 3812.90]  contemporary unpopular opinion which is that as much as i i think ai is a real pain in terms of code
[3812.90 --> 3821.30]  generation i think it generates terrible code but i love it because i think it is creating job security
[3821.30 --> 3828.50]  for security engines and it will be for the considerable future cool cool we just held in
[3828.50 --> 3833.78]  berlin like two weeks ago and b-sides which is a security conference and we had two out of the nine
[3833.78 --> 3839.78]  talks about ai so cool filipo do you have an unpopular opinion i mean i'm tempted to counter your
[3839.78 --> 3845.30]  unpopular opinion with the unpopular opinion that i do use copilot in cryptography code but only to write
[3845.30 --> 3850.90]  error messages because i hate writing error messages but no no no so i think my unpopular opinion
[3850.90 --> 3856.58]  and i will probably get yelled at for this one but it's that that's your goal yes
[3859.14 --> 3864.74]  there's a reason open source maintainers don't get donations and i think the companies are not wrong
[3865.38 --> 3871.62]  asking for donations companies cannot do donations that's not a thing they know how to do that's not
[3871.62 --> 3877.46]  a thing they're even supposed to do how do you justify to your board if you start making donations by
[3877.46 --> 3883.70]  the tune of like hundreds of thousands of dollars to support all your uh downstream uh dependencies
[3883.70 --> 3889.78]  i think as a tax entity you cannot do give donations to a something that is not a non-profit
[3889.78 --> 3894.02]  there you go exactly like there's a legal definition to what can a company donate to
[3894.02 --> 3900.82]  exactly and then i have maintainers who i truly understand the plight of because like hi but uh
[3900.82 --> 3907.62]  uh and then they come to me and they're like but but i have all of these users and they make so much
[3907.62 --> 3915.86]  money out of it and they don't donate any of it to me and i'm like yeah yeah that's yeah they don't
[3915.86 --> 3922.74]  donate money that's not what they do give them a send them a pdf send them an invoice offer them
[3922.74 --> 3929.38]  something it doesn't have to be much logo on the page support hours i mean i actually have a whole idea
[3929.38 --> 3933.62]  of what you can offer them and there's a changelog uh podcast episode if you want to hear about that
[3933.62 --> 3937.62]  but the proper opinion is not about everybody should be doing what i'm doing what i'm doing is
[3937.62 --> 3943.70]  kind of weird and uh you know we'll find out if it works but donations are not it and getting angry
[3943.70 --> 3949.78]  at companies for not donating uh money i don't know on the moral level if it's right or wrong you know
[3949.78 --> 3955.30]  capitalism might be all wrong and i will probably i would probably agree with that argument but since we do
[3955.30 --> 3960.66]  live in capitalism donations will just not work technically it doesn't work for companies it's
[3960.66 --> 3964.58]  true that you have to offer something there you go offer a sticker for a thousand bucks but offer a
[3964.58 --> 3973.06]  sticker offer sell something yes uh and and then send them a invoice a pdf sign up for bill.com
[3973.06 --> 3979.94]  it's fine it's a web ui i promise you'll be okay developers don't like a paper work i have a solution
[3979.94 --> 3989.62]  make my wife do all the paperwork and send the pdf this is a much solution yeah handling
[3989.62 --> 3994.98]  or marrying a responsible adult is a great strategy in life kudos you you hacked it you won
[3997.86 --> 4004.02]  yeah i um the thing though is that i never heard a dentist say the same thing like i never i never heard
[4004.02 --> 4009.86]  a dentist say you know i really like teeth but i really don't like paperwork so i don't bill anybody
[4010.66 --> 4018.18]  like no we have to make enough money to hire somebody to to do the administrative work which
[4018.18 --> 4023.30]  i think is it's a chicken and the egg problem fair enough you're saying dentists also hire somebody to
[4023.30 --> 4030.26]  uh get uh get them to do the paperwork i guess that's fair yeah well they they hire people who
[4030.26 --> 4036.66]  specifically the job is to do like insurance billing oh right the us i had forgotten about
[4036.66 --> 4041.94]  all that sorry i had forgotten that for every doctor you have like five administrative people
[4041.94 --> 4049.70]  yeah no it's a little different over here yeah well my unpopular opinion is a in a also a non-software
[4049.70 --> 4056.50]  world um cooking i think kitchens are overrated and i think most households all they need is a
[4056.50 --> 4063.78]  multi-cooker specifically i can recommend from my personal use the ninja foodie i forget 16 in one
[4063.78 --> 4069.86]  or something 15 in one i i can like remove my kitchen if it would be less of an effort i would
[4069.86 --> 4074.82]  just throw away the entire kitchen take one square meter put the pot there and that's it
[4075.70 --> 4081.38]  that and the disher i i think it's very brave of you to to say this in the presence of two italians
[4081.38 --> 4088.02]  i know i know i'm sorry i mean honestly i was here thinking that if it can make pasta i might be down
[4088.66 --> 4094.98]  it can do anything it can make the sauce like so today what i did is is the sauce for tomatoes like
[4096.02 --> 4100.98]  vegan meatballs so i i took the vegan thing fried it there then put the tomato sauce there like
[4100.98 --> 4105.78]  everything in one pot and then it goes into the disher not like you know if you have a special fancy
[4105.78 --> 4110.74]  pan you will not you'll have to hand wash it you're gonna have to have two pots right maybe no
[4110.74 --> 4119.46]  no i'm italian but i'm completely unable to cook so i i'm actually also a terrible cook i can cook
[4119.46 --> 4124.98]  pasta uh which okay by italian standards i'm a terrible cook uh by us standards actually i would
[4124.98 --> 4129.86]  always like cook pasta and risotto and be like oh yeah yeah like i'll cook dinner for everybody
[4129.86 --> 4134.34]  don't worry and like and people would be like oh yeah this is so great this is italian pasta and
[4134.34 --> 4140.90]  i'll be like it's like parmigiano yeah it's not parmesan that's what makes it the pasta good
[4141.78 --> 4148.58]  it i mean pretty much the fewer ingredients the better so the easier the better exactly if this is
[4148.58 --> 4154.58]  your approach a multi-cooker is all you need in life throw away the rest of the kitchen i am listening
[4154.58 --> 4160.74]  my landlord might not appreciate that but we'll tell him after the thing in germany is when you move
[4160.74 --> 4166.50]  into an apartment it's empty it does not have a kitchen and then really yes unless you you move
[4166.50 --> 4172.50]  into a fully rented apartment the standard like a normal apartment is a long term so there's never
[4172.50 --> 4178.10]  a deadline in the in the contract but there's also no kitchen there's also no lamp there's like a cable
[4178.10 --> 4183.06]  hanging from the ceiling you're lucky if there's a bulb but usually the first thing you do when you
[4183.06 --> 4187.46]  assign a rental contract which is like three months in the future you also order a kitchen because
[4187.46 --> 4192.90]  that also takes three months that does make sense so for especially for people with such setups it's
[4192.90 --> 4199.22]  amazing yeah a sink is something that has to be in the apartment okay so you do get a sick nice uh
[4199.22 --> 4204.10]  no in italy if you get something unfurnished it might not have the lamp but it will have the kitchen
[4204.10 --> 4206.98]  which i guess says something about italians and germans
[4210.66 --> 4215.94]  all right let's see which unpopular opinion wins may the odds be in our favor thanks everybody who
[4215.94 --> 4225.06]  are joining and let's pretend this is the outro tune that is go time for this week thanks for
[4225.06 --> 4232.90]  hanging with us subscribe now if you haven't already head to go time.fm for all the ways also check out
[4232.90 --> 4238.74]  changelog news while you're at it it's the software industry's best weekly podcast slash newsletter to
[4238.74 --> 4245.06]  keep you plugged in to developer news worth your attention subscribe now at changelog.com
[4245.06 --> 4253.54]  slash news thanks once again to our partners fastly.com fly to io and typesense.org and thank you to
[4253.54 --> 4258.66]  breakmaster cylinder for producing so many fresh beats for us that we're now releasing full-length
[4258.66 --> 4264.82]  albums on spotify apple music and the rest listen along by searching for changelog beats in your music
[4264.82 --> 4280.74]  gap of choice you'll find us that's all for now but we'll talk to you again next time on go time
[4280.74 --> 4290.74]  you
