[0.00 → 15.32] welcome back everyone this is the changelog and I'm your host Adam stakowiak this is episode 158
[15.32 → 21.44] and on today's show we have Eric St martin and Brian kettle son joining us they are the organizers
[21.44 → 26.70] behind gopher con and if you didn't know the changelog is going on the road we're taking
[26.70 → 33.48] changelog films to Denver to cover gopher con so if you see us there cameras in hand make sure you
[33.48 → 39.26] say hello we're going to be there seeing how to everybody we can July 7th through 10th and we
[39.26 → 44.12] talked to Eric and Brian today about everything we could about gopher con what it takes to create an
[44.12 → 50.66] event like this the size the days the after parties the hack day the workshops and even their diversity
[50.66 → 55.88] program Eric and Brian care so much about the go community they created a diversity of scholarship
[55.88 → 61.52] support fund as part of gopher con so even if you're not going to the event you can support
[61.52 → 68.62] this scholarship fund to ensure diversity in the go ecosystem we're also shooting season three of
[68.62 → 73.76] beyond code at gopher con so if you'd like to participate check the show notes for details
[73.76 → 80.76] this episode is sponsored by code chip is a hosted continuous delivery service
[80.76 → 87.94] focusing on speed security and customizability you can set up continuous integration in a matter
[87.94 → 93.86] of seconds and automatically deploy when your tests have passed code chip supports your GitHub and your
[93.86 → 99.08] Bitbucket projects you can get started with code chips free plan today and should you decide to go with
[99.08 → 105.62] a premium plan you can save 20 off any plan you choose for three months by using our code the
[105.62 → 113.52] change log podcast again that code is the change law podcast head to code chip.com slash the change
[113.52 → 116.22] log to get started and now on to the show
[116.22 → 126.76] all right we got Eric Saint Martin and Brian kettle son joining us today the organizers behind
[126.76 → 132.98] gopher con uh if you don't know the change log is going to be at gopher con where work with Brian
[132.98 → 138.96] and Eric to film all sorts of stuff about gopher con this year so if you see us we'll likely be
[138.96 → 144.58] carrying cameras but say hello we want to say hi to everybody we can but Eric Brian how are you
[144.58 → 151.76] welcome to the show I'm doing great happy to be on yeah, thanks we also got jarred online as well and
[151.76 → 156.18] you know I know that I'm speaking for jarred when I say this, but we've been really excited about go
[156.18 → 161.86] yep talking about gopher con today we've had several shows on go we cover go pretty much every week
[161.86 → 166.86] and changed all weekly but jarred how excited are you personally about gopher con this year
[166.86 → 171.90] I'm excited for two reasons first I have dabbled in go so I'm excited to learn a little bit
[171.90 → 178.10] more I do have one production go application which is more than zero uh but not very many and secondly
[178.10 → 183.72] because I love me some Denver and I'm excited about that that's the funny thing is that Eric and Brian
[183.72 → 191.24] neither of them are from Denver are you guys I'm I'm originally from Wyoming and everybody who grows up
[191.24 → 197.08] in Wyoming ends up in Denver if they want a tech job so after let's say I moved to Florida I don't
[197.08 → 202.82] know 10 years ago and when we were looking to do a conference um we wanted someplace that was kind of
[202.82 → 209.68] neutral because San Francisco is kind of not neutral in terms of corporate territory so we thought
[209.68 → 217.10] Denver might be a really neutral place to have a conference that is not a Google conference this is a
[217.10 → 222.58] go conference and uh you know we wanted that neutral territory so I picked Denver just because
[222.58 → 227.48] I wanted to go back home and see the mountains just for separation of voices who was that that was Brian
[227.48 → 234.68] and I think that uh Denver is really an upcoming tech hub too there are a lot more places popping up
[234.68 → 242.18] there, and we had a lot of uh offers for feet on the ground to help uh by the local meetup group
[242.18 → 247.36] there as well, well deal lets uh let's get some introductions out of the way let's figure out who
[247.36 → 251.72] you guys are we'll dive deep into go we don't have a ton of time because we got a hard stop on one of
[251.72 → 256.32] our sides so we're going to try and blaze through this in 35 minutes just for listener’s sake to know
[256.32 → 262.42] what we're working with here but uh let's start with eric who are you and uh and how did you get
[262.42 → 270.00] started with go for con so my name is Eric Saint Martin uh so Brian and I actually worked together at the
[270.00 → 276.82] time, and we were doing go and uh we kept talking about it for probably what Brian like a year and a
[276.82 → 285.92] half two years easily we were begging for a go conference we really wanted one and uh, uh Brian
[285.92 → 292.14] through some Twitter conversations uh basically got dared to do it and uh he's like let's let's
[292.14 → 303.46] organize one and the rest is history what about you Brian so um I've been doing go since 2010 early
[303.46 → 311.16] 2010 and um wanted there to be a go conference for a long time like Eric said uh you know we've been
[311.16 → 316.98] chatting about how nice it would be to be able to go to a go conference and at some point I guess it was
[316.98 → 324.52] about 2012 uh we said all right this needs to happen uh one of our twitter friends said well
[324.52 → 330.30] then do it you know why sit around complaining about it just make it happen all right fine so i
[330.30 → 335.68] think it was probably midnight I registered gophercon.com and sent Eric an email and said we're
[335.68 → 341.78] doing a gopher conference suck it up suck it up yep and of course he was in full bore so
[341.78 → 346.86] that was that's our origination story our founding story where was the first one at
[346.86 → 353.14] first one was in Denver okay, and we had no idea what we were doing probably still don't to be fair
[353.14 → 359.96] but um you know we'd never run a conference before we just wanted to have a place to build a
[359.96 → 366.74] community for go people to come together now previously we had already created gopher academy
[366.74 → 377.26] which is an um an organization a website whose sole purpose is really just to promote go we wanted
[377.26 → 386.42] there to be an um almost like the ruby central kind of foundation that um promotes go without any sort
[386.42 → 393.48] of corporate sponsorship any corporate allegiance or alliances and I thought it was important early on
[393.48 → 399.78] for there to be that sort of foundation for go so that um people could see it as something bigger than
[399.78 → 408.72] google and uh so we already had the gopher academy um foundation to move on when we built gopher
[408.72 → 414.66] con so it was a little easier for us, we already had a corporation that we could use to create gopher con
[414.66 → 421.08] you know we already had some web properties and such that's a LLC not uh when you say foundation you
[421.08 → 429.04] mean foundation isn't like not real foundation like foundation no it is not a non-profit organization
[429.04 → 435.46] it is sort of a not-for-profit LLC we certainly aren't making any money off of it
[435.46 → 442.42] but haven't gone through the trouble yet of turning it into a non a true IRS type non-profit organization
[442.42 → 449.14] and really that comes with a lot of additional overhead and work which you know obviously gopher
[449.14 → 455.04] academy and gopher con aren't Brian and ice full-time jobs it's stuff that we do on the side
[455.04 → 461.92] so anything that causes additional overhead uh hurts so jerry for you was this uh was gopher
[461.92 → 469.40] con last year on your radar no, no it wasn't at all which uh is strange considering it's not too far
[469.40 → 475.64] away from me and I'm I'm on the periphery of the go uh ecosystem but uh was that the first one guys or
[475.64 → 480.94] was it there was that the second one that was the first one that was the first one all right and
[480.94 → 485.80] when you guys took the dive when you took the dive did you uh know what all goes into
[485.80 → 490.80] throwing a conference or was it an ignorance is bliss type of situation it was definitely an
[490.80 → 497.16] ignorance is bliss if it was like this will be easy no big deal right yeah it was really astonishing
[497.16 → 502.88] how much stuff came up and how much you learn about the whole event industry and all the things
[502.88 → 508.58] you didn't know the contracts and complexities and how much stuff costs it was definitely an
[508.58 → 513.06] eye-opener but yeah last year was our first and I think it didn't register on a lot of people's radar
[513.06 → 520.06] um because we was relatively unknown a lot of even companies came to us afterwards and didn't realize
[520.06 → 526.56] that it had happened already so Brian we have to say a big shout-out to you because we well I guess you
[526.56 → 530.90] and jarred technically because jarred you opened up an issue on our ping repo which people are familiar
[530.90 → 536.68] with so listeners of the show we have a ping repo on GitHub that we use to sort of take in
[536.68 → 542.12] uh notice from the community it's sort of our open repo where you can create issues and help us learn
[542.12 → 546.62] more about what's happening out there and bring us into the know, but we also use it to sort
[546.62 → 553.32] of blast out some information um and in this case we use it to document the changelog 2015 conference
[553.32 → 559.34] scene and that was an evolving issue and Brian you were the very first person to uh come on there
[559.34 → 564.70] and comment and what you said was um gopher con gopher's role, and then you linked out to uh gopher
[564.70 → 570.12] con.com which was great because not long after that we sunk up, and now you're on our list of
[570.12 → 575.50] conferences we're going to as the changelog and changelog films so that was pretty cool
[575.50 → 579.86] I'm quick trigger finger you are quick trigger finger
[579.86 → 585.92] um let's let's talk a bit about I guess we sort of talked about what it takes to create a conference
[585.92 → 592.56] like this but when we say like this can we share a bit about the size change from last
[592.56 → 598.00] year to this year and what the space is so big this year I've been talking to heather and you guys
[598.00 → 603.66] behind the scenes about what's what's all going into making this year's 2015 gopher con take place
[603.66 → 609.28] but you know can we talk about the size difference of last year to this year and what's been learned
[609.28 → 616.84] sure um so I guess it might help with uh history of the progression too so when Brian and i first
[616.84 → 623.22] started talking about this we knew it was something we were new to and uh the I guess the original idea
[623.22 → 629.44] was more a regional style conference you know two to three hundred people so we made room for about
[629.44 → 635.84] four hundred people to begin with assuming you know that'd be our cap, and we ended up selling out
[635.84 → 641.26] and we worked with a hotel to make room for more people and I think we bumped it up to around like
[641.26 → 649.06] 500 or 550 we sold out again we made room for 750 people and then I think that batch of tickets sold
[649.06 → 654.20] out in less than a week, and then we were capped there was no more room left in the hotel to expand
[654.20 → 661.90] so with that amount of growth and just the huge adoption of go even in the last year since gopher con
[661.90 → 669.66] is just staggering so we wanted to make room for uh kind of where our home should be uh from now on
[669.66 → 675.28] and the convention centre the Colorado convention centre there in Denver had a lot more room for us
[675.28 → 684.92] so I mean the main uh ballroom that's split the same way it was last year here is 50 000 square
[684.92 → 693.48] feet so we have a lot of space, and we made room for 1500 people this year uh so we hope we sell our
[693.48 → 701.64] and in some respects we hope we don't because then what do we do next year no yeah so and logistically
[701.64 → 708.44] I think after 1500 you almost have to do multi-track, and we've been trying to stay single track but
[708.44 → 717.14] we'll see how it goes well just curious about the name gopher con um you can throw the f on
[717.14 → 722.16] the end, or you can take the f off the comic con that's that's a convention rails cone that's a
[722.16 → 727.54] conference maybe splitting hairs a bit but did you leave the f off because you were planning on it being
[727.54 → 734.02] a convention on Sunday or was that just kind of how it fell out it just didn't it didn't sound as
[734.02 → 741.54] good gopher cone doesn't sound as good as gopher con good point well now it's named well because it
[741.54 → 748.18] at these sizes I mean if there's 1500 this year uh that's 3000 next year and then 6000 the year after
[748.18 → 753.80] that right just kind of that exponential growth you guys have a convention on your hand yeah we were
[753.80 → 757.90] speaking with a couple of people that were saying you know things like puppet cone took you know three
[757.90 → 763.56] years before it hit 700 people so I think it really astonished us that the first year out that
[763.56 → 769.74] you know we had so many people attend and so many great sponsors that helped make that event
[769.74 → 775.34] happen, and you know we were just two programmers you know throwing a conference so it was really great
[775.34 → 780.16] to see the community respond and all of our sponsors, and they were so great with us too they
[780.16 → 784.44] just really they were kind of in the same boat we were you know they really wanted the conference too
[784.44 → 789.28] and if they could give us some money to help that happen they were happy too let's talk about the
[789.28 → 792.98] one comment you got back from rob pike that really touched your hearts can we talk about that a bit
[792.98 → 803.06] so yeah this is Brian um i I can't give you the exact verbatim comment but it he were walking
[803.06 → 811.12] out of probably lunch at on the last day, so there were still a few uh talks left to give on the last
[811.12 → 815.12] day, but most of the conference had already happened and he turned around to me he said I can't thank
[815.12 → 819.78] you enough for making this happen you know this is such an amazing event and it really
[819.78 → 825.64] feels like you know watching our baby go off to her debutante ball it feels like our baby's growing
[825.64 → 833.42] up and become bigger than us, and you know it is really was heartwarming to see that appreciation
[833.42 → 840.60] and um and joy actually in Rob's eyes he was very excited you know it's like his little
[840.60 → 846.74] girl was going off and getting married and starting her own family, and it was i think the whole
[846.74 → 852.16] team really loved the atmosphere everybody there was so excited and just the conversations
[852.16 → 858.98] and things that were taking place was just mind-blowing and um I'm not sure of the exact
[858.98 → 865.36] percentage but I'm fairly certain that the majority of the go team will be at this year's event as well
[865.36 → 871.50] let's break that down then since uh we've talked about last year and this year's size changes and what it
[871.50 → 879.92] takes uh, so this year is happening July 7th through July 10th uh in Denver Colorado so pretty easily
[879.92 → 888.00] accessible to you know from an airport standpoint uh it's three days after parties a hack day and an
[888.00 → 893.76] optional workshop day does that about break it up into how you describe the tracks and what's going on
[893.76 → 899.38] with uh with the actual conference itself yeah and there's going to be some uh outside events to some of
[899.38 → 906.64] the sponsors are working on planning uh some events on nights outside the after party and then the
[906.64 → 913.90] Denver go group is doing a kickoff party like they did last year at galvanized as well yeah uh yes and
[913.90 → 921.28] which day is that on that is on Tuesday the same day as the workshops okay so basically if you're getting
[921.28 → 925.38] there that night, and you're not attending the workshops, or you're getting there that day to attend the
[925.38 → 930.28] workshops there's something going on that night for you to take part in so watch uh watch the hashtag
[930.28 → 935.96] what is the hashtag for this uh conference go for con go for con hashtag go for con hashtag go for con
[935.96 → 941.72] so if you follow that uh hopefully you'll be up to the know in all the things happening uh with the
[941.72 → 946.38] conference itself uh anything else you guys want to talk about in terms of the track itself any
[946.38 → 952.52] particular talks that you guys are excited about uh a keynote speaker or in terms of talks we've got
[952.52 → 960.00] some really amazing stuff we've got um Dimitri Yukon coming in from Russia he's on the go team now
[960.00 → 968.54] previously from intel um an amazing technical guy who is going to talk about changes to scheduling
[968.54 → 975.32] and go 1.5 I'm I'm personally that's probably the thing I'm most excited about uh we've also got
[975.32 → 982.84] uh rick Hudson who's coming in to talk about the changes to uh garbage collection in go 1.5 and
[982.84 → 987.52] memory management uh that's going to be another huge one honestly all the talks are going
[987.52 → 993.58] to be amazing this year and uh I mean Hannah Kim's coming in to talk about uh go on mobile devices which
[993.58 → 1000.00] is fascinating and that's kind of an um a pattern that we like with the talk selections too
[1000.00 → 1005.92] is to get some things that are slightly different like last year you know we were excited
[1005.92 → 1010.04] to get the go bot guys in there because it was something totally different from what everybody
[1010.04 → 1018.40] else was using go for and uh we've got uh we've got go kit go kits uh we're really excited about that
[1018.40 → 1024.32] and wanting to see its progression there's pretty much all the talks I want to see and there were
[1024.32 → 1030.64] so many that we wanted to see and unfortunately had to turn down too because we had a nine to one ratio
[1030.64 → 1037.02] for slots to fill versus submissions we had over we had 164 proposals this year
[1037.02 → 1042.74] can we yeah talk go ahead Brian I was just going to say talk about heartbreaking when you get
[1042.74 → 1050.34] 164 proposals for 22 speaking slots it's so painful to turn down all those great proposals you know sure
[1050.34 → 1058.90] out of 164 i I probably could have easily enjoyed watching 120 of those talks you know there were so
[1058.90 → 1064.08] many good proposals so if it was very painful turning a lot of perfect proposals down that's interesting
[1064.08 → 1070.94] to see the ratio of talks proposed uh to the attendees coming to like they're in the same ballpark
[1070.94 → 1076.78] but missing a couple zeros or missing one extra zero I guess, but you know like in terms of how many
[1076.78 → 1081.80] proposals versus how many people are coming there's a lot to talk about so you know to go back to
[1081.80 → 1087.14] jarred's point for next year being 3000 it might be a clear winner that next year will double because
[1087.14 → 1093.16] there's such uh such a diverse amount of topics to cover about go it's its uh I know when we had
[1093.16 → 1097.70] Andrew Duran on recently at the tail end of the call we start to talk about mobile a little bit so
[1097.70 → 1101.30] it's exciting to hear more about what's happening in mobile because they're they're working towards
[1101.30 → 1107.78] things for android first in 1.5 and uh I know he was pretty excited about the efforts taking
[1107.78 → 1115.06] place there yeah we're we're definitely really excited to see all the places that go is taking
[1115.06 → 1119.32] off and distributed systems world it seems like everybody who's building a new distributed system
[1119.32 → 1127.66] tool is all go maybe lets uh be slightly self-promotional at this point uh let's talk
[1127.66 → 1132.92] about why we're why we're involved together uh the change log and go for con and you guys
[1132.92 → 1140.70] um and I guess I can maybe crack that nut if you don't mind um we are working with you guys to
[1140.70 → 1147.30] we opened up sort of a films division to our company we started shooting this um well how would
[1147.30 → 1150.32] you describe it jarred how would you describe beyond code is it like an interview series would you call
[1150.32 → 1159.32] it that yeah that's exactly what I don't know what to call it um a film a short film I don't
[1159.32 → 1163.84] know interview series what do you want to call it I'd say like a brief interview series we shoot only at
[1163.84 → 1171.80] conferences, so the whole point is like to be in the scene itself to be enmeshed immersed into the
[1171.80 → 1176.68] community, and it's all about finding not so much the people but just um
[1176.68 → 1182.00] just feeling the heartbeat of the community which is what I loved about uh you Brian and Eric about
[1182.00 → 1185.64] your passion towards go for con was that it seemed like that's exactly where you were coming from so
[1185.64 → 1191.10] we were in synergy in terms of like what we were trying to do with that but also in addition to you
[1191.10 → 1195.40] know our interview series called beyond code we also want to start working with conferences to help
[1195.40 → 1201.52] them shoot like a creative uh documentary style behind the scenes look from the speaker's point of view to
[1201.52 → 1206.64] highlight reels to promotional videos, and so we're working with you this year so if you see people
[1206.64 → 1214.02] running around with cameras um like a couple cameras a mic something like that it's likely us i
[1214.02 → 1217.28] don't think you have anybody else going to be there running around like cameras and mics do you guys
[1217.28 → 1222.80] uh we just have the uh av company recording the talks themselves so we won't have anybody
[1222.80 → 1227.68] running around with cameras and mics but I mean we're really excited about having you guys there too
[1227.68 → 1232.78] because one thing we wish we had last year was b-roll footage I mean unless you were there it was
[1232.78 → 1238.60] really hard to describe just the atmosphere there and how excited everybody was yeah and that's our
[1238.60 → 1243.76] aim too so if you see us running around, and we ask you to help on camera know it's its legitimately
[1243.76 → 1248.74] you know it's legitimately asked for by Eric and Brian they want us there they want us to sort of
[1248.74 → 1253.54] document what's happening there, and we love the community of go, and we want to be a part of it as well
[1253.54 → 1259.20] so being there and doing that is just going to like hopefully change the game for you guys in
[1259.20 → 1264.12] terms of documenting how this conference played out the people that are involved there and just give a
[1264.12 → 1271.16] lot of a lot of like nice artifacts and takes away takeaways for uh for this conference so that's that's
[1271.16 → 1277.24] that's uh that's a neat thing I'm pretty excited about personally and me too actually um I think one of
[1277.24 → 1282.00] the disappointments I have from last year is that we don't really have any professional photographs we
[1282.00 → 1287.18] don't have any significant recordings uh you know there 's's no takeaway from last year other
[1287.18 → 1293.54] than the recorded videos that conference did and i I enjoy watching them over but I'd really love to
[1293.54 → 1300.06] have you know a more intimate uh recording experience and I'm really looking forward to you guys coming in
[1300.06 → 1306.52] this year and kind of giving us that uh that way to look back and show me how much fun I had
[1306.52 → 1312.94] while I was there and then show a new view into what gopher con is for maybe potential
[1312.94 → 1320.14] attendees next year so since you mentioned attendees um let's let's try to get some attendees so we're at
[1320.14 → 1324.58] how many do you talk about how many ticket sales you have I know you just had the announcement
[1324.58 → 1329.12] of a thousand recently but do you kind of give down to the beat of where you're at I haven't looked
[1329.12 → 1335.38] today, but we're definitely above a thousand um we're following the same trend we did last year when the last
[1335.38 → 1341.68] um I don't know the last 25 or 30 percent of the tickets sold really fast about two months before
[1341.68 → 1348.12] the conference, so my expectation is um now that we're above a thousand and now that we're within 60
[1348.12 → 1355.74] days it's going to sell out really fast what we're seeing now is big companies uh big groups of 20 and
[1355.74 → 1362.02] 30 people booking all at once so the tickets really go faster towards the end, and it's really fun to watch
[1362.02 → 1369.10] the emails come in you know xyz large fortune 100 company just booked 30 tickets wow that is
[1369.10 → 1373.72] so cool those are the kind of emails you're getting right now yeah wow that's awesome yeah I love the
[1373.72 → 1380.06] ones where it's a random company too, and you're like what I wonder what they're using yeah well that's
[1380.06 → 1385.12] awesome so if you're listening right now you're thinking man I'm really considering going to this
[1385.12 → 1392.74] conference now is the time to step in buy your ticket and let's can we talk about the buying the
[1392.74 → 1397.40] ticket buying experience and only to mention this one other thing because I was sort of surprised by
[1397.40 → 1402.72] it and when we talked um several weeks back and I asked you about this portion of it I was like
[1402.72 → 1408.76] what is this and then we sort of dove deep into this topic of discussing diversity, and you have a
[1408.76 → 1413.92] diversity scholarship support fund it's not an admission ticket, but you can give whatever amount
[1413.92 → 1419.08] you'd like I think you can multiply it can you talk about that a little bit uh in terms of when you
[1419.08 → 1426.50] subscribe when you um uh register to go what is that about sure so when you go to go
[1426.50 → 1433.66] for con.com there's a link at the top for um registration and that takes you to a landing page hosted by
[1433.66 → 1440.40] Tito which is a really nice company that does good ticket sales for us and the options that you have for
[1440.40 → 1448.56] um choosing tickets include general admission plus a donation to our diversity scholarship fund which
[1448.56 → 1454.70] isn't actually an admission ticket it's just a donation that helps us bring people in whom
[1454.70 → 1460.18] ordinarily wouldn't be able to attend so our concept behind the diversity of scholarship fund is that
[1460.18 → 1468.26] um you know your typical conference especially lately has just been a slew of white guys standing
[1468.26 → 1474.72] around talking about cool computer programming stuff, but we know you know the workforce in programming
[1474.72 → 1481.76] isn't just white guys it's its a lot more than that so we want to make gopher con representative of
[1481.76 → 1486.96] the workforce representative of the population and if there's anything that we can do to help
[1486.96 → 1492.46] financially make that happen that's what the diversity of diversity scholarship support fund is for
[1492.46 → 1500.54] so anybody who makes a donation to that we've got an online scholarship application form on the gopher con
[1500.54 → 1507.18] website you can go in and say you know hey I'm I'm kind of an underrepresented group I would love to get
[1507.18 → 1513.72] some of those funds it would help me attend gopher con we've got a committee that will help allocate
[1513.72 → 1518.76] those funds and try to bring people in that normally wouldn't be able to attend so that the faces we see in
[1518.76 → 1524.24] the audience actually represent the faces of people who are doing go across the world I think
[1524.24 → 1530.54] the other thing we should point out too is the scholarship fund doesn't uh just go towards
[1530.54 → 1539.02] attendees it also helps for um underrepresented groups in speaking as well so um some of the stuff
[1539.02 → 1544.68] that we'd like to do is assist and getting maybe public speaking training and things like that to kind
[1544.68 → 1550.48] of open the doors for more people to jump up on stage and feel comfortable doing so yeah that's a
[1550.48 → 1557.98] great point that was Dave Cheney's idea um the idea that um in order to foster good public speaking
[1557.98 → 1566.68] you not only have to accept a first-time speaker who might be new to speaking but make sure that their
[1566.68 → 1574.40] speaking experience is a positive one and not a negative one so um anybody who requests assistance can
[1574.40 → 1580.98] get uh some funds from us to get good public speaking training and that's another great way to
[1580.98 → 1587.26] build diversity in the speaking community so that someone who perhaps was afraid to speak before
[1587.26 → 1591.40] can have a good experience at gopher con and go out and speak at other conferences too
[1591.40 → 1600.20] yeah Dave has really led the uh the proposals committee and uh has been working a lot with the speakers and
[1600.20 → 1608.68] he's done a phenomenal job with that uh he set up um kind of uh mentoring program where some of the
[1608.68 → 1614.96] more experienced speakers will help mentor some of the less experienced ones to kind of help them
[1614.96 → 1620.34] refine and practice their talks so that they can feel more comfortable getting on stage and i i I thought
[1620.34 → 1626.36] that that was a terrific idea because a lot of people it's its almost a similar issue to contributing to
[1626.36 → 1634.04] open source people are afraid of the judgment on the other side so they just don't step up and i
[1634.04 → 1640.16] think by having these mentoring programs and offering speaker training and things like that I think that
[1640.16 → 1646.04] we can hopefully start seeing a lot more new faces on stage I like the way you're taking the know
[1646.04 → 1652.22] the banner not only to create the ability for the community to converge together but also helping the
[1652.22 → 1657.82] community come positively especially on the speaker side here that you know that's that's such
[1657.82 → 1662.92] a neat thing you don't see that often from conference organizers especially to programmer
[1662.92 → 1668.04] conference organizers that that just sort of like decide one day hey I'm going to register gopher con and put
[1668.04 → 1673.74] this thing together uh you know two years ago it's really nice to see that that your hearts are investing
[1673.74 → 1678.82] in the community and a positive community convergence together I think that's really awesome
[1678.82 → 1685.92] there are conferences out there that are solely made for making money and gopher con is certainly
[1685.92 → 1690.84] not one of those conferences our conference is about building community and community means
[1690.84 → 1697.18] everybody it doesn't mean just the people who look like me and think like me yeah and Eric and i both
[1697.18 → 1703.92] strongly agree that the more diverse that community is the stronger we'll all be um you know the go
[1703.92 → 1709.08] community right now is an amazing community it's its inclusive, and it's strong, and we only want to
[1709.08 → 1715.64] do everything we can to keep it that way that's awesome so when you go to gophercon.com to buy tickets
[1715.64 → 1720.80] you can get a general mission ticket for 500 bucks they have a special field there for a donation to the
[1720.80 → 1726.56] diversity scholarship support fund it's a nice text field so you can crank that number up or down to your
[1726.56 → 1732.06] liking we hope that you crank it up because that's a great initiative you guys also have some other
[1732.06 → 1737.88] interesting fields on the ticket purchasing page which is for child care can you tell us about that
[1737.88 → 1745.64] sure that it is actually a continued part of the diversity of project that we have going on we realize
[1745.64 → 1751.70] that there are people men women all sorts of people who might not be able to attend the conference
[1751.70 → 1756.84] because they've got children at home, and it's its more difficult for them to attend because of those
[1756.84 → 1763.86] children so we contracted with local registered daycare providers, and we'll be providing daycare
[1763.86 → 1770.70] from for any children from 1 to 15 years old at the conference and that's free of charge so if is
[1770.70 → 1775.80] having your kids with you is the thing that keeps you from coming we're going to fix that so all they
[1775.80 → 1780.06] need to do is just give us a notice of how many kids they're going to bring in each age group so
[1780.06 → 1786.08] we can have the appropriate number of daycare staff present and the older kids we're we're even trying to
[1786.08 → 1790.90] organize some little programming camps for them so that they can have their own little
[1790.90 → 1796.22] gopher con great idea no promises on that yet because it's not finalized, but that's our goal
[1796.22 → 1801.14] is to have some programming activities some more fun things to do rather than just sitting
[1801.14 → 1807.82] around playing Nintendo all day oh kids don't play Nintendo any I'm showing my age what do the
[1807.82 → 1813.94] kids play minecraft they're playing minecraft watching minecraft on twitch yes that's so funny because i
[1813.94 → 1820.78] didn't register that you were wrong uh so it shows my age too well not wrong but just not exactly
[1820.78 → 1824.76] correct for the current time that we're in so there's a good shout out to one of our diamond
[1824.76 → 1830.82] sponsors twitch my son who's 13 uh he would rather watch minecraft on twitch than do anything else in
[1830.82 → 1836.40] the world and when he saw the twitch logo on the gopher con page as a diamond sponsor wow he immediately
[1836.40 → 1841.86] wanted to know if he could meet uh whoever it is the guy that he watches all some really amazing
[1841.86 → 1847.94] minecraft guy and that's a thing I don't understand why watching people play minecraft is cool but it
[1847.94 → 1852.84] really is for my 13-year-old so we're excited to have twitch there, and we know that they use a lot
[1852.84 → 1858.12] of go on their back end to power their systems so it's like rock roll music you don't get it you know
[1858.12 → 1863.70] yeah you know you're getting old when you're like why do the kids watch the minecraft on the internet you
[1863.70 → 1869.10] know I don't I don't get it either even though I was a gamer all my life and uh yeah just getting
[1869.10 → 1875.90] older that's getting older they get it they get it so you guys got tons of people uh supporting
[1875.90 → 1880.78] this in all walks you've got some great sponsors who are some of your biggest sponsors who would
[1880.78 → 1886.10] you want to give some huge thanks to for making gopher con this year possible so our biggest sponsors
[1886.10 → 1893.08] are google twitch and Cisco, and honestly we've got dozens of sponsors uh all the way down to the
[1893.08 → 1898.96] bronze level we could not possibly pull this conference off at the insanely low prices that we're doing
[1898.96 → 1903.14] without them so we have to give them just all the thanks and kudos that we can because
[1903.14 → 1908.88] having a conference of this quality at such a low price is impossible without this kind of
[1908.88 → 1914.34] sponsorship dollars so big plus to all of our sponsors go for con.com slash sponsors you can see
[1914.34 → 1920.14] them and uh shoot them some love for yourself yeah they've they've all been incredible they're trying
[1920.14 → 1925.30] to organize things outside the event they're offering assistance however they can many of them are
[1925.30 → 1931.70] offering to give us feet on the ground if we need help stuffing bags very cool and uh last year a lot
[1931.70 → 1937.38] of people were quick to jump on and we got a bunch of return sponsors this year uh it's been it's
[1937.38 → 1941.94] been really exciting, and we're we're so glad for their support if someone's hearing this for the first
[1941.94 → 1945.36] time right now they're like man I wish I would have sponsored this is there still time to sponsor
[1945.36 → 1952.36] there's we're we've passed our deadline, but that's mainly because of printing so right now our shirts are
[1952.36 → 1958.36] going to go out for print so we'd be happy to bring in more sponsors with the expectation that
[1958.36 → 1962.84] they're they wouldn't be able to be on the shirts and anything that we've already gone out for printing
[1962.84 → 1969.44] on uh by the time they come in for sponsorship gotcha that's cool I like the sponsor you guys have here
[1969.44 → 1975.24] so we talked a bit earlier about twitch and uh I think it was Brian or Brian I think it was you
[1975.24 → 1981.66] mentioning your son wasn't yeah a little twitch addict yes that's that's that's perfect for him
[1981.66 → 1990.78] cool yeah my uh my fiancé is the most excited about time hop yes you know my wife she loves time
[1990.78 → 1995.52] hop except for now that Facebook has a feature that's slightly similar to time hop she's always
[1995.52 → 2001.36] comparing like is Facebook's feature better is time hop feature better I'm like well you choose
[2001.36 → 2005.90] you know which one ever whichever you like so she's she's she likes time hop as well one of the
[2005.90 → 2010.84] things that's really fun for me as a business you know owner person who's running a company is the
[2010.84 → 2016.42] fact that these sponsors that were uh that we have this year for gopher con you know a good 50 or 60
[2016.42 → 2023.22] percent of them are vendors to my company you know we've got we use docker we use uh Cisco we use uh
[2023.22 → 2029.18] all kinds of these different companies we use core OS we use influx dB um you know we use iron Io we use
[2029.18 → 2033.64] data dog we all of these sponsors are people that are really deep into the go community and providing
[2033.64 → 2039.42] a great service so for us, it's extra special because you know not only are they sponsors to
[2039.42 → 2043.18] the conference, but they're they're people that we do business with and that's really kind of cool
[2043.18 → 2048.98] and doesn't uh core OS also have some uh something going on with the night party right
[2048.98 → 2053.60] there's an after party sponsored by them yeah that's cool yeah we don't have specifics on that yet
[2053.60 → 2058.66] but yeah they're they're working on an after party themselves very cool I should also highlight
[2058.66 → 2064.14] that some of the companies that we don't currently use because of the sponsorships have kind of drawn
[2064.14 → 2070.00] our eye towards them too exactly for other needs so become a sponsor get our attention we might start
[2070.00 → 2076.46] using it kind of thing although I doubt uh our market is big enough for them to worry about that
[2076.46 → 2083.44] still it's really cool that uh we've met a lot of great companies you know another one that's uh
[2083.44 → 2087.92] that's surprising chiasmatic was uh somebody I hadn't even heard of and they reached out
[2087.92 → 2093.12] and they've got some really great Kubernetes consulting that they're doing um didn't even
[2093.12 → 2097.32] know that there was a cottage industry building up around Kubernetes now that's that's great
[2097.32 → 2102.76] well i I think you know when we zoom out, and we look at everything you guys are doing with go
[2102.76 → 2107.78] for con it's definitely about organizing community it's you know as you'd mentioned
[2107.78 → 2115.32] it's not about profiting from a community it's about joining a community, and you know the only
[2115.32 → 2121.24] thing I would say and this is sort of like maybe public advice is i uh I wish the information
[2121.24 → 2126.20] about the diversity program and the child care was before the registration page because I think that's
[2126.20 → 2131.82] such unique important information I think our community as a whole needs to hear about and one
[2131.82 → 2137.22] shows how much you guys really care about the diversity of the community because that's that's an
[2137.22 → 2142.46] effort that's not taking place you guys are really taking care to like look at all the finer details to make
[2142.46 → 2148.70] this community as diverse as possible and I think it's just something that that doesn't happen every
[2148.70 → 2153.92] day and I'm really happy that you've done that it's really awesome that you're leading the way in
[2153.92 → 2164.14] that way thanks it means a lot to us so one month 18 days 10 hours from now people will converge upon
[2164.14 → 2170.52] Denver Colorado July 7th through 10th and enjoy workshops the main event for one day and two days and then
[2170.52 → 2177.42] the final hack day can you talk a little bit about the hack day as we trail off yeah so um last year
[2177.42 → 2183.66] the hack day was kind of uh an answer just a side effect that we created kind of uh we had the
[2183.66 → 2188.54] two main days, and we assume most people aren't going to want to leave right after you know 5 p.m head to
[2188.54 → 2194.88] the airport that everybody would be trickling out the next day so we reserved space kind of so
[2194.88 → 2199.96] everybody could hack, and you know there'd be some lightning talks early in the morning, and it turned out to be
[2199.96 → 2206.86] I think around like four hours of lightning talks, and it was just crazy and Brian and I were up that
[2206.86 → 2211.10] morning, and we kept watching more and more people go down the escalator, and we're like uh-oh
[2211.10 → 2217.72] because we had anticipated that you know it would be you know less than half the people kind of coming
[2217.72 → 2223.30] and going as they had to leave for flights, and it turned out everybody wanted to stay wow so this year
[2223.30 → 2230.38] we rolled it in and made it a formal part of the event, and we made enough space for everybody to
[2230.38 → 2236.82] attend um the lightning talks will take place in the main theatre, and we will have those recorded this
[2236.82 → 2244.18] year and in addition to that we have a couple of hack rooms that we're still formalizing exactly what
[2244.18 → 2249.62] will be in those, but they will be themed rooms with uh different kind of projects and activities
[2249.62 → 2255.82] going on hacking on specific projects uh things of that nature and as we formalize those we'll be
[2255.82 → 2260.52] releasing more information online about it too but I think it's going to be a lot of fun and I encourage
[2260.52 → 2265.82] anybody who's going to the conference to stay for hack day and hack day is a big deal it's an it's a blast
[2265.82 → 2274.72] that's uh so the 10th the hack day is a Friday and so the conference itself the main one day
[2274.72 → 2280.74] day uh day one and day two is on a Wednesday and Thursday and July 7th which is the workshop day
[2280.74 → 2287.86] is a Tuesday so it's its during the work week so if it's um if it's someone who you know can't
[2287.86 → 2292.20] take a weekend or something like that it's harder to take a weekend a little easier to get off for work
[2292.20 → 2297.00] or you know be sponsored by their employer to get there it's Tuesday Wednesday Thursday and Friday is
[2297.00 → 2301.26] the final hack day we're going to be there for all the days except for the workshop where the
[2301.26 → 2305.36] change loggers are arriving on uh on the 7th not that that matters, but that's just when we're going
[2305.36 → 2310.46] to get there, and hopefully we're going to hit up that meet up that night and then be there all the way to
[2310.46 → 2317.70] the 10th to the end and one thing I should point out about Tuesday the workshop day is uh with the
[2317.70 → 2323.84] talks starting early on Wednesday a lot of people are going to be arriving Tuesday we have uh worked out
[2323.84 → 2332.66] registration to take place between 12 and 6 on Tuesday so if you fly in on Tuesday like between
[2332.66 → 2337.60] 12 and 6 feel free to come down and register that way that's good there's not as big of a crowd uh
[2337.60 → 2341.46] Wednesday morning yeah definitely yeah let's encourage that if you're there early if you get
[2341.46 → 2346.12] there on Tuesday just register on Tuesday save yourself the line and the craziness on July 8th which
[2346.12 → 2353.22] is the morning there so very cool the last thing I want to mention um is for the beyond code piece
[2353.22 → 2359.62] since it's so many people um it's its like normally we just go to a conference that's maybe
[2359.62 → 2363.24] I don't know jerry what would you say like two or three hundred people maybe is our max so far
[2363.24 → 2369.82] with doing this for us so to go to 1500 for us is a much bigger stretch so I think that
[2369.82 → 2374.76] the way we would like to maybe handle it uh we'll still take the sort of walk-ins so to speak, but it'd
[2374.76 → 2379.52] be really awesome to sort of capture people in advance so Brian and Eric would be awesome to work
[2379.52 → 2383.14] with you guys in tandem with that but just here on the audio while people are listening to
[2383.14 → 2388.06] this um we're going to put up a sign-up form on our site, and we'll work with Brian and Eric to
[2388.06 → 2392.52] make that visibly known to everyone else we'll figure out how to formalize it but uh if you want
[2392.52 → 2397.28] to come on beyond code it's about a five to eight minute interview totally about you uh we'd love
[2397.28 → 2400.52] to have you if there's something you want to say specifically about your involvement in the go
[2400.52 → 2405.02] community while we're there at the conference we'd love to sort of like earmark people to talk to
[2405.02 → 2409.36] that way we make sure that we get the great footage that you guys really want us to have um coming
[2409.36 → 2413.76] from this year's gopher con so uh we'll make that available in the show notes so check out the
[2413.76 → 2417.72] show notes for this and then uh we'll work with Brian and Eric to sort of press that information
[2417.72 → 2421.08] out to the rest of the go community that's actually attending gopher con not just those who are
[2421.08 → 2425.72] listening so but if you're listening to this, and you're not going we all got sad faces on so
[2425.72 → 2432.94] what's going with you go to gophercon.com right now um purchase tickets get signed up support
[2432.94 → 2437.40] let me ask you this guys maybe this is something you plan for but is there a way for people who don't
[2437.40 → 2443.36] attend to support this diversity initiative that you've got going on absolutely the tickets can be
[2443.36 → 2448.14] bought separately, and we've had plenty of people donate to the diversity of fund who aren't attending
[2448.14 → 2453.20] so you can buy a ticket for ten dollars or a ticket for a thousand dollars we've had companies that have
[2453.20 → 2458.34] have contributed significant amounts of money towards those diversity funds, and they're not
[2458.34 → 2464.74] attending so it's easy to buy the diversity of support tickets without attending wow please do yeah
[2464.74 → 2470.86] speakers have also been donating as well so that's the process then is just to go purchase
[2470.86 → 2475.42] tickets but don't actually purchase one for yourself just fill out the part that is about the diversity
[2475.42 → 2482.54] scholarship fund and magic correct I love it that's all awesome all right is there anything else you
[2482.54 → 2487.28] guys want to cover before we tail off and say goodbye everybody uh no I think they're just encouraging
[2487.28 → 2492.30] everybody to go the atmosphere there has been phenomenal better than any conference I've ever
[2492.30 → 2499.04] been to and uh I also encourage other people to do more things to help the community start
[2499.04 → 2505.04] local meetup groups do your own conferences although I recommend for logistics to stay small enough where
[2505.04 → 2510.96] you can stay inside a hotel and small enough where you don't have to feed people, and it makes things
[2510.96 → 2516.18] significantly easier uh but yeah definitely encouraging people to do things that help foster the community
[2516.18 → 2523.34] and help it grow yeah and find us on Twitter or email Eric and I have been giving a lot of advice to
[2523.34 → 2529.00] all the other global go conferences about you know how to pull those things off if you want to run a
[2529.00 → 2532.74] conference across the globe, and you even want to use the gopher con name
[2532.74 → 2539.40] we don't care as long as you're not running one in the United States you can use gopher con like gopher con India did
[2539.40 → 2546.20] and we'd, we'd be happy to give them lots of advice on how to run one very cool that's awesome
[2546.20 → 2552.04] well fellows thank you so much for caring so much about the community thank you so much for
[2552.04 → 2556.50] uh taking the time to come on here and talk to jarred and i about gopher con 2015 I know we're
[2556.50 → 2561.54] excited to be there and be a part of it with you and help document such an awesome community
[2561.54 → 2566.98] converging on Denver uh once again July 7th to July 10th purchase your ticket today
[2566.98 → 2572.66] or support the diversity of scholarship fund which is super awesome to do even if you're not going
[2572.66 → 2580.48] uh head to gopher con.com to find all the news and check out the show notes for any extra links we
[2580.48 → 2585.62] we mentioned like the sign-up form for beyond code and uh all the other things so with that uh
[2585.62 → 2589.38] everyone let's say goodbye thanks for having us see ya
[2589.38 → 2610.52] you
[2610.52 → 2610.56] you
[2610.56 → 2640.54] Thank you.
