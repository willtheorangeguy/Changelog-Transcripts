[0.00 --> 13.76]  welcome back everyone this is the change log where a member supported blog and podcast they
[13.76 --> 17.60]  cover what's fresh and what's new in open source you can check out the blog at the changelog.com
[17.60 --> 23.86]  and our past shows at 5x5.tv slash changelog uh this show is hosted by myself adam stakovic and
[23.86 --> 29.68]  also andrew thorpe andrew say hello my friend hey how's it going man my lips are sticky
[29.68 --> 34.84]  yeah i hear you yeah so speaking of sticky lips tuning live every tuesday at 5 p.m central
[34.84 --> 41.08]  standard time right here on 5x5 and this is lucky number episode 97 and we're joined by drew blass
[41.08 --> 46.54]  a devops engineer at chargeify he's a fellow rubyist and is starting a devops class next month
[46.54 --> 52.96]  called ultimate devops academy so drew welcome to the show thanks a lot andrew i'm gonna let you
[52.96 --> 57.40]  i'm gonna let you steal this one away today because you invited drew on the show i know he's awesome
[57.40 --> 62.50]  but i i just don't have the uptake on him quite as much as you do yeah that's fine i'll kind of
[62.50 --> 69.18]  give a little intro i uh was out in uh san francisco like two or three years ago and actually went out
[69.18 --> 75.56]  to uh to dinner with lance wally drew and obviously you know who that is he's a guy over at chargeify
[75.56 --> 81.14]  um so i reached out to him not long ago and just said hey is there anyone at the chargeify i know
[81.14 --> 86.38]  chargeify specifically is the core is not open source but you know you guys are involved in open source
[86.38 --> 91.46]  you're very active in open source some of the you know pieces of chargeify have been open sourced
[91.46 --> 98.66]  um so is there anyone there that you'd like to have on the show and then drew came about so so here you
[98.66 --> 103.40]  are drew why don't you give us a little bit of a uh intro to who you are what you do at chargeify
[103.40 --> 109.74]  you know what kind of what kind of stuff chargeify is doing in the open source world sure so uh you know
[109.74 --> 115.98]  i joined chargeify about a year ago and it's been a really great transition for me um you know i'm
[115.98 --> 123.52]  traditionally a developer and with them uh i've been recently doing a lot of operations work so
[123.52 --> 130.34]  kind of bridging some of that gap and focusing on our infrastructure and uh lets me play with all
[130.34 --> 136.56]  sorts of cool open source tools and uh chargeify if anybody doesn't know does uh recurring subscription
[136.56 --> 143.10]  credit card billing so if you're building your own sas app and want easy plug-in uh credit card
[143.10 --> 150.42]  subscriptions uh that's what we do and so you know we leverage a lot of of big name open source doing
[150.42 --> 159.14]  that uh not just rails uh of course we're we're heavy uh users of the active merchant gem and uh and
[159.14 --> 162.86]  you know we work hard to contribute back to as many of the things we use as possible
[162.86 --> 167.58]  the cool part about that is that uh active merchant started out to open source too so
[167.58 --> 172.32]  y'all use it and then contribute back as well so yeah yeah it's a it's a really good feedback cycle
[172.32 --> 181.70]  so specifically with chargeify um i noticed that obviously the api wrappers are open source and
[181.70 --> 187.62]  that's a pretty common thing because you know you release it via you know publicly available ruby gem so
[187.62 --> 193.20]  uh you know that's a pretty common for a company to open source something like that but but you guys
[193.20 --> 198.54]  well here why don't you give us a little bit of the uh insight into you know what it looks like to
[198.54 --> 202.98]  work on the specifically the api wrapper and who in-house works on that and how do y'all manage the
[202.98 --> 208.84]  uh open source project so you know we've got quite a few open source projects in addition to just the
[208.84 --> 214.84]  uh wrappers you know we have wrappers obviously for a large number of uh of different languages because uh
[214.84 --> 220.52]  um you know we want to be as compatible as possible and so you know we've always got everybody kind of
[220.52 --> 226.70]  pitching in to help out and uh and maintain those and of course we can't have a developer in every
[226.70 --> 233.38]  language so that's where the open source community at large really uh comes in helpful to uh work side
[233.38 --> 238.48]  by side with us and making sure they're up to date and they handle changes that we might make to the api
[238.48 --> 243.16]  and stuff like that and uh so you know that's a really good part of it and then of course all the
[243.16 --> 251.84]  tools that we're using uh internally uh we we try and separate those out into into pieces that we can
[251.84 --> 258.38]  then push back out into the community um you know shopify did that when they first opened up uh the
[258.38 --> 265.12]  active merchant gem and uh uh you know so we try and follow a lot of that same sort of philosophy take
[265.12 --> 271.14]  any of the pieces we can and then get them back out there i heard uh talk just today about about a new
[271.14 --> 279.32]  one for doing uh worldwide uh iso region um management for like lists of all the different
[279.32 --> 286.78]  principalities uh and things that uh and integrating that into rails so we're always looking for ways we
[286.78 --> 293.42]  can extract that stuff out gotcha so that's a like i said that's a kind of a standard procedure
[293.42 --> 299.44]  for how some of the companies that um you know work with open source kind of operate but you guys do
[299.44 --> 304.92]  a few things that are different over and operate over at chargeify uh specifically you've open
[304.92 --> 313.54]  sourced um docs.chargeify.com um so yeah that's a that's a really cool one uh because it anywhere
[313.54 --> 318.40]  that we might be lacking we we usually get pretty quick feedback for somebody to just go in and
[318.40 --> 326.10]  throw up a pull request and say uh you know hey this wasn't explained really well and uh or here's a
[326.10 --> 330.52]  better way to explain this or anytime there's something like that and then on top of that we
[330.52 --> 336.96]  took our actual cucumber features from uh you know the closed source part of our app and then put them
[336.96 --> 342.60]  into the docs as well so the exact same cucumber feature that says exactly here's how you make
[342.60 --> 349.88]  an api request and here's what you should expect as a response um that we run our internal tests against
[349.88 --> 355.78]  those are right there in the docs and they're they're uh open source and available for for viewing
[355.78 --> 362.02]  and editing yeah that's a really neat idea so where did do you know where the idea to open source the
[362.02 --> 370.26]  cucumber features came from i don't it's something that happened uh really early on and uh um you know
[370.26 --> 379.34]  the guys we spawned off of uh grasshopper uh which is uh uh telephone exchange 1-800 number service
[379.34 --> 386.68]  and uh uh you know again they were using a lot of of internal open source tools and just thought it
[386.68 --> 393.30]  was a really good way to kind of be as transparent as possible totally yeah i i know that you know
[393.30 --> 397.96]  personally from from my experience one of the companies that i uh that i actually helped start
[397.96 --> 404.02]  with some friends of mine uh my buddy ryan schlessinger he was working with not with chargefi he's using
[404.02 --> 410.30]  chargefi and um the he would kind of give back to a lot of the projects that he was using and i think
[410.30 --> 415.24]  documentation was one of them and he always had very very good things to say about the response he got
[415.24 --> 422.20]  um you know from from his contributions to the open source pieces of chargefi so i think that was
[422.20 --> 430.08]  you know uh a welcome change i think that at times with some of the bigger open source projects you can be
[430.08 --> 435.72]  kind of scared to you know get involved because of the you know sometimes there's some of that elitist
[435.72 --> 440.38]  mentality and chargefi definitely from my experience has never had that you guys have always been very
[440.38 --> 447.82]  open to uh submissions and and ideas and contributions so um is that something that is kind of you know
[447.82 --> 453.62]  how how does that culture get developed in-house like to be very open to that you know uh company-wide
[453.62 --> 460.50]  there's two big things i think that contribute to it the the first one is is easy because uh you know
[460.50 --> 467.84]  there's only a couple of us there's we we have very very little uh outside funding um you know we're
[467.84 --> 475.60]  pretty much just bootstrapped and and uh uh you know expanding with our own profitability and so uh you
[475.60 --> 481.50]  know everybody's kind of really critical to that operation and so anytime somebody from the outside comes in
[481.50 --> 487.62]  and offers help we're certainly more than happy to take it you know we're very ironically very humble
[487.62 --> 494.76]  in that regard and the other one is uh again because of the small team we just all really have a passion
[494.76 --> 502.86]  for for uh you know doing everything we can to to uh do the best we can for our customers in the community
[502.86 --> 507.50]  and um you know that's the attitude you have to have when you have so few people and so
[507.50 --> 513.32]  it just comes naturally you know i don't feel the the i don't feel that i have to you know get
[513.32 --> 518.08]  approval before i turn around and open source something if i've got a tool i've written on
[518.08 --> 523.42]  company time and i say wow this would be this would be perfect to open source i just do it there there's
[523.42 --> 528.96]  you know there's no red tape to that gotcha yeah so speaking of tools that you've written on company
[528.96 --> 533.44]  time i know there's you got you know you told me about a bunch of different ideas you had but
[533.44 --> 539.38]  specifically one of them that you actually uh just open source today i think right did you want to
[540.14 --> 549.06]  kind of yeah sure so today's release is uh called it's called consignment and it's a small web service
[549.06 --> 556.28]  that basically takes incoming messages and uh parses them and then re-dispatches them to other remote
[556.28 --> 563.32]  services and so it's just an easy way i kind of think of it like stats d but for for data
[563.32 --> 569.68]  and information as opposed to just numeric metrics and so you can take things like if you have a cron
[569.68 --> 575.78]  job and when the cron job finishes and puts out a report and instead of just you know shooting off an
[575.78 --> 581.38]  email or something send it into consignment and then consignment can look at it determine what action
[581.38 --> 587.48]  to take and then do it so it might parse the message see if something went wrong and then you know
[587.48 --> 592.82]  if something went wrong it might send a pager duty alert or if everything looks okay it might just save
[592.82 --> 599.04]  it to a database for later reference or it can send emails or do any number of different things
[599.04 --> 605.74]  with whatever logic you write so it's just kind of a centralized way to really easily um pop any kind
[605.74 --> 611.42]  of that information in and then turn around later and set up your rules for how you want to handle
[611.42 --> 616.00]  those messages and you don't have to go back to wherever the message came from and keep keep changing
[616.00 --> 622.32]  things gotcha so this is a uh looks like it's a node project is that something that um is is used
[622.32 --> 627.52]  in-house in charge of fire is that just like a weekend hack project that you so so this is this is
[627.52 --> 635.54]  my first uh open source node project and uh i did node just because i thought it was the the simplest
[635.54 --> 642.88]  way to do uh you know non-blocking there was going to be a lot of back-end calls to you know other
[642.88 --> 648.56]  remote services calling out to pager duty or to an email service and all those things and you know
[648.56 --> 653.96]  node just seemed like the right fit to uh then you don't have to put those into like a background queue
[653.96 --> 662.90]  or something gotcha yeah it's a fun it's a fun thing to uh to to hack on for sure um internally
[662.90 --> 668.50]  though so i you may have said this before i may have just kind of spaced out on it but uh does charge
[668.50 --> 675.06]  if i um do you see any any node happening internally with charge of fire is there any now or
[675.06 --> 680.38]  well we're definitely going to be putting uh consignment into pretty heavy use there's a lot of
[680.38 --> 686.44]  uh lot of places that i can see it fitting in it's it in the same way like like i said with stats d like
[686.44 --> 693.22]  you just throw stats d reporters everywhere and then later on decide if they're useful or not and
[693.22 --> 699.10]  you can you know do your analytics and in graphite or whatever it's it's the same kind of thing oh i'm
[699.10 --> 703.88]  building something and i might want to do something with this information later so i'll just throw it
[703.88 --> 709.58]  out to consignment and then you know it might be six months down the road and i say oh you know i'd
[709.58 --> 714.44]  like to start getting an email about these and you can just update consignment and say hey start
[714.44 --> 720.56]  sending me me an email when this event happens and so uh that's going to be really good i think on our
[720.56 --> 726.86]  on our operations front for things like cron jobs and backup reports and chef reports and all that
[726.86 --> 733.74]  kind of stuff so this uh consignments it's it's brand new released here on the show today so that's
[733.74 --> 739.44]  awesome but uh it seems like you were looking for the solution and you didn't find it can you kind of
[739.44 --> 745.88]  tell the backstory on you know yeah you know i just i just asked around uh i always get a lot of
[745.88 --> 751.72]  success when i uh tweet out and ask my developer friends you know hey have you guys heard of service
[751.72 --> 758.26]  x or something that does this and uh you know i was looking for even a sass app that would do it and i
[758.26 --> 764.84]  just couldn't find anything that that was quite scratching that itch um you know this is sort of a
[764.84 --> 772.86]  it's sort of like a zapier or an if this then that but much more developer focused and uh you know i had
[772.86 --> 778.48]  some specific requirements around writing my own code to be able to parse things later on
[778.48 --> 783.46]  uh just couldn't find anything so i said well i'll just try and throw it together and see what happens
[783.46 --> 793.24]  gotcha so it's a it sprung out of a need sprung out of something that you you know like a need so
[793.24 --> 797.84]  you said you want to roll that back into chargeify so was it or yeah so was it specifically a chargeify
[797.84 --> 802.96]  need or a need that you had personally in a different project or i just felt like it's kind
[802.96 --> 808.94]  of something that comes up a lot anytime i'm i'm doing a new app whether it's with chargeify or
[808.94 --> 815.66]  whether it's you know a personal project or anything or where this same kind of thing just like you know
[815.66 --> 821.86]  statsd applies in so many different circumstances that i would just say oh it'd be nice if i could
[821.86 --> 828.86]  just do this with my cron jobs or something like that and uh uh i you know it came up so many times
[828.86 --> 834.88]  that i finally finally got fed up and when i couldn't find a solution uh i said well it shouldn't
[834.88 --> 841.10]  be too hard to throw something together so i mean the difficulty there was i think the 20th this is the
[841.10 --> 848.86]  23rd so on the 20th you tweeted that out so basically three days plus a half day yeah well uh
[848.86 --> 854.10]  if you if i don't get the answer on twitter within like a day you know it's it's probably buried and
[854.10 --> 861.50]  i'm not going to get the answer so i figured i hadn't heard any responses so uh might as well uh
[861.50 --> 867.94]  not waste any more daylight gotcha so another another little project that you mentioned but i think it's
[867.94 --> 874.06]  i don't know if you are are working on it and haven't haven't open sourced it or um if you haven't
[874.06 --> 881.14]  actually begun working on it but you you said you called it auto cloud so yeah so uh this is the one
[881.14 --> 887.18]  i'm really excited about and uh i'm actually i'm on a sabbatical right now for a couple of weeks with
[887.18 --> 892.82]  charger fi uh to take some personal time and my personal coding project will be to convert this for
[892.82 --> 901.02]  for open sourcing uh it's we use it very heavily internally and what it does is it's an uh
[901.02 --> 908.42]  idempotent control framework for uh amazon web services uh it replicates a lot of what their
[908.42 --> 915.36]  internal uh cloud formation tool does which is you write basically a description of you know what
[915.36 --> 921.08]  instances and what security groups and what network settings you want and then it's responsible for
[921.08 --> 927.08]  making sure that you actually have those configured and set up and running inside aws
[927.08 --> 935.50]  uh but cloud formation is is json based with a lot of sort of kludges to get things like fake
[935.50 --> 942.78]  variables and fake loops and if statements working and it just made a lot more sense uh at least to me
[942.78 --> 951.60]  personally to to just take ruby and um inspect the current state of the network via the api and then
[951.60 --> 957.60]  make the appropriate changes and and that way when you're writing your description and you say hey i
[957.60 --> 964.62]  want to have uh you know 10 instances of this you can just use a regular ruby loop instead of of
[964.62 --> 969.60]  something weird and if you want to have them all belong to a single security group you can use a
[969.60 --> 977.08]  variable to do that instead of instead of again some kind of weird foreign pseudo language so uh
[977.08 --> 983.12]  uh that just fit a lot better with my personal workflow for for managing things and uh it's been
[983.12 --> 988.30]  a super powerful tool for us it kind of turns it into it just like we do at chef where everything's
[988.30 --> 996.20]  idempotent gotcha so this is something that you're using in production at chargeify now yep it manages uh
[996.20 --> 1001.96]  you know all of our launching of instances and making sure you know we have as many as we want and
[1001.96 --> 1007.34]  if we're going to change a security group uh you know you just change the configuration file that
[1007.34 --> 1013.60]  says here's what security group x is supposed to look like and um it goes and it checks and it says
[1013.60 --> 1020.36]  hey the security group out on amazon doesn't quite look like that um let's change it and make it match
[1020.36 --> 1025.88]  up and it's so it handles all that logic gotcha is this actually part of the core of chargeify that
[1025.88 --> 1031.00]  you're going to extract out or is this uh some other way that you're using this right now so it's a
[1031.00 --> 1036.42]  it's a separate app it's basically its own command line tool kind of like chef and so just something
[1036.42 --> 1045.34]  uh that we we run separately uh and it makes all the uh api calls to amazon to do whatever it needs
[1045.34 --> 1051.94]  to do so it's already its own tool but it uh uh you know it's got a lot of our custom logic and
[1051.94 --> 1058.92]  a lot of the library code is mixed in with our actual configuration files so uh it's it's getting
[1058.92 --> 1064.72]  those separated so that it can be a more generic tool that of course takes a lot of time gotcha so
[1064.72 --> 1070.98]  we'll come back to that but this isn't your first hoorah with uh building something around amazon uh
[1070.98 --> 1077.82]  the amazon aws suite so looks like you've you built the uh probably the official the unofficial official
[1077.82 --> 1085.24]  ruby wrapper for ses is that right yeah so uh ses when it first came out uh i was really excited to
[1085.24 --> 1094.96]  use it and they didn't have uh a ruby wrapper for it at the time so uh i went and wrote one that was
[1094.96 --> 1102.82]  specific to it and uh uh you know it's been kind of plugging along ever since uh the api hasn't
[1102.82 --> 1108.02]  changed a lot and they haven't really added anything new to it so you know it's uh it's certainly
[1108.02 --> 1115.40]  lived a very uh long happy life and eventually amazon did release their own version into the
[1115.40 --> 1123.88]  the major ruby aws sdk but a lot of people still like to to target specifically just ses and not
[1123.88 --> 1129.84]  bring in all those other dependencies so gotcha and ses uh for those that don't know it's amazon's
[1129.84 --> 1137.50]  was it simple email service right yep yep so it's just sending you know bulk transactional emails
[1137.50 --> 1143.88]  basically similar to like a send grid or yeah send grid or postmark or mandrill or any of those
[1143.88 --> 1150.92]  gotcha was that the first uh open source project you worked on uh no but it was probably it's it's
[1150.92 --> 1157.14]  one of i think the most successful ones i've worked on so it definitely um it was picked up really well
[1157.14 --> 1164.18]  by the community uh it still gets support requests every once in a while and uh uh you know has had a
[1164.18 --> 1171.14]  lot of pull requests some come in so it's it's definitely been been uh popular and and you
[1171.14 --> 1177.74]  know still requires work to maintain so gotcha yeah one of our previous guests uh mike perham
[1177.74 --> 1183.20]  mike perham from uh sidekick he was telling us about how he got involved in open source like you know
[1183.20 --> 1188.68]  20 years ago or something before you know before github and before like ruby and before
[1188.68 --> 1193.68]  before source forge before source forge he was you know he got involved before there was anywhere to
[1193.68 --> 1198.88]  put your code so it's like nowadays it's hard to imagine you know getting started without a tool
[1198.88 --> 1205.50]  like github or source forge or you know any of the bit buckets out there so uh i i i definitely respect
[1205.50 --> 1211.22]  that so what what was the first uh what what would you say your like intro into open source and and why
[1211.22 --> 1217.40]  you you know got started in that realm was oh i've got a this is a sad anecdote actually my
[1217.40 --> 1225.70]  really my intro into open source was trying to contribute to the rails core um way back in the
[1225.70 --> 1234.44]  days when they were uh they were still on track for their their bug tracking and and uh their pseudo
[1234.44 --> 1243.34]  pull requests and and i submitted uh uh you know patches to the the core for issues that i was having or
[1243.34 --> 1251.44]  issues that somebody else had been reported and i offered to fix um and they uh i probably did this
[1251.44 --> 1256.82]  six or seven times i'd submit a patch and then six months later somebody on the core team would
[1256.82 --> 1262.04]  finally look at it and of course by then it didn't merge cleanly especially when they were on
[1262.04 --> 1266.68]  subversion so they just come and they close it and they'd say no it doesn't merge cleanly thanks
[1266.68 --> 1273.62]  anyway um wow you know let us know when you fix it of course it worked when i submitted it but uh
[1273.62 --> 1283.40]  uh so that was kind of a uh uh depressing start into uh uh trying to to help out and uh luckily luckily i
[1283.40 --> 1290.98]  wasn't deterred though uh and and managed to to keep plugging away at it so what if they would have
[1290.98 --> 1296.04]  accepted it though and then uh and then when they merged it because of they don't have like the
[1296.04 --> 1301.76]  pleasures of git couldn't like submit it with you you know like the merge like like it doesn't get
[1301.76 --> 1309.70]  up you know oh i mean i don't get credit i don't i don't know that i care about that but i mean like
[1309.70 --> 1314.12]  getting the point like oh i contributed to xyz you know that that's what i mean like yeah that's
[1314.12 --> 1322.76]  that's nice too although if i if i recall like back in the uh uh early days of uh uh there was a
[1322.76 --> 1327.74]  script that would check if you had contributed something like if you had contributed a patch
[1327.74 --> 1334.86]  and it actually checked like the track log to see um if an issue that you had submitted a patch on
[1334.86 --> 1340.64]  had been accepted or something so there was still a way to see even if your name wasn't on the actual
[1340.64 --> 1348.32]  commit gotcha so the ultimate dev ops academy where did this uh where did the idea to do this
[1348.32 --> 1355.94]  come from so uh it's just something i had kind of been thinking about for a long time um uh you know
[1355.94 --> 1363.20]  i've been doing a lot of different things to try and help uh mentor and teach uh i've been trying to
[1363.20 --> 1372.88]  get my uh public speaking chops up uh i was at uh uh mountain or yeah mountain west ruby comp and uh
[1372.88 --> 1380.64]  several others uh giving talks and and uh doing rails hotline and stuff like that and so uh i don't
[1380.64 --> 1386.60]  know i think this just came naturally from that that uh it was it was an area where where a class would
[1386.60 --> 1393.04]  be helpful and be a little more effective than doing a lot of one-on-one work and so i decided to
[1393.04 --> 1398.96]  launch the ultimate dev ops academy and uh see if there was anybody interested have you got any
[1398.96 --> 1404.88]  have you got any interest in it early yet i mean yeah yeah so far uh the interest has been really
[1404.88 --> 1411.02]  good and uh the feedback's been really positive we still have seats available though it starts august 12th
[1411.02 --> 1415.94]  um ultimate devops.com which i thought that was a pretty awesome domain name to still be available
[1415.94 --> 1423.62]  so uh uh uh just goes to show you that dev ops hasn't uh you know become too mainstream yet or
[1423.62 --> 1428.70]  else you wouldn't be able to get a domain like that but uh so so yeah there's still seats available and
[1428.70 --> 1436.82]  uh uh you know i'd love to have more people join up and um i'm i'm excited to uh you know i think it's
[1436.82 --> 1442.92]  going to be a good opportunity to reach out to a lot of people at once and uh then the the big goal
[1442.92 --> 1451.66]  is uh using the benefit of of the the uh paid attendance which is really paying for my time to
[1451.66 --> 1458.04]  do a lot of one-on-one work and help and support that uh you know just like if you need to call me
[1458.04 --> 1462.68]  and ask questions and stuff like that but then it's also going to i think generate a lot of of material
[1462.68 --> 1468.92]  uh you know lesson plans and everything like that that i can i can turn around and give back to the
[1468.92 --> 1475.46]  community as well i was going to ask because we just had the last show we had jesse welcome on the
[1475.46 --> 1481.20]  show and he runs ruby off rails and part of his huge selling point to that course so if you're
[1481.20 --> 1487.72]  looking to learn ruby that's a really good thing because during the process of his course he's he
[1487.72 --> 1492.68]  acts basically as a mentor to you you know so it seems like you're trying to do the same thing with
[1492.68 --> 1499.28]  uh with this to be able to kind of work one-on-one with someone yeah and and uh uh so i'm really
[1499.28 --> 1503.90]  excited about it i think it's i think it's going to go off really well and uh starts here in a few
[1503.90 --> 1511.46]  weeks and uh by the end of it i'll have a ton of you know live videos and lesson plans and and
[1511.46 --> 1517.12]  everything and uh so of course six months later i'll all be out of date and i'll have to start all
[1517.12 --> 1522.52]  over again but that's the life we lead yeah is are you going to be hitting on vagrant at all in the
[1522.52 --> 1529.44]  course i am yeah yeah it'll definitely be a part part of it uh and is i'm going to try and hit a
[1529.44 --> 1536.08]  little bit of everything but also uh go pretty in depth i mean we're going to take a a pretty decent
[1536.08 --> 1542.54]  sized rails app and turn it into a a complete production environment you know so we're not just
[1542.54 --> 1546.76]  going to be playing around with little bits and pieces but we're going to have you know full
[1546.76 --> 1553.56]  redundancy uh you know full operationally sound infrastructure on which you could could run you
[1553.56 --> 1559.62]  know serious traffic on and uh you know i think sometimes there's a pretty big gap between the
[1559.62 --> 1565.82]  intro tutorials that a lot of people get into and then really being able to to you know batten down
[1565.82 --> 1573.08]  the hatches yeah it's a topic that we actually talk about often on the changelog and it's uh kenneth who
[1573.08 --> 1579.46]  you know was potentially going to join us but apparently fell off the earth uh wow we love
[1579.46 --> 1585.76]  kenneth um he he hit on it early you know earlier on you know a few months ago he said uh it's like
[1585.76 --> 1591.74]  this tribal knowledge right there's this gap between like beginner and expert and that's like the tribal
[1591.74 --> 1595.66]  knowledge region where you just have to kind of throw yourself into the fire and learn as you go and
[1595.66 --> 1601.86]  and uh it sounds like this is a great step in that direction of helping to share that tribal knowledge
[1601.86 --> 1611.06]  in a um in a you know strategic uh structured manner so yeah what would you say the level of the i i guess
[1611.06 --> 1614.52]  the the i don't know if you're calling them students or not you're calling it academy so i gotta imagine
[1614.52 --> 1620.18]  they're called students but registries people that come and take the course with you this intensive like
[1620.18 --> 1626.88]  what is the level that they need to be at with devops so i i would say you should be a programmer
[1626.88 --> 1632.68]  and obviously it might be a little easier for ruby programmers because uh we're going to be focusing
[1632.68 --> 1640.88]  on chef although uh i kind of make the disclaimer that a lot of this you know the lesson plan is is
[1640.88 --> 1649.44]  revolved around goals so doing things like your goal is to you know write uh an automation script that
[1649.44 --> 1654.42]  gets you to a certain state and you could do that with puppet or you could do it with ansible or salt
[1654.42 --> 1659.96]  stack or whatever uh so it doesn't have to be chef but uh you know uh obviously i'm going to teach what
[1659.96 --> 1669.34]  i know best and um so it should be developers who who have programming experience and uh you know maybe
[1669.34 --> 1675.56]  don't have the the operation chops that they like you know uh which which i think comes up a lot you
[1675.56 --> 1681.54]  you get developers who can write lots of great code um and that's great when you have no customers
[1681.54 --> 1686.10]  but then you turn around the next day and your app's really popular and now your problem isn't
[1686.10 --> 1691.96]  writing your new features the problem is keeping things running and uh you know scaling and expanding
[1691.96 --> 1698.32]  for the users that you have i gotta take a little chuckle though publicly on your second line on
[1698.32 --> 1703.90]  knowledge prerequisites for the course uh it says highly recommended to be able to read understand and
[1703.90 --> 1709.36]  write simple ruby programs but then you also put in uh parentheses work through try ruby.org at least
[1709.36 --> 1720.12]  twice how's it cool well i mean i guess i don't want to scare anybody away but uh um uh i don't know so
[1720.12 --> 1728.48]  so so that's tough i i i'm sure i'll have a wide variety of of ability levels and you know it's it's
[1728.48 --> 1734.20]  certainly i i make no bones that it's my first time doing a course in this fashion i've taught a
[1734.20 --> 1741.52]  lot of in-person courses uh before but never never an online one and so you know i'm gonna have to take
[1741.52 --> 1749.12]  take a uh take stock of of the people in the class and and some of them might have it easy and some of
[1749.12 --> 1755.06]  them might need more help and uh you know i'll just have to have to help where where i need to
[1755.06 --> 1764.40]  so the the class is gonna be uh is it twice a week or what is the well it's it's one lesson a week
[1764.40 --> 1772.82]  and what what i'll be doing is i'll i'll record i'll record the video um i'm actually working through
[1772.82 --> 1781.42]  like doing some test recordings this week um and and then put the video out and and kind of go
[1781.42 --> 1788.40]  in a pseudo live fashion alongside with the students so you know if we need to to stop and
[1788.40 --> 1793.32]  talk about things or whatever we can but then they've also got the the whole video to refer back
[1793.32 --> 1801.38]  to so it's one lesson per week but we're going to have multiple um you know live chat and and uh live
[1801.38 --> 1809.06]  audio sessions to to talk about what's going on and answer questions gotcha so the first the cost of
[1809.06 --> 1816.10]  this class is 999 so it's definitely an investment but one that's uh worthwhile but after the initial
[1816.10 --> 1820.92]  um course you said you mentioned that you potentially would like to release like
[1820.92 --> 1830.04]  open courseware i think as you put it yeah so um so you know what what i'll probably do is is um
[1830.04 --> 1839.50]  try and package together um a good portion of it and and uh you know release it for for free use
[1839.50 --> 1845.64]  and uh you know to help as many people as i can i mean there's no use in me holding on to it and
[1845.64 --> 1852.62]  keeping it to myself and like i said you know it'll be outdated in a year so uh right uh you know let's
[1852.62 --> 1859.04]  let's make use of it while it's while it's still good stuff to have any plans to do something like
[1859.04 --> 1864.74]  uh for those that are familiar with like a ruby cones something like that to kind of step somebody
[1864.74 --> 1870.68]  through enlightenment of of devops not so much ruby itself but devops um you know i think it'd be a
[1870.68 --> 1877.70]  really good idea i i bet a lot of this uh might do the same thing in the in the goals from the lessons
[1877.70 --> 1885.04]  and uh we'll just have to see how how it goes uh i definitely have my work cut out for me just for
[1885.04 --> 1890.84]  this so uh i'm pretty focused on it well if you're listening now or on the podcast and you plan to go
[1890.84 --> 1900.44]  to this give drew some slack it's his first time go around so share some grace yes so well cool it
[1900.44 --> 1907.06]  sounds really uh sounds like it's going to be a fun time uh it's ultimate devops.com to plug that for
[1907.06 --> 1913.74]  you uh definitely good luck with that hope it's uh turns out to be incredible for you yeah thanks
[1913.74 --> 1920.34]  very much kind of wanted to roll back into the uh uh auto cloud that we were talking about before um
[1920.34 --> 1926.34]  when you guys are sitting around and in chargeify uh we may have kind of touched on this but uh what
[1926.34 --> 1932.46]  it was this something that you wrote uh that you spent like i don't know what your you know process or
[1932.46 --> 1937.88]  what your internal team you know how your roles are split up or anything but was auto cloud something
[1937.88 --> 1945.26]  that you kind of rolled mostly yourself or was this a team project or internally now um it was just
[1945.26 --> 1951.08]  kind of something that came out of my personal needs uh it wasn't like an initiative that was dictated
[1951.08 --> 1958.82]  from the top or anything like that it was just um you know we make very very heavy use of automation
[1958.82 --> 1966.44]  for for managing the individual servers and it's a lot like test-driven development once you get into
[1966.44 --> 1977.80]  that um code as configuration sort of mindset for your systems um it kind of felt it felt wrong to be
[1977.80 --> 1987.56]  going into the uh you know the amazon management console to make a security group change or or manually
[1987.56 --> 1993.28]  writing an individual api call to launch a new instance and it was like these are the types of
[1993.28 --> 2000.74]  things that just like with with uh when you're doing chef or puppet that you you want to have in a
[2000.74 --> 2007.24]  repository and that way you know you've got a log of the changes hey on this date i added this
[2007.24 --> 2014.20]  rule on this date i added uh five new servers to this auto scaling group you know all these kind of
[2014.20 --> 2020.78]  things and then you've already got you've always got a very authoritative source for for what's going
[2020.78 --> 2026.86]  on not just on your individual servers but on your infrastructure as a whole and uh so you know it's
[2026.86 --> 2033.08]  it just seemed like a very good complement to that and when we didn't have anything like that it you
[2033.08 --> 2040.60]  know it kind of it feels wrong you can feel it in your gut yeah it's uh so you're you said you're on
[2040.60 --> 2046.00]  like a sabbatical from chargeify right now is that for to work on ultimate devops or are you going to
[2046.00 --> 2052.10]  work on autocloud or what what are you doing on your sabbaticals you put it uh it's well it's a
[2052.10 --> 2059.28]  really long vacation just so uh uh you know doing a lot of family things and also just taking some time
[2059.28 --> 2067.82]  to you know code on whatever i want to code with with you know kind of no uh deliverable milestones
[2067.82 --> 2074.84]  hanging over my head and and work on what interests me or play with things um the big one for me lately
[2074.84 --> 2082.64]  is i've been working through the uh matisano security challenges yeah um and those are super fun
[2082.64 --> 2089.54]  and after i did them the first time i went back through and i rewrote all of them in go so uh again
[2089.54 --> 2095.02]  just you know fun ways to do cool things in in programming that i don't get to do every day
[2095.02 --> 2102.14]  and so that's what i'm doing with my spare time cool yeah so uh with mitchell uh hashimoto we've
[2102.14 --> 2106.80]  had him on the show from vagrant uh we've had solomon hikes or just a few weeks ago on the show
[2106.80 --> 2114.38]  from dot cloud and docker um you know mitchell was he he built vagrant out of a need internally he had
[2114.38 --> 2120.62]  for uh i can't remember the company he was at but they had a need for it and um and he worked on it and
[2120.62 --> 2125.78]  then it became really popular so he left his company in his case and you know in good very
[2125.78 --> 2131.62]  good graces and everything but left to work on vagrant full-time uh solomon hikes today he was
[2131.62 --> 2138.44]  the ceo of dot cloud and um they started docker and he today announced that he hired a ceo to replace
[2138.44 --> 2145.90]  himself so that he could become the cto and focus full-time on docker um smart yeah i mean it's and he's
[2145.90 --> 2150.46]  very excited about it so it's big news and you know i think the whole community could could be
[2150.46 --> 2155.98]  excited about that to know that uh that you know docker is taken off and it's going to get some big
[2155.98 --> 2161.68]  legs behind it to go you know even even harder in development so let's say auto cloud kind of starts
[2161.68 --> 2167.18]  to take off in the same mold and you know becomes a bit a real popular tool and and chargeify says you
[2167.18 --> 2172.02]  know we'd love for you to kind of lead this project up specifically and and maybe not even work
[2172.02 --> 2175.96]  on the chargeify core anymore would you welcome something like that is that something that would
[2175.96 --> 2184.86]  interest you or uh it definitely would um but you know i i don't know it's it's not quite in the same
[2184.86 --> 2193.90]  league like i mean personally docker is one of the is i'm such a huge fan boy of docker and um you know
[2193.90 --> 2200.84]  i'm waiting with bated breath for the day that they stick a production ready label on it um so that i can
[2200.84 --> 2209.68]  start i you know replacing huge swaths of our infrastructure to use it um but you know i i
[2209.68 --> 2215.54]  think auto is quite quite a bit simpler of a tool than that you know it's not it's not on the same
[2215.54 --> 2223.60]  level as something like chef it it's it's smaller and um you know it doesn't even necessarily need
[2223.60 --> 2233.14]  full-time um you know work on it or improvements because uh you know i mean really all it's doing
[2233.14 --> 2240.74]  is is just making one configuration match another configuration and i hope to just have it kind of
[2240.74 --> 2247.76]  grow naturally and as somebody you know we have it built to do security groups and then tomorrow if
[2247.76 --> 2255.08]  somebody says oh i'd like for it to be able to manage you know some other aws component you know
[2255.08 --> 2259.34]  then they can add that and then the next day if somebody says oh i wish this would work for
[2259.34 --> 2268.42]  rackspace cloud instead um well great i hope uh you know we can make that happen too but uh um yeah
[2268.42 --> 2274.70]  that's the path that you seem to see a lot and i can i think that's kind of why i was asking is
[2274.70 --> 2279.28]  because they start off as you know these a lot these much smaller projects and they kind of grow
[2279.28 --> 2284.16]  into these when they kind of get grow in popularity then people say well this is awesome and i just want
[2284.16 --> 2289.80]  to mold it a little bit to use it you know in this way and it starts to kind of take off and grow uh
[2289.80 --> 2296.08]  grow legs and become a whole different monster so um that's the beauty of open source software though
[2296.08 --> 2302.44]  that's you know with vagrant he was mitchell was telling us that you know different um images that you
[2302.44 --> 2307.40]  know he's had community support to write different you know support for different images and it was a
[2307.40 --> 2313.04]  you know i mean that's the beauty of it you don't it's not all on you to do everything and um you know
[2313.04 --> 2318.56]  you can just kind of manage people that as they need different pieces they can kind of get get them
[2318.56 --> 2323.28]  in there so yeah that's the beauty of open source man that's why we do what we do
[2323.28 --> 2332.12]  plus it's nice to have people who like using the things that you wrote well yeah definitely it's
[2332.12 --> 2337.16]  also it's nice for people to tell you how awesome you are yeah say it again
[2337.16 --> 2348.32]  all right so everyone that uh listens to the changelog uh knows that we kind of asked two
[2348.32 --> 2355.20]  questions on every every uh guest that we have on there and the the first one i'll ask you drew to
[2355.20 --> 2361.22]  kind of to uh get your input on is for a call to arms so uh whether it's something with chargeify
[2361.22 --> 2367.38]  or something that you know you've worked on specifically um you know with devops or uh
[2367.38 --> 2371.92]  consignment or anything like that do you kind of have a call to arms whether you would love to see
[2371.92 --> 2380.20]  the open source community get involved and help out with something um you know the the honest truth
[2380.20 --> 2390.76]  is i i just like to to have more people contributing overall like um you know there's so many open source
[2390.76 --> 2400.16]  projects um out there that need help uh especially the smaller ones and i think a lot of people use more
[2400.16 --> 2406.54]  of them than they realize you know just like if you go through your gem file and look at how many
[2406.54 --> 2416.76]  uh little gems that you might use on a regular basis and who have authors who you know need help or or need
[2416.76 --> 2424.18]  new features or have issues um it's so easy to find those and thanks to the wonder of github you know
[2424.18 --> 2430.04]  help find an open issue and and do a pull request for it and i think there's still lots of developers
[2430.04 --> 2440.04]  who get intimidated or or um you know just don't get involved in and uh there's so many easy paths to it
[2440.04 --> 2444.06]  and i there's a lot of great i wish i knew the name but there's a lot of great services out there now
[2444.06 --> 2453.64]  that uh will help you uh uh find open issues um for projects you care open on projects you care about to
[2453.64 --> 2461.84]  to be able to jump in and uh uh help out so you know i say the call to arms is do something yeah
[2461.84 --> 2466.14]  so let's just sit on the sideline that's something that we talk about a lot on the changelog is
[2466.14 --> 2472.86]  you know people when i go to you know uh conferences or just like my local ruby groups and people ask me
[2472.86 --> 2478.00]  a question like how do i get involved with open source what do i do i'm like just find something you care about
[2478.00 --> 2482.88]  just start doing it it's like you know find a project that you care about and go and look at
[2482.88 --> 2488.92]  their issues and start start contributing code and you find that the majority of times um when you
[2488.92 --> 2494.00]  when you get involved when you you know try to start getting involved the community is very
[2494.00 --> 2500.78]  supportive and very helpful and if you're you know honest about you know this is my first time
[2500.78 --> 2505.82]  getting involved with open source uh not that they hold your hand but they you know you just find it's a
[2505.82 --> 2510.10]  pretty welcoming community and most projects that are very active in open source they kind of have
[2510.10 --> 2514.74]  their guidelines and their standards and what you should or shouldn't do when contributing to open
[2514.74 --> 2520.62]  source so like you said we just tell people just just start just start doing that's that's kind of the
[2520.62 --> 2528.04]  key and the truth of the matter i think and almost universally but especially on bigger projects um i know
[2528.04 --> 2534.62]  the rails core team has said this many times in the past is what most open source projects need
[2534.62 --> 2542.06]  is not somebody who like knows the internals to go and code a solution what they need is a secretary
[2542.06 --> 2550.32]  like they need help from the community to look at open issues and try and reproduce them like
[2550.32 --> 2555.22]  somebody will open an issue and say here's my problem and it sits there because nobody knows like
[2555.22 --> 2560.06]  what the real cause is so what they really need is like hey look at it if there's not enough
[2560.06 --> 2565.88]  information respond to the original poster and you know ask for the information or try to reproduce
[2565.88 --> 2572.06]  it yourself follow the steps and then see if you can dig a little bit deeper than the person before you
[2572.06 --> 2577.84]  did and you know kind of unlock the key so that one of the core developers can just you know knows
[2577.84 --> 2583.48]  exactly what he needs to do to fix it sort of thing so all that triage and just that user interaction
[2583.48 --> 2590.66]  and and that's all you know that's all you have to have is a grasp of the english language um you
[2590.66 --> 2595.60]  know you don't have to know the internals of the project you want to help out yeah that's that's
[2595.60 --> 2601.24]  certainly an easy way to to kind of i mean that's kind of how we handle bugs at at pure charity i mean
[2601.24 --> 2606.62]  we do the same thing we report bugs and the very next step is to validate them it's the same case here
[2606.62 --> 2611.14]  it's like you know you're reporting an issue it's it's a bug with the the project or whatever but
[2611.14 --> 2617.78]  that's pretty neat so we um you weren't on the last show andrew but uh i started to ask this new
[2617.78 --> 2621.18]  question i thought it was kind of neat but it doesn't always apply so it's not always like your
[2621.18 --> 2627.00]  exact every show question but i figured for drew it might it might make sense so drew if you weren't
[2627.00 --> 2635.44]  programming in ruby what would you be programming in um i the tough part is there aren't many languages
[2635.44 --> 2642.34]  languages that i don't enjoy um you know every it's every new language comes out i go boy i wish i could
[2642.34 --> 2649.08]  just do that all the time um so you know i i wish for the perfect language that did whatever i want
[2649.08 --> 2660.40]  um i'm lately i'm a really big fan of go and i've also been trying to uh you know just spread out into
[2660.40 --> 2665.30]  into just about anything so that's exactly what jesse said last week too when i asked the question
[2665.30 --> 2671.92]  he's like i want to i want to learn go yeah that's two in a row if you kind of like uh ruby and but
[2671.92 --> 2677.88]  you you know you'll like what i found because if ruby and go both are kind of like interesting to you
[2677.88 --> 2682.44]  steve klabnik who you know most people know we we have him on the show every once in a while he uh
[2682.44 --> 2689.88]  he's a big proponent of rust the uh new-ish mozilla language that uh is out and i encourage people to
[2689.88 --> 2694.26]  check it out it's a really cool it's a really cool it's got a book on it too doesn't he yeah it's
[2694.26 --> 2698.98]  like a ebook that um is in constant development because the language is so young in constant flux
[2698.98 --> 2705.50]  but yeah yeah rust definitely worth checking out too i i've you know i read a lot of the theory behind
[2705.50 --> 2711.66]  rust and it really resonated with me and of course just like every other language i read i go yes this
[2711.66 --> 2716.62]  sounds like a wonderful idea that's funny i thought i was the only person that that happened to and i
[2716.62 --> 2721.06]  thought there was something wrong with me because every time i read a uh something about a new
[2721.06 --> 2728.26]  language i'm like this is it the perfect language but it's never the perfect language never so so rust
[2728.26 --> 2733.90]  i think if it starts getting the same kind of traction that uh that go has been getting lately
[2733.90 --> 2742.48]  um i'll definitely take a bigger interest in it gotcha so our last uh i guess standard question
[2742.48 --> 2748.46]  that as you called them adam which i think is a good way to describe them is for a programming hero
[2748.46 --> 2756.16]  so someone you want to give a shout out to drew sure um you know everybody that i i meet in the
[2756.16 --> 2763.34]  at conferences and everything is is so uh you know are always so genuine and so very nice it's it's
[2763.34 --> 2769.40]  really it shocks me all the time but uh you know a couple stand out in my mind james edward gray uh who
[2769.40 --> 2777.06]  who lives pretty close to me in uh in oklahoma and uh he's a really awesome guy and he uh definitely
[2777.06 --> 2784.06]  does a lot of contributing to open source um and evan light is a good friend of mine so a shout out to
[2784.06 --> 2791.62]  him and uh he just joined uh basho and he's going to be doing some erlang hacking so i'm pretty excited
[2791.62 --> 2798.96]  for him about that and uh my boss at chartify michael clatt he's a pretty cool guy too so uh he he
[2798.96 --> 2806.62]  definitely knows how to uh have a cool culture that you want to work for so uh quick plug chartify
[2806.62 --> 2816.96]  is hiring if anybody uh ruby on rails dev so yeah i i uh i think was it was evan light he's the one
[2816.96 --> 2820.90]  with the he was very open about a lot of the personal stuff that he was going through yes yes
[2820.90 --> 2826.78]  that's correct so yeah i remember reading through his stuff and just was uh incredibly taken back by
[2826.78 --> 2834.80]  his candor and um i mean yeah he's uh he's a man with a a bigger heart who uh you know he's tested
[2834.80 --> 2841.22]  every single day and uh so my heart goes out to him for sure yeah great guy though for sure absolutely
[2841.22 --> 2848.24]  cool i guess uh i guess since we're done with these standard questions we can go with these standard
[2848.24 --> 2855.76]  clothes of the show uh no and drew was it was good having his show i i uh i knew uh andrew line up a
[2855.76 --> 2861.46]  good show when he had you on and we're big fans of chargeify i think the story of chargeify for those
[2861.46 --> 2866.98]  listening that may not know it i mean y'all have a pretty wild story with how you kind of grew out of
[2866.98 --> 2873.86]  grasshopper labs and um i just think the story of the last five years of grasshopper and or sorry um
[2873.86 --> 2881.10]  chargeify has been really really cool so yes it's you know for for we're kind of in part of the old
[2881.10 --> 2886.28]  guard ironically being only five years old but uh you know that's a long time in this world and uh
[2886.98 --> 2895.10]  um you know so we've got that and we we've kept it kept it small and uh um you know it's really it's
[2895.10 --> 2899.40]  really been a good ride for us so we're really happy with that you mentioned on the show too like
[2899.40 --> 2904.94]  uh i think closer to the middle somewhere in there but you mentioned how you guys grow organically
[2904.94 --> 2910.30]  based on you know your actual company's growth and that's just something i've seen you know from
[2910.30 --> 2915.84]  you guys and have just always been um taken back by that and always respected the way that you've
[2915.84 --> 2921.26]  approached the market and approached growth of the company too and the michael that you mentioned as
[2921.26 --> 2924.88]  one of your heroes that at chargeify is he one of the old guards because i remember somebody named
[2924.88 --> 2931.70]  michael i met a while ago yeah he's uh you know he was uh back with grasshopper and he he basically
[2931.70 --> 2939.48]  is is the first man to uh to code on chargeify back when it was still a grasshopper internal product
[2939.48 --> 2946.26]  michael and i met up at a future of web apps back in 2008 so i i know for sure that was yeah that was
[2946.26 --> 2956.74]  2000 no that was 2010 2010 2010 we met up so so yeah it's uh it's a nice it's a nice attitude and it uh
[2956.74 --> 2966.54]  you know it's it lets us kind of guide our own ship and uh uh lance uh the who's the ceo he's uh you
[2966.54 --> 2974.30]  know a very genuine very open guy um uh you know he just he plays with his hand on the table and uh
[2974.30 --> 2979.12]  it's a very refreshing yeah i'll let this just say because you mentioned the jobs there so if
[2979.12 --> 2983.54]  you're listening to the show i mean great place to work so if you're a rubyist or we're gonna work on
[2983.54 --> 2990.80]  on their stuff uh head on over and say hello but uh this has been episode 97 of the change
[2990.80 --> 2995.24]  we're almost to 100 andrew can you believe that so close we need to have a big party or something so
[2995.24 --> 2999.18]  close we'll have to have like an all-day change log or something like that you know for episode 100
[2999.18 --> 3003.40]  or something we'll have to do something like nobody wants to listen to us talk that much all day live
[3003.40 --> 3008.12]  nothing but the change log all open source all live but uh thanks drew for coming on the show
[3008.12 --> 3012.10]  let's uh let's all say goodbye all right thanks so much man see ya
[3012.10 --> 3014.10]  you
[3033.40 --> 3044.10]  you
[3044.10 --> 3045.10]  you
[3045.10 --> 3046.10]  you
