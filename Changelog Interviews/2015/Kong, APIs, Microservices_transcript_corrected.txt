[0.00 → 2.96] I'm Ahmad Masri, and you're listening to The Change Log.
[11.80 → 15.80] Welcome back everyone. This is The Change Log, and I'm your host Adam Stachowiak.
[15.92 → 20.66] This is episode 185 and on today's show we're talking to Ahmad Masri.
[21.10 → 24.10] We're talking about Kong, the open source management layer for APIs.
[24.76 → 28.26] We're talking about what it is, why it exists and why Mash Ape is behind it.
[28.26 → 34.66] We had four awesome sponsors, Code Ship, Braintree, Harvest and also DigitalOcean.
[35.12 → 40.74] Our first sponsor is Code Ship, and they've got an awesome e-book totally for free for you to download today.
[41.14 → 48.88] Head to resources.codeship.com slash e-books, and you're going to see a book there called Why Containers in Docker are the Future.
[49.34 → 55.56] Now this e-book is going to help you learn what the differences are between the traditional virtual machine and container stacks.
[55.56 → 60.36] You'll also learn about Docker and its ecosystem and why it's such a big deal.
[60.82 → 65.18] And you'll also learn about Docker and its community and how they're helping to standardize the container workflow.
[65.82 → 70.16] Now you can go to resources.codeship.com slash e-books right now and download this e-book.
[70.58 → 76.46] And I shouldn't tell you this, but when you do that, you're going to get access to three other e-books from Code Ship.
[76.46 → 82.76] We're diving deep into Docker, continuous delivery and how to do all this with native Docker support.
[83.04 → 88.66] Head to resources.codeship.com slash e-books and download those e-books right now.
[88.72 → 92.26] Or head to our show notes for the link and tell them the changelog sent you.
[92.76 → 93.88] And now on to the show.
[93.88 → 104.96] All right, everyone, we are back.
[105.06 → 107.44] It's Jared here with another episode of the changelog.
[107.80 → 116.68] Today, I'm joined by Ahmed Masri, who is the head of engineering at Mash Ape and an advocate of all things open source.
[116.80 → 117.80] Ahmed, welcome to the show.
[119.04 → 119.76] Thank you for having me.
[120.96 → 122.48] So we're excited to talk to you.
[122.48 → 129.12] We also are excited about this little thing called Kong, which sounds really cool.
[129.24 → 130.90] Also, it's a little bit nebulous to me.
[130.98 → 134.04] So I think this would be a good opportunity to learn all about it.
[134.18 → 140.02] Kong is an open source management layer for APIs, which delivers high performance and reliability.
[140.66 → 142.28] We'll get into Kong in a little bit, Ahmed.
[142.42 → 146.92] But at first, I'd like to just get to know you a little bit and hear a little about your history,
[146.92 → 150.96] because you have what I think is somewhat of a fascinating history.
[152.48 → 153.22] What do you think?
[153.26 → 153.94] Where should we start?
[155.06 → 157.02] Sure, we can go back as far as you want.
[158.62 → 161.70] So, well, let's start where you're at right now.
[161.76 → 163.00] So you live in Canada.
[163.54 → 164.02] That's right.
[164.06 → 164.68] I live in Toronto.
[165.48 → 165.88] Okay.
[165.88 → 170.74] And as we were talking, kind of setting this call up, you were in London for a little while.
[172.14 → 175.06] But that was just a was that vacation or work related?
[175.94 → 176.72] It was work related.
[176.86 → 183.52] I actually travel a lot for conferences, events, and as part of the Mad Shape clientele and work we do.
[183.68 → 187.64] We also have teams across the globe and clients across the globe.
[187.70 → 192.34] So we actually have a team in London as well, as well as the company itself is based out of San Francisco.
[192.34 → 197.40] So if I'm not in Toronto, I'm usually on a plane heading somewhere or on the way back.
[197.48 → 197.62] Yeah.
[198.22 → 199.44] But you're not a Toronto native.
[199.62 → 201.90] You were originally from Syria.
[201.90 → 203.58] So maybe let's go all the way back.
[203.88 → 211.76] Your childhood, you had what I think was an interesting childhood, especially with, you know, access to PlayStation magazine that other people didn't have.
[211.82 → 215.54] Give us some of your backstory of how you came from Syria to Canada.
[215.54 → 215.78] Sure.
[216.54 → 218.80] So I was actually born in Damascus, Syria.
[219.50 → 223.58] And back in the 80s, I was born in 85.
[224.54 → 231.38] Syria was still kind of in the pre-crazy state that it is now, but also pre-opening up to the world.
[232.40 → 236.10] So growing up in Syria was, you know, normal childhood, normal life.
[236.22 → 237.92] We never really had any problems or issues.
[238.04 → 244.64] This whole concept of terrorism and terror in general and fighting and war was really foreign to us.
[244.64 → 252.70] And, you know, just like for me as a child growing up, you know, I come from a Sunni Muslim background.
[252.88 → 253.70] My family is Sunnis.
[254.02 → 258.64] I went to a Shiite school and most of my friends were actually Christians.
[259.38 → 262.04] So you can tell there's a big diversity there in the country.
[262.22 → 267.38] So I actually got a little bit of worldly education growing up within Syria before even leaving Syria.
[267.38 → 274.94] But, you know, I think for me, there's always been more to see in the world, more things to explore.
[275.56 → 279.76] And I kind of gravitated towards the technology space and the Internet in general.
[279.98 → 286.90] I remember when I was still like 12, 13 years old, we never had Internet in the country.
[286.98 → 288.48] We didn't even have cell phones back then.
[288.48 → 299.00] And the only way you can get access to the Internet is through long distance dial up to the neighbouring country, which is Lebanon, and which was highly illegal as well.
[299.54 → 313.98] So I used to actually sit in my dad's office and long distance Lebanon just to get access to the Internet from a service provider called Siberia at the time, which is a weird name to choose, given that we're in the Middle East.
[313.98 → 320.28] But anyway, so Siberia was my Internet access provider, my very first one, which was based out of Lebanon.
[320.88 → 322.08] And this was highly illegal.
[322.40 → 329.54] So the government had the kind of secret services and like the internal police is what we call them.
[329.78 → 337.14] And they would go around and make sure they listen in on all the phone communications in and out of the country because, you know, it's a dictatorship, and they're paranoid about everything.
[337.72 → 342.06] So, of course, Internet access was really forbidden because why would you want to know about the world?
[342.06 → 346.96] Why would you want to be educated about, you know, how sciences and the rest of the world actually lives?
[347.34 → 349.70] So they would go around and try to shut these down.
[349.84 → 360.00] And I remember being, you know, a 12-year-old sitting in my dad's office late at night, browsing the Internet, looking up Yahoo's homepage, trying to learn things about technology and computers.
[360.00 → 364.94] And, you know, the knocking on the door would be like at 12 o'clock at midnight.
[365.68 → 373.52] And you just go quiet, and you turn off all the lights, and you just pretend you're not there because otherwise they would really try to break it, break through and get in there.
[374.04 → 375.96] Really? Like they're actually coming after you?
[376.14 → 376.48] Oh, yeah.
[377.54 → 377.78] Wow.
[377.78 → 381.18] But, you know, the reality is they're not coming after you to punish you.
[381.24 → 387.12] They're coming after you for bribery so that you can bribe them, and then they give back to their friends and families, I guess.
[387.78 → 388.36] Oh, I see.
[388.48 → 393.26] So it's illegal, but also the enforcement of it is somewhat lawless.
[393.26 → 395.74] So they're not going to, you know, do it by the books.
[395.86 → 396.46] They're going to...
[396.46 → 396.76] Exactly.
[396.98 → 403.50] It was completely corrupted, which is why a lot of people got away with it, because essentially you bribe your way through it and you're fine.
[403.50 → 410.14] A few years later, we started getting Internet service from the government, provided by the government, and, you know, cell phone service started becoming the norm.
[411.76 → 425.84] And then, you know, for me, like that just evolved into actually getting into the entrepreneurial mindset of actually using this thing called the Internet to my benefit and trying to capitalize or monetize on it.
[425.84 → 438.02] So one of the things I used to do as a kid, I used to go online and find all the cheat codes to computer games or PlayStation games and then sell them to my friends who didn't have Internet access, didn't even know what the Internet is.
[438.02 → 449.10] So there was this thing called PlayStation magazine back in the day, and I used to access it online, and they had like a big directory of all the passwords and all the games and their cheat codes.
[450.50 → 454.76] So I would actually access that online and get all the information from there and follow the articles through.
[454.76 → 467.58] And then as my parents travel or, you know, as we go out as families to trips, we would usually go to neighbouring countries to Lebanon who had less of a global boycott and restrictions on trade as Syria did.
[467.72 → 469.30] So they actually imported a lot of things.
[469.88 → 481.84] And two of the main things I used to just love grabbing when I was in Lebanon visiting our PlayStation magazine, the actual physical copy and Pepsi, because we never had any Pepsi from Syria.
[482.00 → 482.76] Not Coca-Cola?
[482.76 → 483.36] Come on, man.
[483.36 → 485.22] No, no, it's all Pepsi all the way.
[485.70 → 487.00] Are you still Pepsi to this day?
[487.18 → 488.32] Still Pepsi to this day.
[489.00 → 490.10] So you're still on the dark side.
[490.20 → 490.36] OK.
[492.08 → 498.10] So you're getting these PlayStation magazines and there are cheats in the back of them.
[498.12 → 498.62] Is that right?
[498.72 → 501.14] I remember PSN, but I wasn't a reader.
[501.74 → 502.38] Yeah, I was.
[502.64 → 507.02] So, I mean, it was also all fully in English, and I was still kind of learning English at the time.
[507.02 → 518.16] So, you know, it was both kind of adventure for me to learn English and read better this kind of magazines, as well as go online and discover things online that are predominantly in English.
[518.16 → 524.90] But also as being a kid and playing video games, that was kind of my only way to see what's coming up next.
[524.90 → 529.94] So I'll be talking about the next Tomb Raider version that's coming down in a couple of months.
[530.04 → 534.32] But we probably won't see it for another year and a half or two years until the smugglers get it into the country.
[535.76 → 539.32] And that's how you got everything back then, because, you know, it was a boycott situation.
[539.32 → 541.36] There was no trade, international trade happening.
[541.62 → 549.08] So electronics were illegal unless they came from other communist countries, which, of course, they don't have PlayStation there, and they don't have video games there.
[551.18 → 560.36] So, yeah, that was kind of the early childhood and the early kind of foray into leveraging the World Wide Web for entrepreneurship purposes.
[561.06 → 563.80] So you would actually sell these codes to your friends, is that right?
[563.80 → 572.08] That's right. I would sell them the cheat codes and or trade them for treats and candies and kind of toys and things.
[573.08 → 579.36] What's the market value of like a single cheat code back in the day? Do you remember?
[579.70 → 587.10] Well, I went with like the lowest paper bill, which was the five Syrian pounds paper bill.
[587.10 → 598.80] So I do the conversion rate at the time, a single Syrian pound, sorry, a single U.S. dollars equated 50 Syrian pounds.
[599.20 → 600.40] So it was pretty cheap.
[601.18 → 601.82] Pretty cheap.
[602.34 → 608.18] Yeah. But for the economy of the country, that was actually not very cheap, because especially for kids who don't actually have money.
[608.38 → 611.44] It was like early teens type kids, like 13-year-olds.
[611.44 → 615.12] You know, is that the kind of the age group that you were into?
[615.20 → 616.60] Yeah, 13-year-old and younger.
[617.08 → 620.20] Obviously, the older kids wouldn't pay you any attention.
[620.60 → 621.44] So. Right.
[621.54 → 622.90] But the younger kids are more gullible.
[623.02 → 624.54] So it's sell more to those.
[625.60 → 626.92] So, I mean, it's putting a trend here.
[627.02 → 631.48] We recently had Mitchell Hashimoto back on the show to talk about Otto.
[631.68 → 633.02] Let's see what episode that was.
[633.12 → 633.56] 180.
[633.56 → 639.64] And he got into the game kind of selling cheats as well to a certain degree.
[640.80 → 644.48] But he was basically writing bots for Neopets.
[644.62 → 644.88] Nice.
[645.10 → 652.72] And that was kind of what his entrance into maybe not his entrance into software, but something that he remembers as kind of launching off point.
[653.28 → 657.38] You started off with these PlayStation magazines and other such things and talk about knowledge is power.
[657.52 → 659.34] That knowledge is like literally money in this case.
[659.54 → 659.92] That's right.
[659.92 → 661.92] How did you, and you're leveraging that?
[662.06 → 670.28] How did it how did it turn into software or coding, or where'd you get past like video game consoles and into software?
[670.96 → 677.84] So the cheating industry itself evolved at the time or like the surrounding tooling evolved.
[677.96 → 687.06] I remember there was a thing called the shark that you actually plugged into the back of your PlayStation to get, you know, a database of cheats automatically enabled on your device.
[687.06 → 691.70] And that required a little bit more of a hardware hacking, a little bit of hardware knowledge.
[692.42 → 698.96] And then also the PlayStation itself, because we were in Syria, you can't get the original disks for games.
[699.10 → 700.06] You have to get copies.
[700.44 → 704.42] And there was like hardware kind of restrictions in place to prevent that from happening.
[704.42 → 719.00] So I had to learn more about the both the hardware aspect and the software aspect of how these tools work, namely the PlayStation device itself, the the internal of the motherboard on it and how actually all the protections in place were.
[719.42 → 727.00] And by looking at that information up online, as well as kind of working and collaborating with other people doing the same thing, we kind of self-taught ourselves how these things work.
[727.00 → 730.54] And of course, there are tutorials online for almost everything, even back in those days.
[731.38 → 733.96] So that's kind of evolved into a little bit of hardware hacking.
[733.96 → 746.20] And then that itself done, you know, along the years, I kind of transitioned from, you know, the video game stuff to especially as the country started getting cellular service to mobile phones and mobile devices.
[746.20 → 751.04] And I remember like one of my very first devices was a smartphone back then.
[751.12 → 759.20] It was called the Nokia 7650, which was this Symbian S60 operating system, if anybody remembers that anymore.
[759.92 → 766.92] And that was basically where people didn't even know what a smartphone is and the limitations of the there was no marketplace.
[767.16 → 768.44] There was no app store.
[768.52 → 769.40] There was nothing like that.
[769.40 → 771.10] But people still build software for that.
[771.10 → 790.60] And I started getting into the business of finding applications online for this operating system and installing it for people for money and just blowing their minds off with it because they never imagined their phone could have games and other applications and calendars and things that they can use it beyond just making phone calls.
[790.60 → 800.28] So that kind of evolved as well into both another entrepreneurial adventure of figuring out how to build and make applications for the Symbian S60.
[800.88 → 812.38] And then just also selling that, of course, because they all became part of the same mindset of find the technology, leverage the technology to your needs and then win and profit.
[812.38 → 819.30] Sounds like you have way more of an entrepreneurial spirit than I do.
[819.30 → 827.04] I probably would have just taken the PlayStation sheets and went and cheated at the game by myself and never went anywhere from there.
[827.14 → 828.42] But you've gone quite a ways.
[828.54 → 831.58] I mean, now you live in Toronto, so that's a long ways from Syria.
[831.70 → 835.54] Why don't you tell us how you came to be a Canadian, so to speak?
[835.54 → 843.30] So my parents actually applied for immigration to Canada before I was even born.
[844.64 → 857.34] But since the immigration process back there and even back then was just so convoluted and took so long, they never actually heard back and eventually forgot about the whole thing.
[857.42 → 861.76] And then, you know, obviously had me and my brother and, you know, life goes on.
[861.76 → 873.98] And then I remember just before my 20th birthday is when they actually got a letter from the Canadian embassy saying, oh, yeah, I remember that thing you applied for 19 years ago?
[874.52 → 876.02] Yeah, you're here.
[876.18 → 876.42] You're good.
[876.76 → 877.22] 19 years?
[877.52 → 877.70] Yeah.
[878.22 → 882.90] So they finally got like the green light to actually come to Canada.
[882.90 → 894.12] And because at the time they applied before we were even born, my brother and I didn't have to reapply on our own because otherwise we have, at least for me, I would have to apply again as an adult because I was over 18.
[895.48 → 901.50] So, yeah, that was, we basically had my 20th birthday in Damascus.
[901.78 → 903.40] That was the last birthday I ever had in Damascus.
[903.40 → 910.90] And a couple of months later, we were on a plane, and we came to Canada, and we just pushed the reset button and started our lives all over here.
[910.90 → 911.46] Wow.
[911.80 → 914.34] So nobody in your family had ever been to Canada.
[914.92 → 915.72] Is that right?
[917.56 → 924.04] No, we've actually had like distant cousins and family members who kind of came here years and years ago.
[924.30 → 927.00] So like my dad's cousin, second removed.
[927.22 → 930.70] But I mean, in your immediate family, like your parents hadn't come and visited or had they?
[931.04 → 931.24] No.
[931.48 → 935.74] It was fresh, literally fresh off the boat in all sense of the word.
[935.74 → 941.58] So the four of you moved from Damascus to Toronto, sight unseen.
[942.32 → 945.66] Just picked up and just started life over again in Canada.
[946.00 → 946.18] Yep.
[947.20 → 948.90] That had to be some wild ride.
[950.04 → 950.82] It is.
[951.00 → 963.58] And, you know, it's not like the in today's world, in today's media, they like to portray the Middle East and that part of the world as being completely disconnected from Western culture.
[963.58 → 964.22] It isn't.
[964.70 → 968.32] The reality is we were very engraved in Western culture as it, as it was.
[969.94 → 979.60] Whether through obviously the production of TV and Hollywood movies and all that, or just by, you know, being part of the world, of course, we were very aware of culture around the world.
[979.60 → 984.86] And my dad has actually been like, in his youth, he travelled around the world.
[984.98 → 986.42] He's seen a lot of places around the world.
[986.52 → 990.76] He had never come to Canada, but he lived a while in Paris.
[990.88 → 994.74] He lived a while in London, and he travelled in all over Northern Africa.
[995.42 → 998.74] So, you know, I got a little bit of a foundation to start on.
[998.74 → 1006.48] But obviously there's a bit of a culture shock that you get as much as you think you are prepared.
[1006.88 → 1014.78] There's a little bit of a culture shock that when I first walked along downtown Toronto and I looked at the skyscrapers, I just couldn't look down.
[1014.88 → 1017.14] I was just continually looking up because it was amazing.
[1017.88 → 1020.02] We have buildings in Damascus.
[1020.12 → 1021.64] We have tall buildings in Damascus.
[1021.64 → 1031.76] But not really to the extent of the skyscrapers that we have in Toronto today, of course, and, you know, developed cities around the world as much as we do.
[1032.36 → 1037.70] But that was kind of the biggest, one of the very first memories I remember coming to Toronto is these skyscrapers.
[1037.84 → 1039.16] It was so huge and massive.
[1040.66 → 1045.66] So that's one part of it, obviously, is like the scenery changes around you.
[1045.66 → 1053.10] And then there's the other part that it was, you know, mid-July, and I was still walking around with a heavy, thick winter coat because I was freezing my ass off.
[1053.76 → 1054.08] Right.
[1054.30 → 1060.32] Having grown up in the Middle Eastern kind of temperatures and weather, coming to Canada took a while to adjust to the cold.
[1061.88 → 1065.52] Yeah, we have a friend who lives pretty much on the equator over in Kenya.
[1066.04 → 1066.28] Nice.
[1066.28 → 1067.82] And he visits here pretty regularly.
[1067.82 → 1072.40] And he cannot adjust to the cold at all.
[1072.52 → 1077.66] I'm in, you know, Omaha, Nebraska, so more temperate than where you're at, but still gets cold in the winter.
[1077.76 → 1079.44] And it doesn't even matter what time of year it is.
[1079.78 → 1080.66] Dude's always cold.
[1080.92 → 1082.40] Yeah, I can certainly relate.
[1084.16 → 1086.20] So that brings you to Toronto.
[1086.50 → 1090.14] And no doubt you've had a bit of a career since then.
[1090.22 → 1092.30] You're now the head of engineering at Mash Ape.
[1092.30 → 1104.84] So briefly, and then we're going to get into Kong right after the commercial break, but briefly, can you just tell us, like, career-wise how you went from, okay, I'm moving to Toronto, age 20, and now I'm head of engineering at Mash Ape.
[1106.00 → 1111.00] So the obvious push from my parents was for me to go into university and continue my education.
[1111.00 → 1120.20] I had done a year of computer science in Syria, but at the time, the universities here just didn't accredit everything that I've done.
[1120.20 → 1126.20] So they wanted me to start from scratch, even go back half a year in high school, which I found to be unacceptable.
[1126.48 → 1128.22] So I basically said, screw that.
[1128.30 → 1129.62] I'm just going to go and do my own thing.
[1130.10 → 1135.74] And went back to my best friends, the internet, and going online and connecting with people around the world.
[1136.42 → 1141.90] And basically, I got myself into PHP before I even came to Canada.
[1142.02 → 1145.82] I was starting to develop things and building custom stuff for people on custom websites.
[1145.82 → 1148.38] And then I continued that in Canada.
[1148.38 → 1163.30] And slowly, I went from just hacking little PHP projects on things like Desk and services online to people to joining a company in Toronto and actually just a full-time job and doing PHP development, as green as I was at the time.
[1163.30 → 1172.24] And slowly just made my way through and growing and learning new technologies and new systems and meeting new teams and building new products.
[1172.38 → 1184.74] And it was all really around open source in general, but evolved from different languages and different systems and services to where I am today, working with Misshape, building APIs and tools for the rest of the development community.
[1184.74 → 1187.28] Very cool.
[1187.36 → 1188.66] Well, I think that's a good place to stop.
[1188.92 → 1191.48] We will take a break here from one of our awesome sponsors.
[1191.82 → 1194.32] And on the other side, we're going to dive full into Kong.
[1194.72 → 1195.94] So stay tuned for that.
[1198.52 → 1203.98] Braintree is all about making developer lives simpler with code for easy online payments.
[1204.44 → 1207.84] If you're searching for a simple payment solution, check out Braintree.
[1207.84 → 1215.78] For mobile app developers out there, the Braintree V.0 SDK makes it easy to offer multiple payment types.
[1216.30 → 1224.96] Start accepting PayPal, Apple Pay, Bitcoin, Venmo, traditional credit cards, and whatever's next, all with a single integration.
[1225.64 → 1228.38] Enjoy simple, secure payments that you can integrate in minutes.
[1228.82 → 1230.04] And developers, they've got you.
[1230.08 → 1232.30] Don't worry about taking days to integrate your payments.
[1232.78 → 1234.34] With Braintree, it's done in minutes.
[1234.34 → 1239.84] And if you don't have time, give them a call, and they'll handle the integration for you and walk you through it.
[1240.40 → 1244.18] Braintree supports Android, iOS, and JavaScript clients.
[1244.58 → 1251.78] They have SDKs in seven languages, .NET, Node.js, Java, Perl, PHP, Python, and Ruby.
[1252.20 → 1255.32] And their documentation is comprehensive, and it's easy to follow.
[1255.32 → 1264.52] To learn more and for your first $50,000 in transactions fee-free, go to BraintreePayments.com slash changelog.
[1267.98 → 1273.08] All right, we are back with Ahmed Masri, and we are ready to talk about Kong.
[1273.40 → 1279.50] Now I'd be remiss not to give a shout-out to Justin Dorfman, who's a changelog member, who helped us line up this show.
[1279.50 → 1284.88] He's very interested in Kong as the developer evangelist at Max CDN.
[1285.30 → 1287.22] Sounds like lots of people are interested in Kong.
[1287.38 → 1289.18] Can you give us the elevator pitch?
[1289.52 → 1290.26] What's it good for?
[1290.34 → 1290.78] What does it do?
[1290.86 → 1291.58] Why does it exist?
[1292.72 → 1300.94] So Kong is the API management and abstraction layer for your APIs and microservices.
[1300.94 → 1315.40] It allows you to securely and easily configure APIs and microservices at scale without having to deal with massive deployments and re-architecting systems or even changing the way you design your APIs.
[1316.38 → 1324.00] It really works on the HTTP layer alone, and it's very unopinionated about how APIs are done or built, which is part of the appeal to a lot of people.
[1324.00 → 1336.80] Because in today's world of API technology, people come in from SOAP, people come in from REST, people come in from different kind of mindset to what's the best architecture and format to deliver APIs.
[1337.54 → 1343.30] And in a lot of ways, a lot of the tools and services out there are very opinionated for various reasons.
[1344.06 → 1352.78] So what we did with Kong, we wanted to keep it unopinionated and wanted to keep it abstract and more associated with the HTTP layer, which is the spec that the entire web runs on.
[1352.78 → 1363.10] So that's what really Kong gives you is the ability to control, manage and configure your APIs in a way that is completely agnostic to how your backend or actual APIs operate.
[1364.24 → 1368.20] So just notice that you use APIs plural there.
[1368.32 → 1376.74] So this is for somebody who has a handful, maybe half a dozen, maybe more different APIs that they're offering either publicly or internally?
[1376.74 → 1378.52] So not necessarily.
[1378.72 → 1384.10] And this is, again, part of the chaos that the industry is in today.
[1384.28 → 1386.46] It's not necessarily a negative state of chaos.
[1386.46 → 1390.68] It's just a kind of entropy state where things are just evolving and happening around us.
[1391.50 → 1395.82] So Mass Shape actually started out as, well, that first product was the API marketplace.
[1396.66 → 1399.78] And kind of the short pitch for that, it's eBay for APIs.
[1399.78 → 1412.16] So API providers and publishers can come in and publish their API through the marketplace, whether it's free or monetized, and then just expose it to a vast majority and a vast community of users.
[1412.72 → 1419.96] And then the consumers of the API or people who are building applications can come and discover and select APIs that fit their needs for building their applications.
[1419.96 → 1439.12] As part of being the marketplace, our tools and our proxies and our marketplace itself had to literally support every which way that API providers build APIs and had to support every which way that API consumers expect to consume APIs.
[1439.68 → 1441.54] So we can't be opinionated.
[1441.70 → 1447.88] We couldn't be more subscribed to a single way of building APIs or a single standard or approach.
[1447.88 → 1459.94] So all the talk about, you know, SOA versus microservices versus REST versus SOAP versus X and Y and Z, we just say a thumbs up to all of that because we had to.
[1461.26 → 1464.40] Is there a real difference between SOA and microservices?
[1465.36 → 1467.22] Is there a distinguishable thing or are they just terms?
[1468.06 → 1471.56] You're touching on war territory here.
[1473.10 → 1473.82] Let's hear it.
[1473.84 → 1476.66] I don't have an opinion, so you can just state yours and we'll move right along.
[1476.66 → 1477.22] It'll be a war.
[1477.22 → 1480.28] My opinion is a bit deeper than that.
[1480.40 → 1490.18] I think a lot of people in the industry have a big, big issue distinguishing between modularization, componentization and microservices.
[1491.52 → 1496.80] So these three things are completely independent and, you know, overlapping in a lot of ways.
[1497.24 → 1501.34] Typically, in my view, modularization is more about the code.
[1501.62 → 1502.80] You modularize your code.
[1502.80 → 1509.72] So all the benefits that people talk about microservices is just a way that you can package things together.
[1509.90 → 1512.62] There's, you know, single focus and testable and blah, blah, blah.
[1512.82 → 1514.48] Yeah, but that's more about being modular.
[1515.18 → 1515.58] All right.
[1515.58 → 1520.06] So you can do that as part of codes and libraries and the way you organize your project.
[1520.06 → 1521.88] Same thing for components.
[1522.38 → 1526.06] Components are just a bunch of modules put together to serve a purpose.
[1526.24 → 1529.88] So you can talk about a module being a login module.
[1530.72 → 1535.78] Or you can talk about a module being a username lookup module.
[1535.78 → 1539.78] And another module being the password verification module.
[1540.14 → 1542.20] And then together they become the login component.
[1543.00 → 1548.14] And then in terms of services or microservices as the term is today, same thing with SOA.
[1548.74 → 1558.08] It's more about how these components, which exist to compose of multiple modules, are deployed and managed and operate independently.
[1558.08 → 1569.34] Now, the only thing microservices introduce that's a little bit kind of, at least if you're here to listen to some of the advocates, it's a little bit different from SOA is that it's entirely focused on the HTTP layer.
[1570.40 → 1576.00] As opposed to SOA doesn't really prescribe to being over HTTP or not.
[1576.40 → 1578.26] It just happens to be in a lot of cases.
[1578.46 → 1582.98] But microservices focus on, no, no, no, let's just do things as the web has evolved over HTTP.
[1583.14 → 1587.10] Let's do things as well over HTTP between our products and tools and services within it.
[1587.10 → 1594.66] So I think, you know, generally speaking, and again, because we had to be the marketplace for so long, we're fine with all of that.
[1595.50 → 1597.36] You know, obviously people have personal opinions.
[1597.82 → 1612.14] But at the end of the day, if you're building a product that's solving a problem for your users, they don't really care about are you RESTful or are you SOAP or are you microservices or SOA or so on.
[1612.48 → 1613.64] The point is a product.
[1613.98 → 1615.96] And that's kind of our message that we carry to people.
[1615.96 → 1618.58] When we're talking about an API, an API is a product.
[1618.82 → 1621.48] It's not just a data output.
[1621.64 → 1623.48] It's not just an extension of a product.
[1623.62 → 1624.72] This is a product of itself.
[1625.00 → 1629.64] Because the users of that product are the developers who are supposed to be interacting with it.
[1630.14 → 1641.10] So just as we have product teams and marketing teams and kind of big initiatives around product marketing, we should have the same thing for APIs because we do see them as products.
[1641.10 → 1666.58] So when you have a company that builds APIs for extending their offerings to the bigger market and the bigger community, if they don't put the same effort they put behind their iPhone application or the Android application or the website in terms of marketing, in terms of product management, then most likely is the API itself is not going to be as loved or as there's not going to be as much attention being paid to it as a product on its own.
[1666.58 → 1670.92] So for us, we look at APIs as these individual products.
[1671.44 → 1680.36] However you want to look at it, whether it's a multitude of microservices or a big monolithic API or SOA or so on, it doesn't really matter.
[1680.36 → 1680.44] Yeah.
[1681.16 → 1687.18] I think we run into just name spacing issues when it comes to terms like modules and components.
[1687.54 → 1693.26] And we move fluidly up and down the stack in our conversations with each other.
[1693.46 → 1705.40] Then oftentimes things become conflated because perhaps you're talking about modules at a network layer, or I'm talking about them at an application layer or even inside a code, a library or something.
[1705.40 → 1713.84] So it becomes, we can mince words and I think it's still important to talk about these things and try to come to like one understanding on certain terms.
[1715.16 → 1721.38] But I think what you have here with Kong and what you guys are focusing on with microservices is let's keep it HTTP.
[1722.44 → 1733.76] And then in light of that, let's realize that all these APIs, which we view as products, individual products, they all share these common attributes, these common needs.
[1733.76 → 1748.90] And so why are we all implementing auth and logging and rate limiting over and over and over again in different ways when you could have a layer that sits in front of your APIs and provides that?
[1749.50 → 1750.68] Does that paint the right picture?
[1751.24 → 1752.42] Yeah, that's precisely it.
[1752.42 → 1765.98] And Kong actually evolved in the marketplace itself because, you know, as virtue of being able to offer monetization services for API providers through the marketplace, that means we had to manage their API calls as well, meaning a proxy.
[1766.34 → 1775.20] So everything has to go through our system so that we can track it and appropriately charge for the API calls and so on, and then process it for the consumer.
[1775.20 → 1777.70] So we actually built Kong for ourselves.
[1778.34 → 1787.66] And because, like I said, our need for the marketplace was to be everything for everybody and actually not be penetrated at all, that went into the DNA of making Kong.
[1788.22 → 1798.24] So the idea that we have the authentication and rate limiting and caching control and all this kind of things built into the core really started out because of the marketplace need.
[1798.24 → 1808.16] But then what happened is as the product of the marketplace grew and our clientele kind of became more diversified, we had more enterprise clients who wanted to have things running with their own infrastructure.
[1808.74 → 1815.20] We had people who were worried more about the latency, and they were perhaps using regions on AWS that are not as close to our regions.
[1815.60 → 1824.90] So then we had to worry about how do we actually become a global distribution of proxy service across multiple regions without adding any delay or without losing any context of the data.
[1824.90 → 1830.22] And all these things played into the kind of the makeup and the DNA of Kong.
[1830.54 → 1844.72] So like you said, it's this idea that when you're focusing on building an e-commerce product, or you're focusing on building even a mobile application or an API for a mobile application, your goal is not to do authentication.
[1845.04 → 1846.38] Your goal is not to do logging.
[1846.52 → 1848.56] Your goal is not to do transformation or rate limiting.
[1848.56 → 1856.72] Those things you have to do because of the nature of how the web works, and you want to have security, and you want to perhaps add some protections to your API layer.
[1857.20 → 1870.04] But the reality is in many cases you have to reinvent the wheel every single time in either doing that or luckily in today's world we have libraries and tools that are maintained by the open source community that give you a lot of this functionality.
[1870.04 → 1873.26] But at the same time, you're still responsible for the maintenance of them.
[1873.70 → 1878.44] So think in a scenario where there's a company that has, don't go too far, talk about Netflix.
[1878.64 → 1883.58] They're one of the greatest kind of examples of massive distributions and API management tooling that they've built.
[1884.42 → 1884.52] Yeah.
[1885.04 → 1887.18] They have multiple data centres across the world.
[1887.30 → 1899.04] They have multiple clients, multiple applications, whether it's, you know, PlayStation or mobile phones or desktop TV, smart TVs calling their systems and their APIs to get the data out and get the streams going.
[1899.04 → 1906.02] They probably have, you know, a heck of a lot of APIs that they have to maintain serving different purposes.
[1906.62 → 1909.80] So for each one of these APIs, they probably have to have an authentication layer.
[1910.08 → 1912.68] For each one of these APIs, they have to have some logging mechanism.
[1913.14 → 1916.66] They have to have some, you know, control over what the API is doing.
[1916.80 → 1922.30] And perhaps as they evolve and as they grow as a company, they want to change these APIs, add new versions, add new functionality.
[1922.30 → 1931.68] All of a sudden you're faced with this massive interconnected web of dependencies and repeatable things that you're doing over and over and over again.
[1932.34 → 1938.12] Obviously, like you said, the examples that rank true for a lot of people is authentication is one of the simplest one.
[1938.72 → 1940.92] You have multiple systems, multiple APIs.
[1941.56 → 1942.54] They each have an authentication.
[1942.80 → 1944.30] It's the same authentication mechanism.
[1944.46 → 1948.34] You're doing OAuth on both, or perhaps you're doing JSON web tokens or something similar.
[1948.72 → 1949.68] But it's the same thing.
[1949.68 → 1951.46] Why does it have to live in two different places?
[1952.04 → 1956.94] And then as part of having to be on the application layer itself, it has to also scale with it.
[1957.42 → 1959.46] So, you know, scaling problems become also an issue.
[1959.54 → 1962.80] And how do you maintain the session and the information across servers and all that stuff?
[1963.98 → 1969.38] So with calling, the idea is that you abstract all of these things away, and you move them to the proxy layer.
[1969.78 → 1975.92] And the reality is a lot of people are already running Nginx as their HTTP server or their proxy server.
[1975.92 → 1980.72] And that's also why we chose Nginx as the core for Kong.
[1980.82 → 1982.94] So Kong actually runs on top of Nginx.
[1983.44 → 1991.68] And what it gives you is the ability to configure Nginx servers and configure the proxy mechanisms of Nginx dynamically through a RESTful API of itself.
[1991.68 → 2003.50] So in the olden days, you can actually just set up Nginx and configure it to do everything you want, including customization of things like authentication beyond just the basic authentication.
[2003.50 → 2008.62] You can use Lua as the scripting language with Openest on Nginx to customize it.
[2008.62 → 2011.44] But you would have to do it in configuration files.
[2012.36 → 2014.72] And you have to deploy these configuration files across your cluster.
[2014.84 → 2016.32] And you have to make sure they're all in sync.
[2016.38 → 2018.54] And you have to make sure everything is updated at the same time.
[2019.04 → 2021.22] And sure, there are tooling that help you with that.
[2021.30 → 2024.16] Things like Chef and Ansible and CloudFormation on AWS.
[2025.22 → 2032.96] But that's now becoming a big, massive undertaking for a small team or even a bigger team in an enterprise company.
[2032.96 → 2038.18] Now they have to deal with different departments doing different things, perhaps between development and DevOps and IT and so on.
[2039.38 → 2043.52] So with Kong, you literally have one thing to deal with, which is the API.
[2044.16 → 2049.56] You actually make a call to the Kong admin API in itself and tell Kong to create a new endpoint.
[2050.04 → 2051.68] You tell Kong to add authentication.
[2051.88 → 2054.68] You tell Kong to add logging and so on.
[2055.02 → 2058.22] And you do that through RESTful API calls, which we're all familiar with.
[2058.30 → 2060.96] We can easily make any API call in the command line using curl.
[2060.96 → 2069.00] And these things are automatically synced up across all the clusters without the need for you to redeploy or do it again for every node in the cluster.
[2071.00 → 2074.90] Let me stop you there for a second because I'm trying to make sure that I have the mental model down right.
[2074.98 → 2082.52] When I first started reading this and looking at your diagrams, I thought, okay, Kong is kind of like network address translation that a router might do.
[2082.78 → 2086.56] Where you have multiple services sitting behind it, but one representation.
[2086.56 → 2093.14] But now I'm starting to think maybe if I let's say I'm Netflix and I have two public APIs.
[2093.24 → 2099.70] I have a search API so you can find movies and I have a queue API so you can, you know, see what's in your queue.
[2099.78 → 2100.60] Maybe those are separate.
[2101.02 → 2105.10] Would I have two Kong's or I have a single Kong with multiple endpoints?
[2105.64 → 2107.10] One representing each of those two.
[2107.30 → 2107.66] Single.
[2108.14 → 2108.54] Yeah.
[2108.60 → 2110.14] Single Kong, multiple endpoints.
[2110.14 → 2119.56] So isn't it, is, is Nat kind of good analogy to think of it as a, I know you said proxy, which makes a lot of sense too, but as a single entity representing multiples.
[2120.36 → 2120.72] Yeah.
[2120.82 → 2122.44] I mean, that's a good analogy, of course.
[2123.54 → 2126.82] So you can, you can, and this is the part about us not being opinionated.
[2127.00 → 2137.80] You can use it as a single entity that represent multiple, or you can use it as just the, the translation service to point things in the right direction and, or add logic on top of the request lifecycle.
[2137.80 → 2156.04] So what happens when you have that one, you know, stubborn API that wants to do its authentication just a little bit different from the other ones or has a, you know, you always have these edge cases where, yeah, these three things are 99% the same, but that 1% is super important.
[2157.78 → 2159.58] Do you set up a separate Kong at that point?
[2159.68 → 2163.64] Are there ways that you can have some diversity in your authentication, for instance?
[2163.64 → 2170.46] So let me give you some numbers and for the audiences as well to kind of get the concept of the scale that we're operating within.
[2170.72 → 2177.32] So in the, in the marketplace, we have, I think something around 170,000 active developers.
[2178.00 → 2185.34] We, we, we process a lot of transaction, monetary transaction for paid APIs, I think around an average of $85 per transaction.
[2185.34 → 2196.48] And we have hundreds of public, sorry, thousands of public APIs and hundreds of thousands of private APIs that are not published as part of the public marketplace.
[2197.24 → 2205.82] We process, I think the last numbers we were looking at, I think somewhere around like 10 billion calls per day.
[2205.82 → 2209.68] Uh, and a lot of these APIs are even heavy APIs.
[2209.82 → 2213.50] So for example, Imgur uses the API marketplace for their paid API.
[2213.84 → 2224.52] So if you ever use the Imgur paid API that goes through Mesh Shape's infrastructure, uh, meaning all these people that are uploading and downloading images for displays in the mobile applications, we have to process that.
[2224.52 → 2238.86] That entirety of the scope I'm describing now between, um, hundreds of thousands of, uh, developers and billions of calls is operating on four medium size AWS servers running Kong.
[2239.64 → 2240.18] Four.
[2240.64 → 2241.04] Four.
[2241.30 → 2244.98] So, and that's to be, to be completely fair to Nginx.
[2245.12 → 2249.06] That's really most, mostly Nginx's, uh, efficiency.
[2249.30 → 2250.76] It's not really, you know, nothing.
[2250.86 → 2254.28] There's no special sauce that we're adding in Kong that's making Nginx more efficient.
[2254.52 → 2259.34] This is really Nginx, uh, proxying, uh, being super efficient and super lightweight.
[2259.92 → 2267.38] Um, so the, the layer that we're introducing, even though it is a layer, it's not really adding much in terms of resource usage.
[2267.62 → 2272.70] Uh, and of course, depending on your network setup, it's not really adding anything in terms of network latency at all.
[2273.16 → 2284.24] Um, and as part of the, the plugin architecture that we've created in Kong, the idea is that you can, you can add and remove, uh, logic pieces on top of API routes.
[2284.24 → 2285.36] As you wish.
[2285.50 → 2294.24] So you might have, like you said, you might have, uh, two APIs, two different endpoints or upstreams, and, uh, you want to make an authentication for one, but not the other.
[2294.36 → 2295.50] That's the whole point of the plugins.
[2295.60 → 2299.00] You can enable them per API, and then you can even make it more granular.
[2299.00 → 2301.16] So you can enable and disable things per consumer.
[2301.16 → 2302.16] Mm-hmm.
[2302.16 → 2310.82] So say we have this concept of consumer in the system, and consumer is this abstract notion of anybody or anything that's accessing your APIs.
[2311.30 → 2312.42] So it could be a user.
[2312.70 → 2321.46] That means you create a consumer that matches every user in your system, or it could be an application, or it could be a system, or another server that's trying to access your APIs.
[2321.90 → 2323.42] It's just consuming your API.
[2323.42 → 2329.94] So you can set up rules and enable and disable plugin configuration for each of these consumers.
[2330.20 → 2337.52] So as an example, and I use this all the time when we're doing our webinars, uh, you, you know, a typical use case is to have rate limiting in an API.
[2337.72 → 2339.90] So you would want to enable rate limiting on your API.
[2339.90 → 2346.76] So you have API A that has a rate limiting and API B that has rate limiting that's more appropriate to the different use cases of these APIs.
[2347.20 → 2355.88] But say you've identified a troublesome consumer that's, you know, just making too many calls or perhaps sending you bigger bodies or doing nasty things that you don't like.
[2356.06 → 2364.68] You can make the exception for the rate limiting specific to that consumer to introduce even more harsh rules on the rate limit, uh, per the minute and per the hour.
[2364.68 → 2375.80] So you can actually become very granular in the way you design your API interaction and your logic and calling becomes kind of the protection system in front of your APIs, not just to protect you from number of calls.
[2375.80 → 2380.70] That's going to hit your backend, but to design the experience around your API as well.
[2380.78 → 2388.36] So one of the things we offer as well as a transformation plugin, so you can actually change the request before it even hits your upstream server.
[2389.14 → 2392.78] So say you're doing one of the biggest problems that people deal with is versioning.
[2392.78 → 2398.94] So, you know, as you, your application evolves, as your products evolve, you want to change things up and add more features and functionality.
[2398.94 → 2405.70] But if you're an API provider, you don't want to break the experience for older, uh, application developers or users of your API.
[2406.28 → 2410.52] So with tooling like transformation, you can actually bridge that gap.
[2410.66 → 2418.60] You can make it so that if somebody is making calls with the wrong object name or the wrong, uh, request bodies, you can actually change those up before they hit you're upstream.
[2418.60 → 2435.72] So you're always in a green, uh, lifecycle on your application and the upstream on your actual application stack, but you can expose different things on the API proxy layer that can still benefit, uh, people who are still in the transition period of going up to your most recent kind of documentation, most recent version of your API.
[2435.72 → 2446.90] Yeah, that sounds great for keeping your application code super streamlined and dealing with the complexity of those, basically normalizing those version calls at the, at the proxy layer.
[2447.00 → 2448.70] That sounds like a pretty big win.
[2450.06 → 2454.82] So what about, uh, something a little more, I don't know, a little more complex than authentication.
[2455.16 → 2455.72] What about authorization?
[2456.70 → 2458.76] Not who am I, but what am I able to do?
[2458.82 → 2465.56] Is that something that you guys have found makes a lot of sense at a Kong layer or does that tend to have to be application specific?
[2465.72 → 2470.62] It depends really on the, on the kind of application you're trying to serve behind Kong.
[2470.84 → 2480.98] So we have clients and customers and users of Kong that, um, uh, fit both scenarios, uh, which is going back to the consumer thing that I was talking about.
[2481.10 → 2482.90] That's why we made it into an abstract thing.
[2483.00 → 2490.38] So one of the features of the consumer entities in Kong is that each consumer can have multiple credentials across multiple authentication methods.
[2490.38 → 2501.14] So meaning you can have a single API that you can enable basic authentication on as well as OAuth authentication, as well as JSON web tokens on.
[2501.38 → 2515.20] And you can have a single consumer that can have a credential for, uh, for OAuth and multiple credentials for basic authentication, maybe multiple credentials for OAuth as well, multiple credentials for JSON web tokens.
[2515.20 → 2531.04] So the benefit of that is if you think of scenarios where, uh, and this is one of the things I was helping one of our clients with, if you think of a scenario where you have a mobile as a product, if you think of your products as mobile, and then Android as a platform and iOS as a platform, that's the same product.
[2531.04 → 2539.76] And you want to apply the same rules to the product in general, rather than creating the consumer that represents the Android application and the consumer that represents the iPhone application.
[2540.00 → 2543.90] You just create one single consumer that represents the mobile product.
[2544.00 → 2549.16] And then that individual consumer has different authentication methods for the different platforms.
[2550.04 → 2553.92] So the granularity there becomes, you know, really up to you of how you want to control that.
[2553.92 → 2564.58] The other aspect of this becomes, you know, if you have a partner, like you're, you know, you're a company A or Acme, and you want to give access to another company, um, you know, they have 15 developers.
[2564.58 → 2568.50] Are you going to go and create 15 consumers for each of these 15 developers?
[2568.82 → 2572.32] Maybe, or maybe you can just create a single consumer and give them 15 credentials.
[2572.32 → 2573.16] Hmm.
[2574.36 → 2588.94] That sounds like, you know, going generic and making it, um, easily customizable in this way makes a lot of sense when you're trying to fit all those different use cases, and you can kind of put the puzzle together the way that it makes sense for your product.
[2589.60 → 2593.98] Um, as we all know, every, you know, software development design decision has trade-offs.
[2594.16 → 2602.12] Have you found any drawbacks to the consumer idea and just this very generic, uh, system in general?
[2602.32 → 2602.88] Yeah.
[2603.04 → 2611.20] In fact, it, it sometimes, obviously once, once people get it, once people get, you know, how flexible it is, um, you know, they love it.
[2611.70 → 2614.72] But just to get people through that journey of getting there.
[2614.72 → 2617.60] And I think it's just undoing years of bad practices.
[2618.08 → 2631.78] And unfortunately what the rest of the API tooling industry, um, it's undoing all the brainwashing that, uh, you know, let's call them the competitors have been doing in terms of saying, no, this is the better way of doing things, which is our way.
[2631.78 → 2645.16] And, uh, typically what you see in similar products out there, uh, which, you know, Kong is the only, really the only one that's open source and free and fully supported by, uh, by a company with all its backing behind it.
[2645.16 → 2651.32] Um, what you see is these companies offer you products that, you know, does the similar thing as Kong does, but they're monolithic applications.
[2651.60 → 2652.88] They're very opinionated.
[2653.30 → 2662.00] Uh, they're very heavy on resource usage, and they want you to basically go back to the drawing board and redesign how your application logic works or how you build your APIs.
[2662.00 → 2670.28] So the adoption scale there becomes, you know, uh, a very high ramp up for people to adopt these tools and these products.
[2670.68 → 2681.94] And part of that, what ends up being the result is, uh, developers end up thinking in that one solo way of thinking, or just one line of thought of, okay, well, this is how we do APIs.
[2681.94 → 2683.90] And this is how we do API management.
[2684.24 → 2692.86] And then of course, having been paying hundreds of thousands of dollars for these tools for so many years, uh, somebody in the accounting department finally says enough is enough.
[2692.86 → 2693.86] Go find some alternative.
[2694.34 → 2699.92] And that's when we, when we start coming into the conversation as they discover Kong and talking about the open source and the fact that it's free.
[2699.92 → 2702.72] Obviously that's the starting point for a lot of people.
[2702.96 → 2708.24] And then we get into this conversation about consumers objects and Kong being unopinionated.
[2708.46 → 2711.22] And it's really up to you to design your architecture the way you want it.
[2712.28 → 2719.46] In a lot of cases, developer kind of sit, developers take a step back and say, um, that sounds too loose goose.
[2719.52 → 2720.64] I don't want to get into there.
[2720.92 → 2722.88] Just tell me what the better way to do it is.
[2723.52 → 2729.86] Um, and that's just really, you know, like I said, undoing years of, uh, bad practices or things that were shoved down on the developer.
[2729.92 → 2731.82] Community by these tooling providers.
[2732.16 → 2736.16] And that's also partly why we decided to make Kong free and open source.
[2737.04 → 2742.60] Because we see API management and tooling as, as a commodity that everybody should really have access to.
[2742.70 → 2751.24] It shouldn't be something that you have to pay millions of dollars of, uh, per years for pay hundreds of thousands of dollars for license fees for, to get access to it.
[2751.70 → 2756.10] So that's kind of the drawback, but it's also the same, in the same breath.
[2756.10 → 2760.00] It's also the incentive for a lot of people is that, yeah, you actually get the freedom to do whatever you want.
[2761.64 → 2762.44] Yeah, very good.
[2762.50 → 2763.62] Well, let's take a break here.
[2763.74 → 2765.90] When we get back, I want to talk about some of your technology choices.
[2766.06 → 2767.02] You got Lua in the mix.
[2767.08 → 2768.38] You got Cassandra in the mix.
[2768.94 → 2775.86] Also talk about the enterprise edition and kind of the business side of this from Moshe's perspective and how that fits into the open source stuff.
[2776.02 → 2779.04] So that's on the other side of the break, and we will be right back.
[2779.04 → 2789.26] If you thought harvest was only about time tracking, check again, fast invoicing and payments.
[2789.38 → 2794.22] You can easily create and send invoices and accept payments with PayPal, Stripe, and many more.
[2794.74 → 2796.40] You got expense tracking without the mess.
[2796.50 → 2799.74] You got an iPhone or an Android app to go on the go with you.
[2800.08 → 2802.42] Snap photos or receipts and store them in the harvest app.
[2802.52 → 2807.64] You can also connect favourite tools like Slack and use chat commands to start and stop your timers.
[2807.64 → 2810.58] Head to getharvest.com and start your free trial.
[2811.04 → 2816.02] And once that trial is over, use our code changelog to save 50% off your first month.
[2818.64 → 2821.26] All right, we are back talking about Kong.
[2821.70 → 2824.50] And I want to talk to you a little bit about the technology choices.
[2825.26 → 2829.28] You already mentioned Nginx as a huge aspect of what Kong is.
[2829.88 → 2833.52] Notice that you're almost 100% Lua in the code base.
[2834.74 → 2836.06] Curious about that decision.
[2836.06 → 2841.88] And then just your thoughts in general on Lua as a programming language and how it's been to build Kong with it.
[2841.88 → 2850.02] So the choice in Lua was in a lot of ways made for us years before.
[2850.92 → 2856.54] The Nginx community has actually been the adopters of Lua as the scripting language.
[2856.94 → 2862.28] And for those who are not familiar with Lua, Lua is really fast and powerful and lightweight, embeddable scripting language.
[2862.40 → 2864.82] And it's meant to be embedded within other applications.
[2864.82 → 2868.84] So for example, Adobe actually uses it a lot in their products.
[2869.34 → 2876.00] And it's actually made its way into a lot of embedded systems and embedded application as a scripting layer on top of the application itself.
[2876.00 → 2879.00] So it kind of already fits that model of Nginx.
[2879.92 → 2881.66] It's an HTTP server.
[2882.04 → 2883.38] It's configuration-based.
[2883.68 → 2887.02] It doesn't really have that dynamic aspect or dynamic language aspect to it.
[2887.46 → 2893.52] So Openest was one of the first application servers that ran on top of Nginx.
[2893.94 → 2896.26] And using Lua, of course, it was written entirely in Lua.
[2896.60 → 2901.52] So it just introduces the bindings to the internal Nginx objects and systems.
[2901.52 → 2907.14] So essentially, Kong is written entirely in Lua with Openest on top of Nginx.
[2907.66 → 2909.38] So it actually uses Openest?
[2910.08 → 2910.62] Yes, correct.
[2911.02 → 2911.34] Okay.
[2911.48 → 2915.86] I remember I checked out Openest a while back, and I thought it looked really cool.
[2915.98 → 2918.14] It was like a little bit too low level than what I needed.
[2919.52 → 2923.50] And I didn't necessarily need the performance at the time, but I thought, this is very interesting.
[2924.14 → 2927.14] I wonder if anybody's going to build anything interesting on top of it.
[2927.20 → 2928.54] So it's kind of funny to find out.
[2929.06 → 2929.52] Here it is.
[2929.52 → 2931.20] It's still actively developed, I assume.
[2931.34 → 2934.14] And here it is sitting inside of Kong.
[2934.48 → 2939.56] One of the actually a number of the core Openest contributors are also contributors to Kong as well.
[2940.10 → 2945.04] So that's kind of a validation as well for what we're doing in terms of going in the right direction.
[2945.60 → 2948.24] And generally speaking, the DevOps community and the IT community,
[2948.24 → 2952.18] that's usually been more of where the HTTP server management lies,
[2952.18 → 2956.44] as opposed to developers who are going to dive in and script or configure Nginx.
[2956.44 → 2960.00] The Lua adoption is already the highest there is.
[2960.12 → 2962.90] So everybody's on that train, I guess.
[2963.70 → 2972.32] And recently, some people might be aware that Nginx actually announced that they're adding JavaScript as a scripting layer to Nginx,
[2972.64 → 2977.10] which was met with a lot of raised eyebrows and confused looks.
[2977.20 → 2978.42] Some consternation, yeah.
[2978.42 → 2983.88] Yeah, I think, I don't know if it's really a trend of, hey, lets JavaScript all the things.
[2984.10 → 2984.66] Don't get me wrong.
[2984.74 → 2985.82] I'm a fan of JavaScript.
[2986.16 → 2988.84] But I don't really understand fully their motivations.
[2989.16 → 2991.78] And I didn't actually get to speak to them at all recently.
[2991.78 → 2994.52] So I want to have that conversation with them just to understand it more.
[2994.52 → 3004.56] But the early feedback from the community trying the beta of Nginx with JavaScript was that the performance was just simply not there.
[3005.16 → 3010.72] And we're talking about 100x performance differences between scripting something with Lua versus doing it with JavaScript.
[3011.56 → 3015.04] And that's probably because they're doing their own virtual image as well.
[3015.20 → 3020.04] It's not exactly JavaScript because it's missing a lot of the ECMAScript standards and specs in there.
[3020.04 → 3024.10] So I'm sure they're going to get there, and they're going to make more improvements on it.
[3024.20 → 3031.74] So if Nginx and JavaScript becomes more of the standard and a better performance one, that is, which is the most important thing for us,
[3032.02 → 3035.06] then, of course, you'll see JavaScript make its way into Kong as well.
[3036.36 → 3036.66] Huh.
[3037.76 → 3039.30] So at the plugin layer?
[3039.72 → 3040.16] Yeah.
[3040.36 → 3043.62] Or as actually cutting over to JavaScript for codes?
[3043.98 → 3048.90] I think more likely at the plugin layer because, you know, with Openest, we've got a good solid foundation.
[3048.90 → 3049.22] Yeah.
[3050.04 → 3056.40] But the idea that people can come in and write their own plugins, which they can already do in Lua, although, you know, not everybody is familiar with Lua.
[3056.82 → 3059.24] So JavaScript just bridges that gap a little bit.
[3059.62 → 3069.88] I can definitely see why the Nginx people would want to add JavaScript just from a, you know, just from a perspective of adoption and use of the scripting side of Nginx, making it more powerful for more people.
[3070.00 → 3070.36] Absolutely.
[3071.00 → 3077.16] That being said, I've looked at Lua when I was checking out Openest and stuff, and it seems like it's a really nice little language.
[3077.16 → 3082.18] It doesn't seem like the hurdle to learn it and get started would be too much to jump over.
[3082.30 → 3083.24] How do you feel about that?
[3083.24 → 3088.44] It was a hurdle for me to jump over it just to get going into it.
[3088.44 → 3098.74] But once you recognize some of the similarities to other languages, and it's really just the syntax at the end of the day, that's kind of true to all scripting languages and high-level languages.
[3099.10 → 3102.92] If you're familiar with a high-level language, then it's not hard to jump to another high-level language.
[3103.30 → 3106.48] If you're familiar with a scripting language, it's not hard to jump to another scripting language.
[3106.48 → 3115.24] It's usually the cross-reference there where it becomes a bit more complicated, where somebody has been doing C Sharp or Java and wants to do JavaScript or Lua.
[3115.50 → 3117.36] They find that a little bit jarring.
[3117.90 → 3123.28] But once they get over it, then they realize they're not going to get the nice things that they have in Java or C Sharp.
[3123.78 → 3125.14] Then they can start actually being productive.
[3125.62 → 3134.38] Let's talk about another technology choice when it comes to dependencies, aside from Nginx, of course, is you have a hard dependency on Cassandra.
[3134.52 → 3135.16] Can you talk about that?
[3135.16 → 3144.14] Yeah, so as I was saying earlier, one of the marketplace kind of challenges is because we had to proxy everybody's API calls,
[3144.56 → 3152.32] a lot of people serve APIs and have their servers in locations that are in the world that may or may not be close to where our servers were.
[3152.84 → 3154.32] So network latency became a problem.
[3155.12 → 3158.36] And the solution with that was to basically deploy across multiple regions.
[3158.88 → 3162.34] And we are hosted on AWS, so we wanted to be on all the AWS regions.
[3162.34 → 3167.72] We literally have people sending traffic from every region in AWS around the world.
[3168.20 → 3169.96] So it made sense for us to be there.
[3169.96 → 3185.48] So the challenge there was, of course, in the case for monetized APIs especially, is they monetize usually based on number of API calls or certain data being sent or anything else that they want to monetize on.
[3185.48 → 3197.24] But what happens if you have a data centre far in the east and another data centre far in the west and a user making API and the same user making calls to your API from both of them?
[3197.24 → 3204.62] Say a user or, sorry, a consumer built a mobile application and that mobile application became popular and now people around the world are using it.
[3205.10 → 3208.58] You want to charge the developer of that mobile application according to their usage.
[3209.12 → 3212.04] But his users, his end users are all over the world.
[3212.18 → 3215.46] So the traffic is not always coming from the same direction or the same source.
[3215.46 → 3227.62] So the challenge of keeping these servers in sync became a bit of a problem to solve, architecturally speaking, as well as a cost centre for us.
[3227.62 → 3236.18] Because now we have to invest a lot, not only in engineering solution, but also maintaining that solution and scaling it up as the system grows.
[3236.18 → 3246.10] So Cassandra just became kind of the natural choice for that because it was a database that was designed from the ground up to solve that problem.
[3246.20 → 3253.48] So my problem of concurrency to solve that problem of clustering and multiple regional data centre data sharing.
[3253.70 → 3256.24] So you can solve that problem with Postgres.
[3256.36 → 3259.80] You can solve that problem with MySQL or any other databases.
[3259.80 → 3271.30] But it's typically a bigger investment for you to go and try to solve that with, let's say, Postgres and deal with sharding and deal with distribution of data and deal with syncing of data.
[3272.08 → 3274.46] So we research a lot of databases.
[3274.78 → 3276.04] We experimented a lot of them.
[3276.22 → 3280.48] And Cassandra just was one of the kind of easier choices.
[3280.48 → 3290.38] And we also had to consider a developer experience of somebody, especially for the Kong side of it, who will just want to be able to run Kong and get started in five seconds.
[3290.38 → 3291.34] What are they going to have to do?
[3291.72 → 3293.98] So we didn't want to choose something that was too complex either.
[3295.28 → 3297.06] And Cassandra became the obvious choice.
[3297.72 → 3308.80] Again, just as with the Lua and the kind of the unopinionated architecture that we did, kind of placed both to the benefit and to kind of intimidating newcomers.
[3308.80 → 3314.44] Somebody who's not familiar with Cassandra as a database choice might find it a little bit more intimidating to grab their head around.
[3315.38 → 3321.36] My example of that I always go back to, it's kind of the same thing as when people were moving from subversion to Git.
[3321.68 → 3330.28] This idea of a decentralized system is just so bizarre and out there for somebody who's always used to having the central point of truth.
[3330.28 → 3341.34] Same way as you would have an SVN versus Git, it's the same that you would do with SQL-based databases and relational databases and what Cassandra has to offer and decentralized databases have to offer.
[3341.88 → 3357.30] So the same kind of effort that a lot of developers go through in crossing that bridge is probably the same experience they've had in switching from SVN to Git or, you know, decentralized or from centralized version control to decentralized version control as we all did over the years.
[3357.30 → 3360.06] So you have dependencies on Cassandra.
[3360.34 → 3361.66] That does seem to make some sense.
[3361.80 → 3364.30] You have Nginx, of course.
[3364.70 → 3371.10] But as far as what this will run on, sounds like any, you know, Star nix system.
[3371.66 → 3372.66] Yeah, pretty much everything.
[3373.74 → 3375.70] Anywhere that Nginx would run, basically.
[3375.70 → 3390.66] And, you know, to the point about Cassandra, now that Kong is established, and it's out there and people are using it, one of the most popular issue on the GitHub project is to add support for Postgres.
[3390.66 → 3400.62] So we are actually doing that and that's going to be coming in the next couple of months to add support for Postgres and other SQL relational databases.
[3401.08 → 3406.18] Obviously, with the caveats of you're going to be worried about your own distribution and so on.
[3406.24 → 3408.58] But the reality is not everybody has to solve that same problem.
[3408.84 → 3408.90] Right.
[3408.90 → 3412.74] So for many people, it's just they're using Kong internally only.
[3412.84 → 3414.90] They don't even need to expose it to external users.
[3415.22 → 3417.22] They just want to use it between their own internal systems.
[3417.68 → 3422.72] So, you know, a simple Postgres database would solve that problem for them just fine.
[3423.00 → 3423.22] Right.
[3423.38 → 3425.34] No, I think that's a pragmatic choice.
[3425.44 → 3430.20] I think you can kind of liken that to what we just talked about with Nginx, you know, adding JavaScript, scripting support.
[3430.64 → 3435.28] It's just to make a great tool available to a broader group of people.
[3435.28 → 3440.18] You know, when I see Cassandra as a dependency, just the messaging and my knowledge of that database.
[3440.70 → 3446.06] And I think this is probably not a tool for me because Cassandra solves problems that I rarely have.
[3446.12 → 3446.46] Exactly.
[3446.66 → 3449.98] As a contract developer working for small businesses and startups.
[3451.46 → 3456.38] And so that's just like an implicit message that goes out.
[3456.64 → 3460.30] Like, oh, this is for people with big data, you know, quote unquote problems.
[3460.30 → 3465.52] Um, and I think adding Postgres support is a pragmatic choice and that's, that's pretty cool.
[3466.12 → 3468.84] Um, tell me about the plugin architecture.
[3469.20 → 3470.44] It's plugin oriented.
[3470.70 → 3476.58] You guys provide a bunch of first party plugins, ones we discussed, such as authentication and rate limiting and such.
[3476.80 → 3479.26] How do the plugins work, and how do you write them yourself?
[3479.26 → 3490.96] So the plugins are essentially, uh, in the simplest terms, they're just, uh, events and part of the request lifecycle that, uh, operate custom code that you write or the ones that we package with the system.
[3490.96 → 3500.88] So, you know, we talked about a lot about the authentication plugins, but there are many other plugins in there, including things like rate limiting, uh, request size limiting or transformations.
[3500.88 → 3506.36] They can modify the request and response, uh, logging plugins in case you want to write logs to files.
[3507.00 → 3519.40] Essentially what they do is in the request lifecycle, you have a number of events, uh, to simplify that you have pre, pre, uh, request received, uh, and then request sent and then response received and response sent.
[3519.54 → 3522.96] You know, these are the four major events that you would probably want to listen to.
[3523.04 → 3527.32] There are more like first header received from the upstream and so on.
[3527.32 → 3540.52] So you essentially subscribe to events and the request lifecycle and, uh, your, your, your plugin logic will trigger at, at that point of the event request lifecycle and, you know, do whatever the custom logic that you've written in the plugin to do.
[3541.52 → 3551.12] So many cases, the authentication methods, these trigger as soon as the request has finished processing into the Kong layer, but before it was sent to the upstream server.
[3551.32 → 3552.68] So that's when you do the authentication.
[3552.68 → 3561.56] And then if everything is good and well, you just continue down the lifecycle and process other plugins' logic, or just send it to the upstream, receive the response back.
[3561.66 → 3572.76] And then perhaps, and then at the end of the receipt, the receiving of the response, that's when you'd run the logging plugins, for example, because you want to log the entirety of the request lifecycle, not just part of it.
[3572.88 → 3574.42] So it really is event based.
[3574.42 → 3578.76] And depending on the lifecycle of the request is where you can introduce logic into the flow.
[3578.76 → 3588.00] One of the best parts about open source is when, you know, some person you'd never met before comes along and makes your software better.
[3588.50 → 3596.90] You know, best of all, if you're sleeping, and you wake up and, you know, and you have a pull request where, oh man, my project's better than it was when I, before I went to sleep.
[3596.90 → 3601.08] It seems like you guys have a lot of pull requests open on Kong.
[3601.18 → 3611.58] Have you guys had any awesome plugins that were created by third parties that you'd like to highlight as like, oh, this is something that either we didn't think of, or we're glad some other third party came along and wrote this plugin?
[3611.58 → 3623.18] Yeah, we're actually, so, you know, like I said, we have the first party plugins that we created, and then we have third party plugins for our own products as well, because we have more products than just Kong.
[3623.30 → 3628.52] We do offer Galileo, which is our API analytics service and Gelato, which is our developer portal service.
[3629.02 → 3631.56] We have those also as plugins in the system.
[3631.56 → 3642.86] But like you said, we have a developer community that's actually quite active from the day we launched, which was, I think it's about eight months ago now.
[3643.44 → 3648.90] In the first three months, we just went on Hacker News and everybody ended up posting about it everywhere.
[3649.42 → 3656.34] And within the first couple months, we, like the star count on our GitHub repo, whether you think that means anything or not, went up to like 2,000 stars.
[3656.76 → 3659.92] I think now it's at around 3,500 stars or something like that.
[3659.92 → 3665.02] And people started coming in and actually started reading about it and contributing to it.
[3665.12 → 3669.20] And then initially, they highlight all the things we did wrong.
[3669.30 → 3671.74] So they're like, oh, your documentation here is wrong.
[3671.94 → 3675.16] You mislabelled this thing, or you have an issue here.
[3675.58 → 3678.94] And that's where, you know, initially the feedback from the community ends up being.
[3679.06 → 3687.26] But then slowly over time, we're seeing a lot of the things people are building on top of Kong for their own use cases within their own corporations and businesses, of course.
[3687.26 → 3694.60] And I think in the next couple of months, we're going to be announcing a number of third-party integrations and services that are being built on top of Kong.
[3694.74 → 3704.44] Obviously, the reason we're having this conversation is that the guys at Max CDN are looking at it, and they're building kind of plugins and services that benefit Max CDN users and Kong users.
[3704.44 → 3708.14] We have Run Scope building plugins.
[3708.38 → 3709.24] We have Datadog.
[3709.34 → 3720.66] We have a number of this kind of tooling and service providers around the world that kind of fit the same target audience of API tooling and providers who are building all these products and plugins to Kong now.
[3720.78 → 3725.46] So I think in the next couple of months, you're going to see a lot of these third-party plugins start to surface.
[3726.32 → 3729.82] And I think it's going to be pretty exciting for us to see those go out there.
[3729.82 → 3730.22] Awesome.
[3731.30 → 3734.18] Yeah, it looks like you also have a Nginx plugin.
[3734.76 → 3736.62] Yeah, we have Nginx.
[3737.60 → 3741.08] Nginx Plus is a premium service from Nginx, too.
[3741.76 → 3744.24] And it offers you monitoring access to Nginx.
[3744.32 → 3745.66] So that's also available on Kong.
[3746.38 → 3752.80] And I was going to say, one of the things people always end up rebuilding is a GUI interface for Kong.
[3752.94 → 3756.44] Because Kong, like I said, its only interface is an API.
[3756.44 → 3774.66] So people are actually, there's like one, two, three, four, five, six frontends to Kong that people have built across all the different frontend frameworks, whether it's Angular or Python or Node.js or anything else they started building with.
[3775.10 → 3784.48] Are you going to bring those in and have some sort of like some frontend death match and then announce one as the canonical blessed mash ape frontend?
[3784.48 → 3785.98] Or what's going to happen there?
[3785.98 → 3787.50] We're actually working with all of them.
[3787.86 → 3793.04] We're seeing a lot of things people are building with Kong that are quite innovative and interesting.
[3793.48 → 3802.20] There's actually a company in Belgium that's building kind of a multi-tenanted API directory on top of Kong as well.
[3802.78 → 3803.98] And they're open sourcing that.
[3804.10 → 3809.48] There's all these GUIs that people are building and the frontends that people are building that we're just encouraging them to build.
[3809.48 → 3810.80] I don't think we're going to have a death match.
[3811.30 → 3818.10] But we do every once in a while nudge them and say, hey, you know, that other guy has implemented this new features and you haven't.
[3818.22 → 3819.00] Maybe you should take a look.
[3819.96 → 3823.48] That's the entrepreneur in you again saying, you know, bringing out the competition.
[3824.48 → 3824.74] Yeah.
[3824.74 → 3826.50] Just to make everybody better.
[3826.62 → 3828.34] A little bit of public shaming doesn't hurt anybody.
[3830.66 → 3833.06] And people are building integrations with it.
[3833.10 → 3836.20] And that's really exciting to see because it's things we haven't thought about.
[3836.42 → 3839.30] And that's why we want it to be open source.
[3839.36 → 3840.56] And that's why I love open source.
[3840.70 → 3842.02] Just to get that.
[3842.02 → 3845.28] Like you said, you wake up in the morning, and you see the surprise, and it's like, wow, this is cool.
[3846.34 → 3846.40] Yeah.
[3846.44 → 3849.10] Let's talk briefly about the open sourceless of this.
[3849.46 → 3856.06] You know, the difference between personal projects and business projects is an open source business project has to justify its existence.
[3856.88 → 3862.24] Obviously, if this was a proprietary thing, the existence could be, well, we'll sell this to people and make money.
[3862.90 → 3867.40] What's the business oriented decision from Mash Ape to open source?
[3867.40 → 3873.40] You touched on it briefly, but if you could, you know, restate that and give like, where does this fit into Mash Ape as a company?
[3873.94 → 3877.00] So, like I said, Mash Ape as a company, we have a number of products and services.
[3877.24 → 3878.18] We have the API marketplace.
[3878.76 → 3881.52] We have API analytics product called Galileo.
[3881.64 → 3887.06] We have a developer portal product called Gelato and a few other products as well.
[3889.76 → 3892.50] Open source has been in our DNA from the start.
[3892.50 → 3901.16] We even have a product called Unrest, which is not really a product, but just a series of open source HTTP client libraries.
[3901.62 → 3902.52] They're actually quite popular.
[3902.80 → 3907.20] The Node.js one gets about a million downloads a month or something.
[3907.38 → 3910.52] And the PHP one gets about 30,000 downloads a day.
[3911.54 → 3916.34] We enjoy building open source as part of being developers and engineering driven as a company.
[3917.42 → 3920.08] And, you know, we have a number of things.
[3920.08 → 3922.40] I can't even remember half the open source projects that we maintain.
[3923.06 → 3929.74] But as a product strategy, we obviously are not the only company in this space.
[3929.82 → 3931.98] We're not the only ones that offer API tools and services.
[3932.14 → 3933.20] There are many others.
[3933.84 → 3937.86] The reality is, though, when you look at all these other providers and services out there,
[3938.36 → 3944.48] they are, even some of them do have some open source into them, but they're not fully entirely open source.
[3944.66 → 3946.40] What they do, they just want your paycheck.
[3946.40 → 3959.36] So when you have a conversation with them about using their products and tools, they basically want hundreds of thousands of dollars to millions of dollars based on your usage and based on how your API is or how big your company is.
[3959.40 → 3960.70] They just want to bleed you for money.
[3960.70 → 3969.40] And because of our individual teams kind of backgrounds coming from the open source world and coming from kind of bootstrapping and building things on your own and being entrepreneurial,
[3970.12 → 3981.46] most of us don't think of the software world as the way to make billions of dollars out of companies of just, you know, bleeding them for money for buying your product or using your service.
[3981.46 → 3991.02] So in open source and Kong, we're basically saying, hey, look, this kind of tools are not the kind of tools that we should charge the community money for.
[3991.10 → 3995.14] These are not the kind of tools that people should be paying hundreds of thousands of dollars for.
[3995.30 → 3996.04] These are commodities.
[3996.24 → 3998.88] These are part of the necessities for building API products.
[3999.14 → 4003.00] If you want to make money and monetize things, then monetize based on services.
[4003.50 → 4005.66] Monetize based on value add you're adding to people.
[4005.66 → 4008.72] The reality is all of our clients are developers too.
[4009.18 → 4015.10] And there's nothing stopping our developers and our clients of going on and building their own API management solution.
[4015.64 → 4016.14] They can.
[4016.74 → 4021.98] The question is, do they have the time and the energy to invest in building something like that for their own needs?
[4022.08 → 4022.98] And many people do.
[4023.62 → 4031.64] But the reality is their real focus of a development team is to solve problems of the product or solve problem of their own consumers or their own clients.
[4031.64 → 4039.58] So for us, open sourcing the HTTP management and the API management layer just made sense because it is a commodity.
[4039.78 → 4045.88] It's not something that people should be charging enterprise level contracts with and paying hundreds of thousands of dollars for.
[4046.50 → 4048.28] So we just wanted to give it out for free.
[4048.60 → 4050.66] So you said the Kong Enterprise Edition.
[4050.82 → 4055.78] There's actually not a difference in what we call the enterprise service on Kong versus what Kong is.
[4055.84 → 4056.64] It is the same product.
[4056.76 → 4057.34] It's open source.
[4057.42 → 4057.76] It's free.
[4057.88 → 4058.88] There are no strings attached.
[4058.88 → 4061.26] You can use it today in production or in development.
[4061.94 → 4062.58] We don't care.
[4062.70 → 4063.14] Have fun.
[4063.24 → 4063.76] Enjoy it.
[4063.84 → 4066.86] Let us know what problems you have, and we'll help you with it.
[4067.12 → 4069.52] But what we do offer is the value add.
[4069.70 → 4078.22] So the value add that we think people want for open source products is more around the support and more around customization, more around professional services.
[4078.22 → 4086.40] So for a bigger company or a bigger team, they might have a production system running on Kong and many people do.
[4086.40 → 4099.86] They come to us, and they say, look, we just want to have you in kind of our production level environment so that if something happens or if we need your help with something or there is a demand to change things on the fly.
[4100.86 → 4109.36] But instead of managing the relationship and maintaining this product internally with our teams, we'll just have your team come and be part of maintaining the product and helping us answer questions.
[4109.36 → 4114.56] So it becomes a support relationship for people in a higher production kind of standards and requirements.
[4114.74 → 4126.12] At the same time, there are a lot of people who may or may not need or want to invest into Lua or customization, or they just may not have the time.
[4126.22 → 4128.00] They have other priorities to focus on.
[4128.30 → 4135.02] So if they really need to have something customized or something developed for their own needs, that's where they engage us for the kind of professional services' aspect.
[4135.14 → 4138.18] So we can come in and help them with the integration or the customization of the product.
[4138.18 → 4146.36] And to us, that's providing value to our customers rather than putting a barrier in front of their adoption of saying, no, no, no, you need to pay for this before you use it.
[4148.26 → 4150.58] I think that's a good place for a break.
[4151.10 → 4154.60] On the other side, we will talk about getting started with Kong.
[4154.68 → 4160.26] I also want to ask about future roadmaps and where Kong could be going in the future.
[4160.44 → 4160.86] Stay tuned.
[4160.98 → 4162.80] We will talk about that on the other side of the break.
[4162.80 → 4168.34] I have yet to meet a single person who doesn't love DigitalOcean.
[4168.56 → 4171.66] If you've tried DigitalOcean, you know how awesome it is.
[4171.96 → 4178.42] And here at the Changelog, everything we have runs on blazing fast SSD cloud servers from DigitalOcean.
[4178.42 → 4184.08] And I want you to use the code Changelog when you sign up today to get a free month.
[4184.42 → 4190.34] Run a server with 1 gig of RAM and 30 gigs of SSD drive space totally for free on DigitalOcean.
[4190.58 → 4192.52] Use the code Changelog.
[4192.74 → 4194.92] Again, that code is Changelog.
[4195.24 → 4196.86] Use that when you sign up for a new account.
[4197.26 → 4200.94] Head to DigitalOcean.com to sign up and tell them the Changelog sent you.
[4200.94 → 4209.64] All right, we're back, and we're ready to wrap up this conversation about Kong.
[4209.80 → 4217.08] But we do need to know how the heck do you get started with it if it's something that is interesting to you?
[4217.08 → 4218.48] So you've sold me.
[4218.58 → 4219.76] I'm interested in Kong.
[4219.84 → 4222.02] I want to try it out.
[4222.12 → 4222.56] What do I do?
[4222.58 → 4223.24] What are my first steps?
[4223.24 → 4232.08] So first step is you go to getkong.org or simply go to mashhape.com and find the link to Kong from there.
[4232.94 → 4237.56] The website will provide you linkage to the GitHub repo and everything else about the documentation.
[4237.92 → 4242.26] But just if you already know what you want to do beyond learning about what Kong does,
[4242.68 → 4246.58] we actually offer a number of distribution packages for a number of Linux distros.
[4246.58 → 4252.96] So depending on what Linux distribution your server runs on, you can actually download it for Debian, CentOS, Red Hat, and so on.
[4253.22 → 4256.36] We even offer a CloudFormation template for AWS users.
[4256.76 → 4261.88] We even offer an AMI for AWS users as well if they don't want to build servers from scratch.
[4262.42 → 4268.96] And we even offer Voucherized versions of Kong and Cassandra as well that you can just simply run with two command lines.
[4269.02 → 4271.36] And that's actually what I use most of the time for my development purposes.
[4271.90 → 4274.74] I just run the Voucherized version locally and just go from there.
[4274.74 → 4282.12] And we're also working, and then if you want to develop for Kong and build your own programs and run it locally,
[4282.30 → 4288.64] then we actually have full instructions of how to run the source and run it within Vagrant as well for Windows users
[4288.64 → 4291.66] because Nginx doesn't run just natively on Windows.
[4292.64 → 4294.38] That's it, man. It's as easy as that.
[4294.58 → 4295.48] It's super easy.
[4296.74 → 4297.88] That's what we like to hear.
[4297.88 → 4305.96] Looks like you don't yet support DigitalOcean, Heroku, Microsoft Azure, but these things are coming soon.
[4306.16 → 4306.72] FreeBSD.
[4307.00 → 4308.00] We do support them.
[4308.26 → 4310.50] Obviously, DigitalOcean runs on Debian too.
[4311.58 → 4315.96] And Azure as well gives you a Debian-like system that you can set up with Linux and everything.
[4316.12 → 4317.02] So we do support them.
[4317.16 → 4324.32] But what we want to do is just automate that process and having kind of the one-click launch scenario that we've done for AWS.
[4324.32 → 4329.14] So if you look at the CloudFormation example, you go to the CloudFormation page on the installation page,
[4329.24 → 4332.84] and you literally click a button, and it takes you to a form on AWS side.
[4333.00 → 4334.60] You fill it up, and then your servers are launched.
[4334.82 → 4339.84] So that's what we're actually aiming to do with the Google Cloud Platform and Azure and DigitalOcean as well.
[4340.36 → 4341.00] I see.
[4341.08 → 4343.48] So you have a little flag there, banner, that says soon on those.
[4343.56 → 4345.80] That's because you haven't fully automated the process yet.
[4345.96 → 4346.30] Correct.
[4346.48 → 4352.64] But typically speaking, almost all the cloud providers have either Debian or CentOS, and we do have those.
[4352.64 → 4353.60] So you're good to go.
[4354.40 → 4355.76] Let's talk about the status of Kong.
[4355.88 → 4357.58] Production ready, I assume.
[4359.30 → 4360.52] API finished?
[4360.60 → 4362.16] Is it still under heavy development?
[4362.46 → 4363.54] Do you have multiple rounds?
[4363.60 → 4364.48] What's your future plans?
[4364.58 → 4365.28] Where it's at right now?
[4365.48 → 4367.02] So it is production ready.
[4367.14 → 4369.06] We are using it ourselves in the marketplace.
[4369.46 → 4376.22] And many of our customers, including governments and financial institutions and healthcare providers, are using it in production.
[4376.22 → 4385.90] And obviously, we have an ongoing relationship with these customers to make sure we get their feedback and learn from them and incorporate all these learnings into the product as well.
[4385.90 → 4390.30] So just because it's an open source product, it's not one of those side project things.
[4390.48 → 4393.08] We actually have a full team dedicated and working on Kong.
[4393.62 → 4394.34] Myself included.
[4394.50 → 4396.90] A lot of our engineers are working on it day and night.
[4396.90 → 4402.40] So it is really, even though it's an open source project, it's also a core product that we offer.
[4402.40 → 4405.62] So people are working on it all the time and adding new functionality and features.
[4405.76 → 4413.00] In terms of roadmap and the next releases and what we're aiming to do, right now, Kong nodes are kind of stateless.
[4413.42 → 4421.00] So they rely heavily on Cassandra to kind of share the state and share the information across them, specifically for information about the APIs and the configuration.
[4421.68 → 4425.34] In the next release, we're adding cluster awareness for the Kong nodes.
[4425.34 → 4428.58] So each node in the Kong cluster would be aware of all the other nodes.
[4428.86 → 4443.80] And when events happen in the system, like an invalidation of the cache event, the nodes can talk to each other and invalidate each other's caches or reset each other's caches, which makes the system even more dynamic and introduces more kind of functionality for building plugins and features across it.
[4444.96 → 4452.40] Beyond that, like I said earlier, we're introducing PostQuest as well as a database choice for developers and people who want to run PostQuest in production.
[4452.40 → 4456.70] And we actually try to publish our wiki and roadmap.
[4457.48 → 4460.30] Sorry, we try to publish our roadmap in our wiki on the GitHub repo.
[4461.18 → 4471.02] But typically, it's always changing and evolving because the more people who discover Kong and the more people who come and look at the Kong project, they end up contributing back in issues and questions and feedback.
[4471.28 → 4476.30] So we have kind of two main channels for talking to our community, which is the GitHub issues, of course.
[4476.62 → 4480.52] And then we have a Gitter channel for live chat with our community.
[4480.52 → 4484.78] And really, the community is the one that drives our roadmap.
[4485.52 → 4490.90] We don't actually go behind closed doors and say, OK, here's what we think we're going to do and what we think the community wants.
[4491.12 → 4495.48] We actually just look for the community for guidance and feedback of what they want, what they need.
[4495.74 → 4502.58] And of course, depending on how loud people are to certain issues and certain requests, then that just takes higher priority than others.
[4502.58 → 4512.80] So if you look at the Postgres issue in our GitHub repo, I think there's something around a couple of hundred plus ones on the issue because people just keep on going.
[4512.96 → 4513.68] It's like, yep, plus one.
[4513.76 → 4514.16] I want this.
[4514.86 → 4518.96] And so that obviously became a higher priority because clearly there's a lot of demand for it.
[4519.02 → 4520.68] And that's how we actually drive our roadmap.
[4521.22 → 4527.64] We look at people and what they're building and what they want to build, what's lacking, what's limited, what needs to be expanded on.
[4527.64 → 4531.30] And we prioritize accordingly and just do it by the community's feedback.
[4532.68 → 4540.34] Well, let's cut straight to the chase and talk about when is GitHub going to implement upvoting and downloading on their issues?
[4540.58 → 4542.42] I mean, come on, the plus ones are ridiculous.
[4542.98 → 4549.90] There is a GitHub plugin called Zen hub, which kind of gives you the Trello view of GitHub issues.
[4549.90 → 4555.14] It actually has a dedicated plus one button that kind of superimposes on GitHub issues.
[4555.26 → 4560.84] So you can just do that instead of people coming in and manually typing in plus one into the issues.
[4561.20 → 4562.54] So I find that always funny.
[4562.92 → 4563.46] Zen hub, huh?
[4563.72 → 4565.32] Yeah, it's a cool tool to use.
[4565.48 → 4566.48] I'd highly recommend it.
[4567.10 → 4567.28] Yeah.
[4567.36 → 4570.80] So tell GitHub, if you're listening, hire the Zen hub guy.
[4571.34 → 4571.58] Yeah.
[4571.72 → 4573.36] They'll implement your plus one feature for you.
[4573.52 → 4574.06] That's right.
[4575.06 → 4575.82] Very cool.
[4575.82 → 4585.68] So we're about to move on to our closing questions, but any closing thoughts for you on Kong or Mash ape as we transition to the closing questions?
[4586.34 → 4587.40] Anything else you want to say?
[4587.98 → 4594.64] The one thing I would say is, you know, kind of building on that community relationship is that, you know, Kong is an open source product.
[4594.96 → 4598.06] And obviously we're championing it as the company behind it.
[4598.18 → 4605.02] But we also want people to be more engaged and get and be more involved so that, you know, we're not just the only ones building it.
[4605.02 → 4610.74] We already have a number of contributors, a number of people in the community who are actively building and introducing things to the product.
[4610.96 → 4612.06] But we want to hear from you.
[4612.16 → 4616.08] We want to hear from even the people who don't like it, even the people who don't want to use it.
[4616.36 → 4617.68] I'd love to have that conversation.
[4617.80 → 4625.52] I'd love to see, you know, what is the feedback that, you know, you saw on the product or the information that doesn't really fit your needs.
[4625.58 → 4631.30] I want to learn from the community as much as I want to share the knowledge and learning that we have as an API company to the community as well.
[4631.30 → 4634.76] So I would encourage anybody to jump in and, you know, give us feedback.
[4634.98 → 4635.96] Talk to us on the chat.
[4636.48 → 4638.54] Open issues for anything that you think is lacking.
[4638.84 → 4644.16] Or just, you know, email us in the chat or go for coffee and talk about APIs and technologies in general.
[4644.30 → 4648.20] Because we're all API nerds at Misshape, and we love talking about this stuff all the time.
[4649.00 → 4649.52] All righty.
[4649.52 → 4650.84] Well, closing question time.
[4651.28 → 4659.84] And the compulsory question that we just love to ask everybody is, who is your programming hero and why?
[4659.84 → 4662.26] All right.
[4662.60 → 4668.12] I don't have to think too much about that because I always quote this person all the time.
[4668.30 → 4680.96] So my programming hero is Grace Hopper, who, if you're not familiar with who that is, it's, it was, she was back in the, in the US Navy, one of the early programmers back there.
[4680.96 → 4690.72] And she's usually credited for creating or inventing the word debugging and kind of reference to what we do today in debugging programs and applications.
[4692.64 → 4699.70] Although there's also the other story of how the encryption, back in the days of earlier, the war and encryption, there was an actual bug in a system.
[4699.70 → 4706.58] Um, that's, that's where the word bug came from, came from, but the word debugging, uh, kind of came from Grace Hopper.
[4706.66 → 4708.00] And that's usually what she's credited for.
[4708.10 → 4714.34] But what I love her the most for, and the more I learn about this person, the more amazing she, she becomes in my mind.
[4714.34 → 4718.68] Um, is the one quote that I actually just found by Hab stance.
[4718.84 → 4724.58] And then I got to know more about Grace Hopper is, um, the quote about management and leadership.
[4725.14 → 4730.30] And, uh, the famous quote basically says, you manage things, you lead people.
[4730.60 → 4741.32] And that was kind of in context of how in the software development culture that we have today, we have developer managers, we have product managers, we have project managers.
[4741.32 → 4750.88] And, you know, in a broad sense, those kinds of people are generally tasked with the purpose of managing the developers or managing the technologists on their teams.
[4751.42 → 4762.08] But, you know, to a big failure and to lack of, uh, love from development team, they just don't like that relationship and ends up being a poisonous relationship in a lot of ways, not always.
[4762.08 → 4771.52] But generally speaking, that's kind of the core part of it is because the idea of managing things or being responsible as a person to manage things doesn't translate well to human beings.
[4771.80 → 4774.84] But if you want to be a leader, then that's a different conversation altogether.
[4774.84 → 4783.50] And the reason that kind of rang true to me, because in my career, I kind of evolved from, uh, you know, different roles and responsibilities along the way.
[4783.62 → 4793.18] And in many places, you know, my role was always been the development manager or the team lead or, you know, the manager kind of suffix always made it's way through to the title.
[4793.18 → 4805.82] And although I don't actually think of myself that way, I used to think that used to be a skill that I had because the business owner or my bosses would come to me and say, oh, we seem to have a good business lingo and understanding of the business.
[4805.82 → 4809.08] And you can talk to us like normal, and we can understand you.
[4809.14 → 4813.58] But at the same time, you go and talk this geeky language with the developers, and they understand you.
[4813.76 → 4816.12] So, you know, you seem to make a good manager.
[4816.72 → 4818.66] And I used to think that was a skill that I had.
[4818.76 → 4820.06] I used to think that was a positive thing.
[4820.06 → 4832.44] But of course, over time, I realized that's actually not because it's not so much that I'm able to kind of bridge that gap between business language and technology and kind of the motivations of developers versus the goals of business.
[4832.62 → 4842.64] But it was just the lack of the business people or people who are the business owners to understand the motivations and the kind of culture of technologists and hackers and developers.
[4843.76 → 4845.84] So that's how I came across Grace Hopper.
[4846.00 → 4849.00] And, you know, keep reading more about her and what she did.
[4849.00 → 4852.56] And that quote just rings true to me all the time.
[4852.60 → 4854.00] And I use it everywhere I go.
[4854.12 → 4855.66] It's just you manage things.
[4855.70 → 4856.86] You don't manage people.
[4857.04 → 4857.96] You lead people.
[4858.12 → 4859.30] So that's kind of my mantra.
[4859.50 → 4861.40] I want to be a leader to my team.
[4861.42 → 4862.50] I don't want to be a manager.
[4863.28 → 4866.82] So my title right now is head of engineering, but it really means nothing.
[4866.96 → 4868.14] I don't care about the title.
[4868.26 → 4870.50] I care more about my role to the team.
[4870.54 → 4873.54] And my role is to lead the team and help the team accomplish things.
[4873.54 → 4878.50] Not so much look at hours and input and output and production of the team members.
[4879.62 → 4881.46] No, that definitely rings true to me.
[4881.54 → 4886.42] And I think, you know, I've been in the position to both manage and to lead in certain aspects.
[4886.74 → 4889.52] And I found that I'm very bad at managing people.
[4889.60 → 4895.28] I don't enjoy managing people because it does feel very much like their things.
[4895.28 → 4897.54] And it seems like it's demeaning.
[4898.28 → 4900.02] But leading on the other hand, that's appealing.
[4900.20 → 4901.90] That's something that's challenging.
[4902.02 → 4903.36] That's something that's way more attractive.
[4903.88 → 4907.52] Also reminds me of, you know, one of my pet peeves is what's up with human resources?
[4907.86 → 4911.36] And like the idea of like, do you have any resources for this project?
[4911.42 → 4913.50] It's like, these are humans we're talking about here.
[4913.58 → 4918.44] You know, I realize we need to formalize on some terms for, you know, for easy communications.
[4918.44 → 4920.28] But come on, can we just call them people?
[4920.28 → 4931.66] Well, to me, it's the whole lack of understanding of what motivates us as human beings, but even more as technologists, as hackers, as developers.
[4932.34 → 4940.48] Like we, I mean, I'm sure some people are in it for the money, but I highly doubt these people will make it far in a career in software technology.
[4940.48 → 4961.92] The majority of us, and, you know, I would, I'm going to make a statement and say, I think all real developers and programmers are in this industry because they enjoy the aspect of creating and innovating and changing things and challenging the status quo by going in and making a program or an application or a product that solves people problems and changes the world around you.
[4962.04 → 4963.70] That's really what we are doing it for.
[4963.70 → 4971.82] If it was, if we were doing it for the money, then we'd probably go to the law school or study medicine and just make a bigger paycheck there.
[4972.32 → 4973.86] But that's not what motivates us.
[4973.92 → 4978.34] What motivates us is that opportunity to change the world around us and be innovative in what we're doing.
[4978.42 → 4980.00] And technology gives us that opportunity.
[4980.94 → 4985.46] But for a lot of businesses, a lot of people on teams, they don't necessarily touch on that.
[4985.46 → 4998.26] So what you see is that's where like your post comment about human resources, they talk about, you know, let's incentivize developers by giving them pay raises or vacations or, you know, offsites and travel kind of budget.
[4998.80 → 5002.12] Yeah, that's kind of nice, but that's not really how you make a development team happy.
[5002.22 → 5010.26] That's not how you lead the development team and, you know, champion the team itself and what they're doing into building better products and better services.
[5010.26 → 5022.76] Yeah, tease up my next question pretty well there, which is if you weren't doing what you are doing, which is being a leader of development at Mash Ape and whatnot, what would you be doing?
[5024.42 → 5029.72] I can't even think about it because I wouldn't be happy in my life.
[5029.76 → 5030.38] I wouldn't exist.
[5030.38 → 5038.90] I like we're talking before we started recording when I'm done to work, I'm still sitting at my desk, and I'm still writing code because that's what I enjoy doing.
[5038.90 → 5048.74] And my wife often doesn't even know the difference between, you know, me being in work mode and me being in just hacking and doing open source project work because it is the same to me.
[5048.82 → 5053.80] And I love this industry because it actually gives me that opportunity to do the things I enjoy doing the most.
[5054.18 → 5063.64] Yeah, I think that's funny because we have a video series called Beyond Code that is a very brief interviews that we shoot at conference after parties.
[5063.64 → 5066.00] And we ask the exact same five questions to everybody.
[5066.00 → 5070.30] A couple of them are kind of like the closing questions like who's your programming hero is one that we ask.
[5070.74 → 5074.34] Another one that we ask, we ask it a little more pointedly than we ask this question.
[5074.50 → 5080.18] It's pretty close to the same question, which are we simply say, is there something else that you'd rather be doing?
[5081.04 → 5085.72] And I've been shocked at how many people say no to that.
[5087.30 → 5089.72] Almost everybody says, no, I love what I'm doing.
[5089.72 → 5092.08] You know, there's nothing else that I'd rather be.
[5092.54 → 5095.30] And people that don't say no, they usually interpret it locally.
[5095.30 → 5097.84] And they're like, you mean besides talking to you guys on camera?
[5098.00 → 5099.60] You know, they make that joke.
[5100.12 → 5112.22] But anybody who answers that sincerely about career, they pretty much all say no, which is, I think, a testament to how enjoyable the work that we do is.
[5112.22 → 5114.84] I don't find that surprising at all.
[5115.04 → 5119.14] I mean, yeah, I think it was surprising at first, but now it kind of like totally makes it's like obvious in retrospect.
[5119.68 → 5119.80] Yeah.
[5120.22 → 5134.28] I think one of the things, if I'm forced not to do what I'm doing today, if for some reason, let's say the developer community came around and decided that I'm not allowed to be in technology anymore, which would be very, very sad indeed.
[5134.28 → 5142.88] And the only other thing I can imagine myself doing is just spend as much time with dogs and animals as I can, because I just, I have a little dog and I love her.
[5143.26 → 5146.34] Her name is Ruby, not an association to the programming language.
[5146.70 → 5153.18] I'm not much of a Ruby fan, but I just, I got, because I never got a dog growing up.
[5153.24 → 5155.44] I never had that pet relationship growing up.
[5155.52 → 5158.44] So I only got a dog as an adult and I love it.
[5158.50 → 5160.72] And it just feels like a little kid again.
[5160.72 → 5169.26] So if there was one thing I would do other than this, it would just be spending more times with dogs and animals, maybe being a dog walker or just a dog caretaker.
[5170.78 → 5171.36] Very cool.
[5171.52 → 5172.86] Well, thanks so much for joining us.
[5172.96 → 5173.80] This has been a blast.
[5173.90 → 5177.70] I think Kong looks really cool, and I hope it has a lot of success in the future.
[5178.32 → 5179.92] Thanks for taking your time and joining us.
[5180.00 → 5182.76] We also want to thank everybody who helps make this show possible.
[5182.92 → 5185.48] Our listeners, our changelog members.
[5185.60 → 5188.26] We appreciate you a lot, as well as our awesome sponsors.
[5188.26 → 5190.64] This show could not be possible without these four sponsors.
[5190.72 → 5195.76] That's Code Ship, Braintree, Harvest, and DigitalOcean.
[5196.04 → 5197.12] They support us.
[5197.52 → 5198.78] We all should support them.
[5199.34 → 5200.54] Thanks so much, you guys.
[5200.76 → 5203.08] And until next week, let's say goodbye.
[5204.22 → 5204.68] Goodbye.
[5204.68 → 5204.76] Goodbye.
[5221.04 → 5221.46] Googles.
[5221.46 → 5221.96] Hands up.
[5221.96 → 5222.42] Goodbye.
[5236.72 → 5237.04] Dear.
[5237.04 → 5237.24] You.
[5237.24 → 5237.48] Bye.
