[0.00 → 20.44] Welcome to The Change Log, episode 0.1.7. I'm Adam Stachowiak.
[20.72 → 24.96] And I am Wendt Netherlands. This is The Change Log. We cover what's fresh and new in the world of open source.
[25.36 → 28.46] If you found us on iTunes, we're also on the web at thechangelog.com.
[28.46 → 34.18] If you want a real-time view of the happenings in open source, check out tail.thechangelog.com.
[34.46 → 44.28] You can also check us out on GitHub.com forward slash explore, where you can find some trending repos, some featured repos from our blog, as well as all of our podcasts from this year's show.
[44.88 → 52.46] And if you're on Twitter, follow changelog show, not The Changelog. And I am Adamitic. That's Adamitic.
[52.46 → 60.84] And I am Penguin, P-E-N-G-W-Y-N-N. Well, special South by Southwest edition, just in time to load it up on the iPhone before you get on the plane.
[61.88 → 62.60] I will not be flying.
[64.50 → 65.54] I meant the listeners.
[66.04 → 68.92] Ah, well, I'll be driving, and you'll be driving as well.
[69.14 → 72.24] I'll be driving. I can listen to the podcast while I'm in the truck.
[72.24 → 73.50] Do you listen to The Change Log when?
[74.26 → 76.12] Just for QA purposes only.
[76.38 → 76.80] Ah, I see.
[77.34 → 83.02] Now, usually podcasts I listen to are the Dev Show, all the 5x5 media. Pretty good. You?
[83.38 → 93.50] Yeah, yeah. I listen to the Dev Show as well. I try to listen to as much as Dan Benjamin as I can take, because their audio quality is just so pimp.
[93.78 → 96.60] Very nice. Tune-age coming out of the 5x5.
[96.60 → 101.20] We should mention some other conferences we're going to be at. Hopefully, Scoff coming up.
[101.54 → 108.72] Yeah, we're hoping to be there, doing something fun there, but waiting on the final green light from the curators of Scoff.
[109.42 → 114.74] Really hope that comes through. That would be a fun conference to hit, another JavaScript conference in our own backyard.
[115.10 → 117.88] Again, in Austin, it's TXJS coming up in June.
[118.26 → 122.54] Rebecca's doing a great job. She's super stoked about the community and the conference.
[122.54 → 128.24] If you see her online, check her out. Follow her and support the conference.
[128.74 → 134.78] Great interview today. We're talking about open publishing with Jeffrey Grossenbach, a.k.a. Top Funky from Top Funky Corporation,
[135.24 → 139.30] proprietor of the Peep Code blog, Peep Code Screencast site.
[139.66 → 142.54] Brandon Mathis, a freelance, I guess, designer from Alabama.
[142.96 → 146.52] And Tim Caswell, a local Dallas area Node.js developer.
[146.52 → 156.72] Brandon and Tim are kind of in the thick of what's called open blogging, where the notion of forking a repo on GitHub that is a blog and the pull request becomes a contribution.
[157.36 → 163.80] That's a lot of concepts. I'm glad we had a chance to bring all these people together and talk about the frameworks and the idea of how it works.
[163.94 → 168.22] And then also just have some back and forth about who does what and how.
[168.92 → 171.62] It was cool talking about all these static website generators.
[171.80 → 174.06] I haven't geeked out like that since talking to Leah about APIs.
[174.40 → 174.84] I know.
[174.84 → 177.44] It was fun. You want to get to it?
[177.60 → 178.58] Yeah, sure. Let's do it.
[186.96 → 190.46] Hi, we're joined today by Jeffrey Grossenbach from Top Funky Corporation.
[191.18 → 195.12] So, Jeff, you've been a big player in the Ruby and Rails scene for a few years now.
[195.28 → 199.86] For anybody that's new to Ruby and Rails, why don't you introduce yourself and a little bit about what you do?
[199.86 → 204.84] Yes, I run a – my main product is called Peep Code video training.
[205.60 → 215.46] Initially, just for Ruby and Rails programmers to help them learn the framework, but now expanding into jQuery, some iPhone development, other kinds of topics as well.
[215.64 → 221.38] And I'm fortunate enough that's been my full-time employment for a little over three and a half years now.
[221.38 → 222.92] You know, I'm a bit excited.
[223.34 → 225.52] I've got to say hearing that voice come across the Skype.
[226.08 → 230.32] I got turned on to Ruby and Rails via your Ruby and Rails podcast a few years ago.
[230.50 → 233.60] How did you get involved with Ruby and Rails and that podcast?
[233.60 → 244.02] Well, I had been living in Taiwan and was about to move back to the United States and thought, hey, let's give this freelancing thing a shot.
[244.46 → 253.58] I had worked with a variety of different technologies, but just happened to learn about Rails, which was starting to become popular at that time.
[253.64 → 254.50] It had just been released.
[254.50 → 275.24] And right, you know, almost as soon as I hit the ground back in the United States, got some contracts, started using it, and then started helping out with this podcast, which has really been a great thing to help me meet a ton of people and build a lot of friendships, as I'm sure you've discovered by running the changelog.
[275.24 → 283.48] Absolutely. You know, as I look at your GitHub page, GitHub.com forward slash top funky, loads of open source projects out there.
[283.96 → 286.88] I got to ask, you know, how did most of those come about?
[286.98 → 288.30] Are you just scratching your own itch?
[288.62 → 292.36] Do you see yourself as a developer first and a publisher second or the other way around?
[293.14 → 295.02] You know, a lot of people ask me that.
[295.12 → 296.58] I think it's a mix of both.
[296.70 → 297.98] I enjoy the creative side.
[298.08 → 299.34] I enjoy the visual side.
[299.34 → 304.90] But at least to some degree, I like to definitely get down in the code.
[305.18 → 312.16] And I like the DAO of coding has a phrase in there.
[312.60 → 316.78] After you go three days without coding, life becomes meaningless.
[316.98 → 318.22] So I definitely subscribe to that.
[318.94 → 328.60] Most of those projects that I have that I've put out there for open source, you know, most of them are things that I actually use, solved a problem for myself.
[329.34 → 330.80] Others are ones.
[332.08 → 336.72] But definitely I try to put other features that people have contributed or are asked for.
[337.38 → 341.84] And inevitably, you know, a project is there and gets a little stale, and I'm not really using it.
[341.94 → 343.36] But there's a whole mix.
[344.16 → 347.64] How does open source drive your business today?
[347.64 → 360.08] I think the big thing is just I started these video tutorials because I wanted to learn about a lot of these different open source projects, and they weren't very well documented.
[361.38 → 366.68] Sometimes it's even two or three years until a book comes out on a particular topic.
[366.68 → 368.42] But people want to know about it.
[368.42 → 374.72] And often a blog post is just, you know, just not long enough to really dig your teeth into it.
[375.00 → 382.38] So I think for me, I'd like to think that I'm helping open source, even though it's a commercial product,
[382.38 → 390.28] by putting the time in to spend a good, you know, a couple of weeks digging into these open source projects that aren't very well documented,
[390.86 → 398.94] coming up with a great demo project and tutorial and then getting it out there so that people can learn some of these different open source things.
[398.94 → 411.26] And it's even been surprising to me that some things I've published on, people have actually started to become interested in them after seeing that now there's some more in-depth documentation.
[412.12 → 418.36] And so that's encouraging to be able to kind of give back by helping people learn this stuff and use it.
[418.36 → 433.46] The only reason I know as much as I know about Git is because of your, you know, tenacious ability to go deep into a subject and just really pull out all the meaningful nuances and, you know, clearly communicate that through an awesome screencast.
[433.66 → 444.66] I know that Git's a big part of and GitHub is a big part of this open source movement that's happened over the past few years and this gigantic community that's just like thriving around us.
[444.66 → 451.80] And it's just wild to see how someone like you can put their passion into what you do and then outcomes, everything that comes from that.
[451.86 → 452.74] So that's pretty awesome.
[453.92 → 458.78] That Git one was fun because it was kind of a risk as is anything.
[458.98 → 464.10] But when I published it, people were starting to kind of talk about Git.
[464.22 → 468.06] I mean, of course, the Linux kernel had used it for two years or something already.
[468.06 → 470.32] So it's not like it was this secret thing.
[470.32 → 475.90] But at least in the Ruby world and a lot of other developers, people just weren't really using that much.
[475.98 → 477.54] But I thought, wow, this looks good.
[477.60 → 478.40] I need to learn this.
[478.50 → 481.12] So I came up with a draft of this screencast.
[481.26 → 485.72] I sent it off to the maintainer of Git, actually, Junior Haman.
[486.36 → 488.30] And I said, hey, I'll pay you some money.
[488.76 → 489.40] Look at this.
[489.48 → 490.60] Tell me if it's any good.
[491.02 → 492.74] And he said, well, it's pretty good.
[492.80 → 495.22] But six pages of notes.
[495.22 → 498.86] So I just scrapped it, started over, refilled the whole thing.
[499.16 → 501.70] And that's now been my top seller.
[502.12 → 506.54] And people actually, actually, when I launched it, very few people bought it.
[506.86 → 510.60] But then a couple of months later, interest kicked off.
[510.98 → 513.80] And it's, yeah, people have definitely loved that one.
[514.24 → 519.54] Well, for me, anytime I meet anybody who's not a Git user, let's say they're using Subversion or something else.
[519.54 → 525.82] But as soon as I know that they're not using Git, I'm like, okay, step one is done a Google search for Scott Charon.
[526.44 → 531.40] And then go to peepco.com and buy the Git screencast.
[531.52 → 532.54] Nine bucks is what is worth.
[532.70 → 538.84] So, I mean, pretty much every time I meet somebody who doesn't use Git, that's my first recommendation to them.
[539.72 → 541.28] Yeah, definitely appreciate that.
[541.28 → 546.00] And, you know, the good thing is now there are many more resources on Git.
[546.12 → 549.92] But still, it's nice to have one spot, sit down for an hour, learn the thing.
[550.06 → 550.90] And then you can go off.
[551.04 → 554.06] Yeah, Scott Charon has, well, he did a PDF for me.
[554.12 → 556.94] And then he did a whole printed book for A-Press.
[557.48 → 558.86] There are a bunch of different blogs.
[559.52 → 565.66] I think Git Ready with Nick Taranto, I think, goes into some good depth.
[565.66 → 572.54] You know, one of the things that I really admired about Peep code Jeff is one of the things that we try to do with the changelog is gone a little deeper.
[572.84 → 581.04] I just know as a consumer of podcasts, it seems like I'm always left just wanting to go a little bit deeper in most topics than most podcasts tend to cover.
[581.14 → 587.36] And that's one of the great things about Peep code and the screencast is just how well they cover a subject.
[587.36 → 598.26] How do you balance covering a subject deeply and letting it have legs as opposed to having content that has a shelf life?
[598.74 → 599.58] That's a great question.
[599.94 → 605.72] And something that I've actually been kind of adjusting to as far as I've learned about the business.
[606.46 → 608.42] First, you're right about the shelf life.
[608.42 → 617.72] I mean, open source software, especially Rails, it's going to change every six months or, you know, every year there's going to be a big release that's going to change a lot of things.
[617.98 → 627.82] So things do tend to get, you know, you got to keep updating them or there are going to be little things here and there that aren't super relevant.
[628.54 → 632.58] The other thing is I do try to hit kind of a higher level of developer.
[632.58 → 644.72] I don't really have that much that's just kind of get started from, you know, if you don't know programming at all or if you have never done any programming, I don't really have much of that content, which actually I'm learning.
[645.20 → 650.12] That's why most publishers do cover that kind of content because it does sell really well.
[650.12 → 669.78] But I still think, you know, there's got to be something out there for the more, you know, intermediate, advanced developer who wants to go learn stuff, see something to where it's not just trying to hold their hand all the way, but to say, okay, let's assume that you have this level of knowledge right here and then let's take off from there.
[670.62 → 674.12] You know, we should mention that all of your content on Peep Code is paid.
[674.24 → 675.42] You have some free content on it.
[675.42 → 690.42] The Peep Code blog, and I think that's one of the things that attracted us to put this particular podcast together is just your take on how you do the Peep Code blog, and you even have an about this blog post that was popular recently a couple of weeks ago.
[691.12 → 701.72] So it's a good opportunity to bring in and introduce Brandon Mathis and Tim Caswell, a couple of guys that are kind of involved in this, I guess, movement we would call open blogging.
[701.72 → 706.26] So Brandon, why don't you introduce yourself to the audience and let the folks know who you are.
[706.70 → 707.08] Hey, everybody.
[707.22 → 709.52] I'm Brandon Mathis, and I live in Birmingham, Alabama.
[711.12 → 719.66] I've done some work on Compass, and I use SAS like crazy, and I decided to write a little blogging framework on top of Jekyll.
[720.72 → 726.30] Since it's file-based, it makes it easy to keep all your source on GitHub, and people can fork and publish.
[726.80 → 729.68] So that's the whole reason I'm here, I guess.
[729.68 → 734.18] And you run an awesome design blog at imathis.com.
[734.22 → 734.50] Is that it?
[735.16 → 740.90] You can get to it at imathis.com, but brandonmathis.com is the forward URL you'll get to.
[741.10 → 741.32] Awesome.
[741.44 → 749.74] And then you recently wrote a blog on open blogging and the whole work with that project you just mentioned.
[749.94 → 756.64] Where did that come about with open blogging, and where did this sort of affirm in your mind really come out into a blog published?
[756.64 → 757.12] Okay.
[757.56 → 769.68] So, yeah, I was working with Ryan Dangle to release a new version of Edge Rails, which is a blog that he's been running for about four years, just keeping up on the latest stuff.
[769.86 → 777.24] And he spends tons of time reading through what's coming up and what people are working on the Edge Rails and writing about it.
[777.24 → 780.72] So really, adopters can get the real deal.
[781.16 → 786.20] Anyway, he kind of felt like he was being the bottleneck having to author all this.
[786.44 → 795.48] And if you've spent much time blogging, you know how hard it is to just get the post out there, especially for geeks who are used to mostly writing in code.
[795.48 → 801.50] So he decided that he'd like to take a look at Octopuses for Edge Rails.
[802.36 → 805.20] And that site is edgerails.info, by the way.
[805.84 → 811.32] Anyway, so he liked the idea that it was file-based, and we talked about what kind of flexibility that gives us.
[811.50 → 816.88] And so on of the things that we do is its all hosted on GitHub, the source for it is.
[816.88 → 825.90] And anybody can fork it and contribute changes to an article if there are errors or things like that, or even write through on articles.
[826.14 → 837.60] And then they can use the fork cue to Ryan Kahn or any of the other authors with commit rights to pull in what they've done and then actually just publish it right to the blog.
[837.60 → 852.16] And the cool thing about that is that instead of being stuck behind this database of – it's hard to give – like what, are you going to give people keys to sign in to WordPress or something and post directly?
[852.62 → 854.54] It's a little bit nastier that way.
[855.06 → 858.62] You start dealing with the whole user management and all that.
[858.62 → 858.94] Oh, yeah.
[859.28 → 861.54] Giving someone a certain access and stuff like that.
[861.92 → 863.50] All the privilege issues are weird.
[863.50 → 878.38] But with GitHub, since it's all open and a fork isn't like access to the core or anything, and it's all managed by people who have commit access, it's a whole different – it's like GitHub has taken care of that for us.
[879.16 → 885.92] And so we're able to accept submissions for articles and things like that really easily from a wide variety of people.
[886.60 → 889.48] And Tim, let's introduce Tim real quick here.
[889.48 → 894.50] So Tim Caswell's waiting in the wings as well, and they're doing that with howtodnode.org.
[894.74 → 897.82] Is that sort of the same stem that you went down, Tim?
[897.90 → 901.26] And let's introduce yourself, I suppose, first, and then you can answer my question.
[901.34 → 901.92] Sorry about that.
[902.60 → 902.84] All right.
[903.18 → 904.16] I'm Tim Caswell.
[904.32 → 907.82] I'm from Richardson, Texas and just north of Dallas area.
[908.78 → 914.56] And I got involved with Node sometime last summer because I was looking for cool server-side JavaScript.
[914.56 → 920.60] And one of the problems with it being a young project is there's not a lot of documentation.
[921.78 → 926.00] And since it's async JavaScript, the programming style is very hard for people to pick up.
[926.36 → 930.76] And the mailing list was just constantly covered with questions, the same questions over and over.
[930.82 → 931.42] How do I do this?
[931.46 → 933.32] How do I do things in parallel?
[933.70 → 934.66] How do I do things serial?
[935.66 → 937.16] And so we said, well, you know what?
[937.76 → 943.24] We should start a blog where people can write articles about how to do these various things.
[943.24 → 949.80] And the Node community, especially the core people, are very hardcore programmers.
[949.90 → 953.58] And we don't want to go start up a WordPress and start typing up a bunch of fluffy content.
[953.92 → 955.52] We needed something that was high-tech.
[956.60 → 960.72] So we got inspired by these programs like Jekyll and said, hey, let's write something like that in Node.
[962.04 → 963.98] So I hacked together a real quick program.
[964.70 → 966.58] It's on GitHub.
[966.72 → 968.38] It's creation slash Node blog.
[968.96 → 970.06] And it's just an engine.
[970.06 → 973.00] And you upload your markdown to a GitHub repository.
[974.34 → 976.08] And it calls some hook.
[976.40 → 977.68] And then it generates all your HTML.
[977.96 → 979.24] Just static HTML generator.
[980.54 → 990.84] But just like we were talking about, since it's on GitHub, if anyone wants to send me an article for the blog, they just need to fork it, write the article, and send me a pull request.
[990.84 → 995.68] And I'll review it and say, it's great, and push it, and it goes live.
[995.76 → 999.40] Or I'll say, hey, could you change these things and give me back another pull request.
[999.76 → 1003.34] And I think I've had quite a few contributors.
[1003.48 → 1006.26] I think about a half of it wasn't written by me.
[1006.80 → 1008.84] So it's done fairly well.
[1008.84 → 1010.64] You got a partner in crime there, don't you?
[1011.32 → 1012.14] With how to Node?
[1013.06 → 1013.26] Yeah.
[1015.02 → 1017.94] Michael, he did the site design.
[1018.30 → 1020.00] And he helped me with the concept.
[1020.16 → 1022.10] And he's been helping me manage these pull requests.
[1023.34 → 1026.94] Because when it first started out, it was hugely popular.
[1027.38 → 1031.74] And I mean, I couldn't get my day job done because I was busy reviewing all these requests.
[1031.74 → 1037.22] And so he would help out, especially since he's in Australia, then we can take turns being available.
[1037.88 → 1039.10] Right, doing the whole time-shifting thing.
[1039.54 → 1039.72] Yeah.
[1040.44 → 1042.90] Yeah, I know that Michael's a fan of the show.
[1043.02 → 1053.76] He always retweets our tweets and helps us raise awareness about the changelog and what we're trying to do with putting the spotlight on new and open source, fresh and new open source projects.
[1053.76 → 1056.82] And people like you guys here on the show today.
[1056.82 → 1065.70] But we definitely wanted to talk about this idea of open blogging and how we can leverage this tool that we all use anyway.
[1065.84 → 1066.38] It's called GitHub.
[1067.26 → 1071.62] And at the heart of that is Git to publish our blogs.
[1072.74 → 1080.00] Normally when we talk about blogging statically, I think what first comes to mind are just single-user blogs.
[1080.10 → 1086.60] I think this open blogging trend, hopefully it will catch on, and it's more of open publishing than anything else.
[1086.60 → 1092.24] But let's talk briefly about the tools that are in the landscape for open blogging.
[1092.36 → 1096.24] We mentioned Jekyll a couple of times and I know Webby is one that I've used in the past.
[1096.38 → 1097.70] Both of these are Ruby-based.
[1098.12 → 1099.64] Adam, I know you're a big fan of Statistic.
[1101.54 → 1109.64] There's a lot of these, I guess, a crop of tools that are arising that are more or less hack CMSs where you don't have to have a database behind the scenes.
[1109.64 → 1118.46] And so that makes it very easy to have multiple environments without having to send data along with your markup and your content lives right there in your version control.
[1119.26 → 1124.98] Jeff, you're using one called Nest or I guess a forked version, a hacked up version of Nest.
[1125.22 → 1130.48] You want to talk a bit about your setup and what you found in moving to the Statics type publishing tool?
[1130.48 → 1138.46] Yeah, basically this is just a Ruby Sinatra application, and it just happens to cache everything.
[1138.66 → 1141.66] So it actually does run dynamically on the server.
[1141.92 → 1147.80] But the first hit, it caches HTML images, JavaScript, whatever.
[1147.80 → 1153.38] It even does some generation of different graphics or resizing things sometimes.
[1153.56 → 1161.48] But after about, you know, 60 or 90 seconds of being up, then everything is cached, and it just works like a static blog.
[1161.64 → 1164.26] So personally, I like thinking that way.
[1164.40 → 1167.40] I like thinking about URLs and handlers and stuff like that.
[1167.84 → 1173.36] Definitely, you know, things like Jekyll or Webby or some of these others are fantastic.
[1173.36 → 1180.62] But I chose just to use a dynamic framework to generate it, but save it all to disk on the first hit.
[1181.40 → 1189.34] I think it's a great setup for a hacker that's also writing, someone that is familiar, just as familiar with the code as the article that they're writing.
[1190.20 → 1203.16] Did you have any reservations about moving to a setup like this thinking, OK, I may be boxing myself in long term around not having contributors that maybe not be this familiar with this low level type of publishing?
[1203.36 → 1209.88] Actually, it's great to hear about these other ways that you guys are doing it.
[1210.08 → 1218.96] And I think that's fantastic because then you can use the commenting and other features at GitHub then to so that you don't have to implement all that editorial process.
[1219.32 → 1229.08] I haven't done anything like that yet, but I have thought about bringing on other authors to actually do creative designs and, you know, write the content and stuff, too.
[1229.20 → 1232.28] And so I may use a situation like that.
[1232.28 → 1237.40] But one thing, you know, just a little history, it's funny how all these things keep rolling back.
[1237.56 → 1243.46] It's not the first time that the web community has hit on this idea of a static blog.
[1243.70 → 1248.38] I remember back in like, what, 99 or 2000, there was like the Blossom.
[1248.38 → 1251.84] It was like a Perl based thing.
[1252.30 → 1256.58] And I forget if it actually ran on a server or if it generated it all dynamically.
[1257.00 → 1261.44] But when I saw that, I mean, that was like a couple of years ago.
[1261.60 → 1263.16] It was like, wow, what a great idea.
[1263.24 → 1268.32] I can just work with files and I can edit code in my text editor.
[1268.54 → 1271.70] And it just works the way that I would be writing normally.
[1271.70 → 1276.90] It seems like a lot of these tools have, and some of them, they're called YAML front matter.
[1277.38 → 1280.58] I'm not sure in Nest, it does have a metadata block up front.
[1280.66 → 1283.26] But is that pure YAML or is it YAML-like?
[1285.26 → 1288.24] I mean, it's just keys and values separated by colons.
[1288.66 → 1289.70] So I don't think it...
[1290.50 → 1296.20] Basically, you have to, if you add properties that aren't supported out of the box, I guess you have to add those to your model.
[1296.20 → 1300.74] Right. So it could be a lot more flexible.
[1302.56 → 1308.56] I think there is a way that you can just dig in and say, okay, give me a key that's named by this string.
[1308.68 → 1312.34] But usually you build a model and add an actual method to pull that out.
[1312.96 → 1319.70] So beyond just regular static blogging where you've got a stream of articles and archives and details of articles,
[1319.70 → 1325.48] have you hit any challenges that this type of approach you think might be hard to work around?
[1326.20 → 1332.76] Well, I mean, the initial challenge was just that I didn't see anything out there that it was exactly what I wanted.
[1333.20 → 1336.18] And of course, you know, that's what open source is all about.
[1336.38 → 1338.84] You don't see the one or two little features you want.
[1338.88 → 1343.06] So you start from scratch and rewrite a whole new software product.
[1343.84 → 1346.10] But, you know, Nest was a great...
[1346.10 → 1347.52] It had most of what I wanted.
[1347.52 → 1354.48] And I actually, I was on a trip down to Australia for Rails camp, which is an awesome thing.
[1354.58 → 1361.86] They just like rent out a summer camp for a weekend and people come and, you know, write code and talk and stuff.
[1362.00 → 1362.06] But...
[1362.06 → 1364.16] Was that the one that's totally away from the Internets?
[1364.96 → 1366.48] Yeah, no internet either.
[1366.60 → 1366.74] Yeah.
[1366.80 → 1369.12] They build their own network.
[1369.12 → 1376.00] I think the guy who wrote Twenty, Lauren Brighter, actually gave them a special version that they can use locally.
[1376.24 → 1382.86] So they actually have a Twitter clone up and people are all, you know, talking and Timing and stuff like that.
[1382.92 → 1386.18] But it's not connected to the outside internet, which is kind of fun.
[1387.48 → 1388.22] So you were in Australia?
[1388.22 → 1388.34] Yeah.
[1389.14 → 1389.54] Yeah.
[1389.78 → 1396.70] So I, you know, I knew, I'd known for even a year or something that I wanted to do something like this.
[1397.16 → 1404.00] And so I cloned a bunch of different products and I started looking at them and I thought, oh, okay, this is nearly what I want.
[1404.14 → 1406.46] But I want each post to be different.
[1406.64 → 1409.70] I want, you know, I want it to use SAS.
[1409.84 → 1411.86] I want a bunch of these different things.
[1411.86 → 1414.52] So I found it really easy just to work those in.
[1415.38 → 1415.46] All right.
[1415.48 → 1416.68] You mentioned Hamill and SAS.
[1416.68 → 1424.30] Adam's and myself's favourite technologies, even episode one, was Hamill, SAS, and Compass.
[1424.86 → 1433.66] So when I read about this blog post on Peep code, I was excited that you were trumpeting that because I just, I love what Hamill does for markup.
[1433.70 → 1438.54] And I think if I could pull the exact quote, I love what you said about Hamill.
[1438.60 → 1442.96] And it says it decreases the mental distance between HTML and CSS.
[1443.88 → 1445.98] You want to expand on that a little bit?
[1446.68 → 1447.12] Yeah.
[1447.12 → 1447.44] Yeah.
[1447.70 → 1455.02] You know, another fun thing about doing it this way is then you can have a draft that's just there for a couple of weeks, and you get to kind of mull it over.
[1455.02 → 1465.28] And you don't feel the pressure of having typed something into this little, you know, text area on a web form that you feel like is just kind of this immediate thing.
[1465.36 → 1467.00] Although I guess you could do a draft there too.
[1467.00 → 1472.28] But that specific quote was like from a separate article that I haven't published yet.
[1472.28 → 1480.26] Just thinking about, you know, as a programmer, especially, you know, a web programmer now, you're thinking in all these different languages and different formats.
[1480.26 → 1490.76] And so anything that can just kind of reduce that without being too much of an abstraction helps me to focus and think about the problem I'm trying to solve.
[1490.76 → 1496.42] And for me, you know, I'm not going to insist that everybody or even anybody needs to use it.
[1496.60 → 1501.72] But Hamill, I think, does that because then I can just think about CSS selectors.
[1501.72 → 1506.16] And then I jump over to SAS or straight CSS.
[1506.64 → 1509.84] And then again, you're thinking about CSS selectors.
[1509.88 → 1511.14] And then you jump over to jQuery.
[1511.32 → 1518.86] And again, you're thinking about CSS selectors as you dial in some element to handle a behaviour or something on it.
[1518.94 → 1520.86] So that's where it's at for me.
[1521.06 → 1529.32] Well, I was jumping over to Brandon's Octopuses project page on GitHub just now to double-check that Hamill was one of the opinions kind of baked in on top of Jekyll.
[1529.32 → 1532.40] And I noticed the last push is 16 minutes ago.
[1532.46 → 1534.70] And I think we've been on the air for like 30 minutes or so.
[1536.16 → 1536.56] Guilty.
[1537.16 → 1539.54] So, Brandon, are you pushing updates during the podcast, buddy?
[1540.94 → 1543.28] Actually, yeah, I was just finishing up some stuff.
[1543.68 → 1548.80] There's a really cool expandable code window that I wanted to get up there.
[1548.84 → 1550.68] And I was just starting it right before you guys called.
[1550.68 → 1560.18] So it's one of the things that frustrates me on fixed widths blogs is you get this code window.
[1560.26 → 1564.00] And sometimes you have to scroll around to read things or copy them and paste them somewhere else.
[1564.34 → 1572.16] So I wrote a little JavaScript that would find the code windows and add these expanders that collapses the sidebar and gives you the full width of the site.
[1572.16 → 1584.08] So that's quite a design decision of are you going to allow people to write long lines of code or are you going to implement something like that, which is a great way to go.
[1584.22 → 1597.12] I know the Marcel Molina in there, you know, a couple of years ago, although it's still going with the projectionist blog, they restricted themselves to something ridiculous like 40 characters wide or something.
[1597.12 → 1601.00] And they just wouldn't write any code samples that were more than 40 characters wide.
[1601.00 → 1602.10] So that's nice.
[1603.20 → 1607.26] So Brandon, you chose Octopuses.
[1607.54 → 1609.32] And primarily, let's set the premise here.
[1609.80 → 1615.72] It's not that you're not a developer, but you're primarily a front-end designer, mostly in the Rails and Ruby world.
[1616.36 → 1619.40] And you're a fan of Hamill, and you're a fan of SAS and obviously Compass.
[1619.54 → 1624.22] So that's sort of the premise of your skill set when you approach projects.
[1624.22 → 1630.54] But why did you choose Octopuses, or why did you choose to chisel out Octopuses and why Jekyll?
[1631.00 → 1635.76] So I was working on, I guess, last summer or something.
[1636.96 → 1640.56] I was working on redoing my website to get some work.
[1640.94 → 1644.98] I'm a freelance designer, so that's kind of one of those things.
[1645.68 → 1648.38] And I was just looking at WordPress and saying, not again.
[1648.76 → 1650.58] I'm not going through this again.
[1650.58 → 1660.70] And I've been paying attention to what people were doing with Jekyll and GitHub Pages were doing that.
[1660.74 → 1662.36] It was kind of the hotness at the time.
[1663.10 → 1669.68] And I think it was the only blog-aware static site generator I could find that you didn't have to do a bunch of tricks to make it happen.
[1670.02 → 1678.42] The problem was that all it did was generate markdown or textile or something to HTML.
[1678.42 → 1682.54] And Heinrich did a fork that let me use Hamill.
[1682.62 → 1685.24] So I was like, okay, this is – the gods have spoken.
[1685.34 → 1686.76] This is definitely something I've got to use.
[1688.30 → 1691.88] And then I found out that all it was is a generator.
[1692.08 → 1694.94] Like it didn't have any kind of starting point framework.
[1695.18 → 1698.10] There was nothing – like it was really hard to figure out.
[1698.18 → 1699.12] I had to read through all these docs.
[1699.26 → 1700.02] Hard to use.
[1700.02 → 1709.82] So I said, well, I might as well build something that is a little more abstract and kind of – you have a couple places where you put in your configurations.
[1710.10 → 1713.56] And you've got these rake tasks that do all kinds of terrific things for you.
[1713.88 → 1725.08] So right now, if you wanted to create a new post, you have to have like the date in the post name and some weird things that as a static site generator, you just have to learn to deal with.
[1725.38 → 1727.86] So I wrote a rake task that lets you do all that.
[1727.86 → 1735.76] But you can deploy through sync with a rake task or use GitHub pages, and you just change some configurations around.
[1736.98 → 1745.20] And like – so one of the problems with static site generators that you guys didn't talk about earlier is that when you're generating a huge site, they can be really slow.
[1746.06 → 1752.14] So when I was working with Ryan, he's got all these posts on edgerails.info.
[1752.46 → 1756.06] And we came up with a way to create a stash directory.
[1756.06 → 1765.10] And so while you're working on a post or a design, you can stash all the posts but one of them so that it will only be generating that one post, and it will ignore the other stuff.
[1765.36 → 1767.32] And then you can reintegrate them right before it deploy.
[1768.38 → 1770.66] So that kind of stuff just makes it nicer.
[1770.78 → 1780.18] And then, of course, all these hackers out there that want to blog, and then when they start, they're like, well, now I have to find a design, or I have to use these ugly default designs or whatever.
[1780.18 → 1788.18] I wanted to come up with something that had the beauty of compass and sass in it so that I could make the layout configurable.
[1788.80 → 1789.78] You just change some variables.
[1789.92 → 1792.20] You've got a different size sidebar, and everything works.
[1792.92 → 1795.54] Or you can get rid of it, and it doesn't break on you.
[1795.70 → 1799.66] Colours are actually in a theme file, so you just go in there and change everything.
[1799.66 → 1805.92] And I think I'm even doing some stuff with gradients through CSS3 that are based on base colours.
[1806.26 → 1811.02] So it's all very – you don't have to be a designer to go in there and make it look good.
[1811.36 → 1814.52] So you've added a lot of design magic in there as well as some of the niceties.
[1815.14 → 1815.46] Right.
[1815.46 → 1822.86] It's something that I use for my site, and there are some other sites out there that are using it too, but it's not really that big yet.
[1822.96 → 1825.36] It's still kind of – still got some work to do.
[1825.40 → 1831.56] We just added partial support through Tamil, and that's – I think I pushed that up this morning.
[1832.30 → 1839.52] But when I was working with Ryan on it, one of the problems is that in the default layout, you have like all this code.
[1839.80 → 1842.76] So I wanted to do conditionals so I could integrate third-party stuff.
[1842.76 → 1849.66] So all you have to do is say, this is my Twitter name, and all of a sudden you've got a JavaScript Twitter widget in your sidebar.
[1850.30 → 1852.60] And if you don't have it, I didn't want to output all this stuff.
[1852.72 → 1857.84] So all these conditionals are hidden behind partials now, which was pretty hard to do earlier.
[1859.42 → 1863.44] You know, one of these tools that we haven't talked about yet is NATO from Denis Dufresne.
[1864.14 → 1867.94] And it's one of my favourite of the static breed.
[1867.94 → 1879.64] But something interesting that Denis is doing is he has a Rack app that fires up, and most of these static generators have a preview mode that runs Web Rick or something internally.
[1879.90 → 1889.68] But, you know, I think the holy grail for me is I'd like to see it develop along the line of being able to fire up that Rack app and have the best of both worlds.
[1889.84 → 1896.48] Have a static compilation up front so that you could have the built-in caching, but also to be able to compile one page on the fly.
[1896.48 → 1900.94] And I think that's what turned me on to Nest, even though you don't have to do the compilation up front.
[1901.08 → 1903.68] You know, there's no pre-compilation required.
[1904.78 → 1906.58] Yeah, I'm definitely keeping my eyes on NATO.
[1906.68 → 1911.46] Hopefully at some point I'll be able to have Octopuses.
[1911.96 → 1913.04] You'll be able to pick your flavour.
[1913.24 → 1916.36] So if NATO does blog stuff really well.
[1916.44 → 1918.48] Right now my focus is blogs, not just static sites.
[1919.72 → 1922.98] So, yeah, if that happens, I'd love to get my hands on some NATO.
[1924.34 → 1925.24] Well put.
[1925.24 → 1929.36] So, Tim, what's going on with Node?
[1929.98 → 1932.06] I guess specifically how to Node.org.
[1932.16 → 1932.94] What's going on there?
[1933.48 → 1935.16] So you wrote your own engine on top of Node.
[1935.68 → 1937.24] What is this about?
[1938.20 → 1946.34] Yeah, I had already made a port of Tamil for Node a while back because I like using Tamil for structure.
[1947.22 → 1950.42] And right now it's using Showdown for the markdown.
[1950.42 → 1956.84] And so the whole back end, if you go to the repository for how to Node.org, it's just, there's a skin folder.
[1957.12 → 1958.46] It's just a bunch of Tamil files.
[1959.18 → 1960.84] And then there's an articles' folder.
[1960.98 → 1962.42] That's just a bunch of markdown files.
[1963.04 → 1964.38] And then there's an authors' folder.
[1964.54 → 1966.00] And that's just a bunch of markdown files.
[1966.72 → 1967.76] And that's the content.
[1967.76 → 1973.04] There's, I mean, there's a little CSS in the static image, but that's pretty much it.
[1973.04 → 1976.12] So it's pretty light then.
[1976.24 → 1977.22] How do you handle layouts?
[1979.10 → 1980.82] Well, the Tamil supports partials.
[1981.24 → 1986.36] And so the engine just looks for the articles.
[1986.56 → 1988.50] And it looks for a Tamil file called Article.
[1989.06 → 1991.24] And that's basically the way it renders that article.
[1992.34 → 1995.58] And then there's a little bit of metadata in the top of the markdown files.
[1995.58 → 2001.92] So it knows which author to link this article to, when it was published, and various things like that.
[2004.54 → 2008.16] And this Tamil JS, is this what we covered a while ago?
[2009.38 → 2010.36] I believe so.
[2010.56 → 2013.26] I have two Tamil projects for JavaScript.
[2013.54 → 2015.54] And people often get them confused.
[2016.20 → 2018.64] One of them is a jQuery plugin that runs in the browser.
[2018.64 → 2024.74] That's a DOM building engine using a JSON expression syntax.
[2025.60 → 2030.98] And then the Tamil JS is targeted for Node, but it really works anywhere.
[2031.18 → 2039.26] It just takes a Tamil file and translates it into a JavaScript file that then takes variables,
[2039.44 → 2041.24] just like any other Vue template engine.
[2041.24 → 2049.60] So when we really spread it across, we've got a static blogging engine built on top of Node.
[2049.70 → 2053.18] We've got something sitting on top of Sinatra, which is a dynamic.
[2053.36 → 2053.86] It's called Nest.
[2053.92 → 2056.76] And then we've got Jekyll, which is just all behind the scenes.
[2056.88 → 2058.34] No dynamic ness at all.
[2058.40 → 2062.00] It's just statically generated one time, and then you upload that to the site.
[2062.06 → 2064.30] So we've got a pretty wide spectrum on here.
[2064.34 → 2066.22] Anybody have any opinions on best or breed here?
[2066.26 → 2069.42] Just curious on what consensus is so far.
[2069.42 → 2072.44] Or I guess maybe the first question is trend or fad.
[2072.86 → 2073.00] Yeah.
[2073.54 → 2078.62] I think a key part of deciding what you want to use has a lot to do with the constraints.
[2079.44 → 2090.38] And the nice thing about having something that generates locally and that you just push is that you have a whole range of server options to choose from.
[2090.58 → 2093.02] You don't have to worry about getting anything set up really anywhere.
[2093.26 → 2097.44] And also you can host on GitHub pages if you want to, if it's all static.
[2097.44 → 2108.76] And then with things like Google Search and Discus comments and things like that, it's really easy to make it feel a lot richer than a typical static site.
[2109.66 → 2113.80] That's one piece we didn't touch on, which I wanted to ask you about search and stuff like that.
[2115.14 → 2116.48] Jeff, how are you handling search?
[2116.48 → 2124.48] I know that with Brandon, you're lynching out to Google Search, and you're returning those results via Ajax and stuff like that.
[2124.52 → 2125.68] But Jeff, how are you handling it?
[2125.76 → 2127.16] And Tim, how are you handling search?
[2127.16 → 2134.42] You know, I've started out very small, and I tend to just build things as I go, as I need them.
[2134.56 → 2138.78] I kind of wait until I have too much content to wade through, and then I'll make a search.
[2139.02 → 2143.96] So, you know, right now I think I have like seven articles on there and there's a good little archive page.
[2144.54 → 2151.58] You know, maybe in a couple of months I'll build search, and I'll probably just do it dynamically because Sinatra is right there on the server.
[2151.58 → 2153.06] How about you, Tim?
[2154.50 → 2159.86] Well, Houghton is just a plain static generator, and then it uses Discus for comments.
[2160.02 → 2163.24] So I guess the only search I have there is Google will index it and find things.
[2164.32 → 2178.28] But another project I'm working on, we're updating Node's API docs, and it's using a similar engine where it just takes a Markdown README file and generates this interactive page where you can go through the API docs.
[2178.28 → 2184.70] And for that one, it's actually doing all the searching in JavaScript in the browser.
[2184.96 → 2190.16] It'll AJAX in the data and then search over that data and then give you your relevant results.
[2191.38 → 2195.60] So for an API site, you can search for any method or whatever.
[2197.18 → 2202.32] One thing, you know, if I was going to, if someone else was going to ask me, oh, I'm going to start a blog, how should I do it?
[2202.32 → 2209.84] I'm not sure if I would even recommend it the way that I do it unless it was a code-based blog.
[2210.04 → 2217.42] And for me, this is where it's perfect is when I want to throw in a little snippet of Ruby or Hall or whatever.
[2217.42 → 2228.96] I'm editing a .Rb file, or I'm editing a .Hall file and I can use all the snippets and feature, you know, syntax highlighting and all the features of my text editor right there.
[2229.06 → 2234.02] And then it just gets slurped into the proper place in the pros.
[2234.64 → 2235.84] How do you guys do it?
[2236.02 → 2238.52] Are you just typing stuff in line?
[2238.62 → 2239.70] Find that works well for you?
[2239.80 → 2244.62] I know TextMate has pretty good support for, you know, little islands of different content.
[2244.62 → 2253.12] But for me, I think a code blog that you want to look good, this is a perfect way to do it.
[2255.32 → 2258.34] Well, I think that we're breaking some rules, actually.
[2258.82 → 2267.16] Because of our constraints with the change blog and getting started, we're using Tumblr, which isn't that bad, like you said.
[2267.16 → 2269.84] But we are inserting code snippets.
[2270.12 → 2279.28] And, you know, when we read your blog post on how you're actually leveraging, you know, a standalone .Rb file for Ruby snippets or something like that, that's, you know, that just makes sense.
[2279.64 → 2284.58] And so we are eyeballing, you know, the Sinatra and Nest scenario.
[2284.72 → 2286.38] We've eyeballed a few of these scenarios.
[2286.46 → 2294.16] That's why we wanted to kind of share this talk to kind of go over different ideas of what's out there and what's successful and what makes the most sense for us long term.
[2294.16 → 2300.76] Yeah, when I read your post, Jeff, about how you're linking to external files, it seems so painfully obvious to do that.
[2300.78 → 2301.92] Because what do we do normally?
[2302.08 → 2305.60] We include a pre-encode nested block in your page.
[2306.12 → 2313.84] And then via, you know, JavaScript, you wire that up to be a separate download in a pop-up window or a copy of the clipboard or something like that.
[2313.88 → 2315.46] It seems to be the common approach.
[2315.94 → 2319.00] Another approach that turned me on was, you know, Rack.
[2319.08 → 2320.82] There's a Rack appliance for everything nowadays.
[2320.82 → 2325.42] And there's a few of these out there that will do syntax highlighting on the way out.
[2325.52 → 2327.10] So it looks for certain rules.
[2327.22 → 2337.74] You can have even markdown for indented space code blocks in your Markdown markup or just regular HTML pre-encode blocks.
[2337.92 → 2344.30] And it will find those and run them through pigments, which is a Python syntax highlighter or something on the way out, which is pretty cool.
[2344.30 → 2350.48] But actually, your approach about doing the external files, I think, is something to take a look at.
[2350.52 → 2353.20] Brandon, Tim, you guys using any special approach?
[2356.12 → 2360.22] I'll probably be snagging that external file approach at some point.
[2360.28 → 2361.64] Right now I'm doing a pre-code thing.
[2361.64 → 2375.00] But, yeah, I was going to say, I don't know if you were asking this, but I definitely think that this static blogging thing makes a lot of sense for programmers, but no sense for, like, you know, my mom or anything.
[2375.12 → 2381.38] I can't imagine anyone wanting to do this who wasn't in a text editor all the time and wanting to stay in their same environment.
[2381.38 → 2389.02] Yeah, we definitely want to pull in that feature in the Node Blog engine where we can use external files.
[2389.90 → 2395.80] One of the problems we had initially been I would put up these code snippets in my markdown because they're easy to see in Markdown.
[2395.90 → 2398.34] They're just over to the side, but there's no syntax check-in.
[2398.38 → 2399.02] There's no highlighting.
[2400.14 → 2403.42] And after I'd post an article, people would say, you got a syntax error here.
[2403.86 → 2409.08] I'd be like, oh, yeah, I didn't test that code because I was just typing it along with the rest of my text.
[2409.08 → 2419.94] And so what I switched to is I started creating subfolders under my articles where I would write the code, I would test the code, and then in my last step, I would copy-paste it back into the markdown.
[2420.92 → 2423.32] But occasionally, I would forget to copy-paste something.
[2423.84 → 2425.64] So it was better but still not ideal.
[2426.44 → 2437.70] So I think the next step we want to take is have some sort of flag in there where it can dynamically pull in the text from the external file and link to the external file, so people can download it if they want.
[2437.70 → 2439.66] So I think that's a great idea.
[2439.76 → 2440.86] I think it's the direction we're going.
[2443.18 → 2447.82] So Jeff, at the close of your article, you'd actually – which saddened me for a moment there.
[2448.04 → 2456.80] I'd actually started to hear taps play and everything, but you had said that you haven't open-sourced your code base yet or don't really have plans to.
[2456.80 → 2466.96] What are your feelings now that you've sat in a conversation like this, and you hear other people wanting to adopt more of the top funky goodness that's out there?
[2467.08 → 2469.70] How do you feel about releasing that code source now?
[2470.50 → 2474.32] I'm not opposed to putting the source code out there.
[2474.42 → 2480.42] It's just a little bit of extra work trying to clean up stuff and all those little hacks that you do just to get something to work.
[2480.42 → 2485.66] And then you don't want people to see that, so you have to spend time making it look good.
[2486.24 → 2489.88] But mostly, I just wanted to put these ideas out there.
[2490.16 → 2497.48] And this whole conversation just now I think has encouraged me that there are many great blogging engines out there.
[2497.72 → 2503.36] It sounds like you guys are doing a fantastic job and doing something that other people are contributing to.
[2503.54 → 2507.44] So I don't know if there's even a need for me to put the code out there.
[2507.58 → 2509.48] Hopefully, maybe just the ideas are good enough.
[2510.42 → 2515.12] One last question before we jump over to the radar.
[2515.38 → 2522.00] So one of the things that you're doing, Jeff, is styling each blog post for the most part with its own style sheet.
[2522.08 → 2526.32] And I think someone that does this extremely well is Jason Santa maria in his blog.
[2526.46 → 2527.70] I mean, it's amazing.
[2527.98 → 2531.52] Every time you hit one of his articles to even realize that this is the same blog.
[2531.90 → 2535.62] How much overhead does that add to your blogging workflow?
[2537.24 → 2538.32] Well, I do.
[2538.64 → 2539.74] You know, it...
[2540.42 → 2542.88] It adds overhead, definitely.
[2543.66 → 2548.22] You know, I'd probably say it takes me a full day of eight hours or something to do a full blog post.
[2548.42 → 2556.24] But that's not counting, you know, the week before where I'm just kind of brainstorming in my free time or, you know, any other little tweaks.
[2556.24 → 2558.90] But for me, it was two things.
[2559.20 → 2562.12] One, okay, I'll admit, it drives traffic to the site.
[2562.24 → 2565.84] People love to see something that looks great and people come in, and they buy my products.
[2566.50 → 2569.48] And I don't have to, you know, shove advertising down their throat.
[2569.48 → 2578.14] I can just write this, you know, good-looking article and interestingly styled and that kind of advertises itself.
[2578.14 → 2586.20] The other thing is, for me, I want to get better at design and at the code behind it.
[2586.20 → 2590.76] And I just don't have that many opportunities to start something from scratch.
[2590.76 → 2603.18] So with this, you know, every other week, it's almost like I'm starting a brand-new project and I can get different inspirations and ideas and try out CSS3 gradients and all kinds of stuff.
[2603.42 → 2609.02] And so to me, it's a great learning experience and just a lot of fun to do.
[2609.02 → 2610.56] So your own little sandbox.
[2611.00 → 2612.48] So what's out there on your radar?
[2612.62 → 2613.76] What open source projects?
[2613.92 → 2615.48] I guess at some point Nest was on your radar.
[2615.66 → 2620.16] What is exciting you now that you'd like to work in to peep code at some point?
[2620.98 → 2624.92] Oh, Node.js is definitely interesting.
[2626.36 → 2638.32] I feel like in the last three or four months, I've just kind of chomped down on a lot of different JavaScript and really started to learn more, be a lot more comfortable with it.
[2639.02 → 2644.02] I also love Raphael.js, SVG graphing library.
[2644.86 → 2654.64] Fun to be able to just actually do some drawing in the browser and whether it's visualizations or graphs or whatever, or even custom widgets.
[2655.94 → 2658.16] You know, beyond that, Rails 3 is very exciting.
[2658.38 → 2660.92] Sinatra 1.0 is coming out.
[2662.48 → 2663.78] All kinds of stuff.
[2663.88 → 2664.68] Yeah, all the time.
[2666.18 → 2667.00] How about you, Brandon?
[2667.00 → 2671.04] Man, you just can't get me to stop talking about Compass.
[2671.32 → 2676.84] I am thrilled with the way that's going and pulling the pre-releases as soon as they come out.
[2677.02 → 2680.10] So that's really my bread and butter right now.
[2682.06 → 2684.30] So just Compass, that's the only one your radar?
[2684.94 → 2685.52] On my radar?
[2685.64 → 2686.60] Well, I mean, that's –
[2686.60 → 2687.52] I guess –
[2687.52 → 2688.32] That is your radar.
[2688.70 → 2688.84] I mean –
[2688.84 → 2689.58] Yeah, pretty much.
[2689.58 → 2691.30] I'm mostly a designer.
[2691.84 → 2696.40] So that's really the key part that I'm paying attention to.
[2696.48 → 2699.74] Obviously, you know, I work with JavaScript frameworks and other things like that.
[2699.92 → 2706.14] But if I just had one thing to push to people right now, I'd say check out Compass because it is changing my life.
[2706.36 → 2707.68] Well, you've got fancy buttons out there.
[2707.72 → 2710.22] Any other plug-ins that you've got for Compass coming out?
[2710.70 → 2711.62] Yeah, let's see.
[2712.34 → 2715.50] I'm working on – well, I have a lot of different things.
[2715.64 → 2721.50] Octopuses is actually chocked full of little things here and there, libraries that I'm working on.
[2722.42 → 2726.06] So like I have a typography module and things like that I'm doing.
[2726.06 → 2731.90] So it's – I think what I really want to get is a good, flexible layout.
[2732.92 → 2734.96] You know, everybody is releasing these grids and things like that.
[2735.00 → 2736.60] And for me, a grid is just useful for layout.
[2736.80 → 2739.98] So definitely I'll be releasing some stuff soon.
[2740.02 → 2742.26] I can't say a lot because I don't want to commit to anything.
[2742.36 → 2743.10] We'll see where it goes.
[2744.22 → 2747.20] But yeah, fancy buttons has been awesome.
[2747.28 → 2753.26] If you don't know what that is, it is a great way to easily style buttons without having a ton of markup.
[2753.26 → 2757.60] It uses – like you can do a style of button or a link.
[2757.84 → 2760.68] That's all there is to it, no adding spans or weirdness.
[2761.34 → 2769.48] And it uses CSS3 gradients to make them look really clickable and has a bunch of options and things and very flexible.
[2769.62 → 2777.04] But also it has a backup image that it uses in case the browser can't render through CSS gradients.
[2777.80 → 2779.70] And Tim, what's on your radar, Tim?
[2779.70 → 2781.70] Tim, well, I won't lie to you.
[2781.82 → 2785.90] I've been completely buried in Node for the last six months.
[2786.22 → 2787.60] But there's a lot of new stuff there.
[2788.50 → 2792.88] One of the projects I find interesting is Felix has been working on something called Node Dirty.
[2793.84 → 2798.90] And it's just a really simple, handmade, NoSQL engine written in pure Node.
[2799.80 → 2801.92] And he kept it simple on purpose.
[2802.08 → 2803.30] It has no network interface.
[2803.30 → 2807.48] It just does append-only write and simple queries.
[2807.72 → 2812.46] And it goes along with the rest of the Node philosophy of keeping it simple and just tie things together.
[2812.46 → 2824.00] Well, I think it's, you know, for this entire subject of static blogging, open blogging, open source publishing, whatever term you want to apply to it, I think it's a pretty wild thing.
[2824.08 → 2832.48] I think as programmers, as developers, as people who pretty much live on the command line or live in your text editor, embracing these tools can certainly do some fun stuff.
[2832.62 → 2834.52] Like Jeff had mentioned, it's a sandbox for him.
[2834.58 → 2835.46] It's a playground for him.
[2835.46 → 2837.58] And, Brian, it sounds like it's the same thing for you.
[2837.66 → 2846.08] And, Tim, it sounds like the same thing for you, that you're just etching out your areas of your craft through blogging and through this type of blogging.
[2846.14 → 2847.34] So I think it's a pretty wild thing.
[2847.48 → 2849.66] Wynn, you want to – you got anything to say about it?
[2850.18 → 2851.22] I'm just – I'll say it again.
[2851.28 → 2856.92] I'm waiting for that NoSQL stash the hash engine in my browser that everybody's so excited about server-side.
[2857.04 → 2864.84] I'd like to – when we get done playing with JavaScript back on the server to put it back in the client, I'd love to have that type of engine in the browser.
[2864.84 → 2869.16] But, yeah, thanks for taking the time, everyone, to talk about this particular topic.
[2869.42 → 2879.02] It's definitely on our radar as we look to grow the changelog blog beyond Tumblr and look to kind of remove the distance between writing and coding.
[2879.78 → 2883.42] Anybody have any fun conferences coming up that you want to plug or mention before we head on?
[2884.42 → 2889.96] Texas.js is coming up this summer, and they actually got me speaking in that, so I got a ticket.
[2890.54 → 2890.94] Absolutely.
[2890.94 → 2894.50] And we're actually – the changelog is going to be a media partner with Texas.js, too.
[2894.50 → 2901.86] So we'll be working with Rebecca on promoting it, so the audience don't get upset when we talk about it because it's a cool thing.
[2901.96 → 2905.16] It's all JS all day in big old Texas.
[2905.76 → 2906.34] Anybody else?
[2907.02 → 2910.72] I'll be going to Lesson on May 21st.
[2910.92 → 2912.50] So come there.
[2912.60 → 2913.08] We can hang out.
[2913.56 → 2914.04] Yeah, Lesson.
[2914.12 → 2915.24] I can definitely speak against Lesson.
[2915.50 → 2917.72] That's an awesome conference.
[2917.72 → 2921.48] It was the first last year and again this year, and I look forward to going there myself.
[2922.26 → 2922.52] Well, cool.
[2922.52 → 2923.02] All right.
[2923.10 → 2928.18] Well, guys, thanks again for taking the time to speak with me and Won and the audience of The Change Law.
[2928.28 → 2931.80] We certainly respect each of you in your own rights and everything you guys are doing.
[2931.90 → 2932.46] Keep doing it.
[2932.50 → 2933.02] Don't stop.
[2933.82 → 2936.92] Love this open source world, and thanks for taking the time to come on the show.
[2937.06 → 2937.52] Appreciate it.
[2937.76 → 2937.92] All right.
[2937.92 → 2938.14] Thanks.
[2938.32 → 2938.52] Awesome.
[2938.66 → 2939.16] Thanks for having me.
[2939.16 → 2947.90] Thank you for listening to this edition of The Change Law.
[2947.90 → 2955.88] Breakup.com to find out what's going on right now and open source.
[2955.96 → 2965.50] Also, be sure to head to GitHub.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Change Law.
[2965.50 → 2995.48] We'll be right back.
[2995.50 → 3025.48] We'll be right back.
