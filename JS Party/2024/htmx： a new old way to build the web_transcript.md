[0.00 --> 15.70]  this is jsparty your weekly celebration of javascript and the web new year same web dev
[15.70 --> 21.20]  podcasting goodness share the show with a friend if you dig it and hook us up with a five-star
[21.20 --> 26.10]  review to let random internet strangers know what's up that'd be pretty cool thank you to
[26.10 --> 34.14]  our partners at fly.io the home of changelog.com fly transforms containers into micro vms that run
[34.14 --> 39.90]  on their hardware in 30 plus regions on six continents so you can launch your app near your
[39.90 --> 46.64]  users learn more at fly.io okay hey it's party time y'all
[46.64 --> 64.10]  hello everybody another week first actually this is my first recording of 2024 and i could not think
[64.10 --> 69.32]  of a better first interview for me of this year than the topic we're going to do today and with
[69.32 --> 75.14]  the guests that we're going to do it with um so we're here today to talk about htmx you may have
[75.14 --> 80.94]  heard about this thing a lot lately uh it's having its moment it's having its 15 minutes and we're
[80.94 --> 88.04]  here to talk about htmx with none other than the creator of htmx carson gross hello carson welcome
[88.04 --> 93.78]  hey thank you for having me on the show i'm really excited to talk about htmx and then just the web
[93.78 --> 97.86]  more generally absolutely because we're gonna not just talk about htmx we're here to talk about
[97.86 --> 101.74]  rendering patterns and we're going to talk about the history of all the different ways we've been
[101.74 --> 109.20]  doing this dance since the beginning of javascript and html and here to join us uh for that discussion
[109.20 --> 119.68]  of the web dance is a person who i'm calling wp-30000 can you take a guess for like okay okay
[119.68 --> 126.92]  it's alex russell okay it's alex russell welcome alex but alex can you guess what wp stands for in this uh
[126.92 --> 134.72]  wp-30000 i hope it's web platform not wordpress but you know no shade to wordpress love me some
[134.72 --> 139.60]  wordpress but yeah it's definitely web platform because i feel like you are web mr web platform
[139.60 --> 145.14]  3000 like that is like that is who you are and i think i thought i was just here to represent uh the
[145.14 --> 150.88]  sedimentary history of web development you know from the ancient person's perspective
[150.88 --> 157.66]  i'm here with your dad jokes and you're you know yelling at the cloud yeah yes not forget the
[157.66 --> 164.16]  yelling you know but yeah so welcome alex we're so excited to have you back on the show so carson
[164.16 --> 168.40]  you know and and just kind of doing a little bit of prep for this show i noticed that not only have
[168.40 --> 173.80]  you been on js party before which by the way i i completely slept on that episode i guess like this
[173.80 --> 179.26]  was a few years ago so you've been on js party talking about this topic but you also were on go time
[179.26 --> 184.30]  about a year ago talking about htmx with those folks and that was that was a brilliant discussion
[184.30 --> 189.32]  i um highly recommend folks to check it out we'll link it in the notes we're excited to have you back
[189.32 --> 194.68]  again today and you know kind of fast forward a year i would say maybe not the average developer
[194.68 --> 201.12]  but i would say the the average tech twitter developer you know has heard of htmx you know and
[201.12 --> 204.90]  so i think some of the things that you were mentioning in that interview with the go folks was that like
[204.90 --> 212.96]  uh you know react is king and for better or worse and no one knows about htmx and you know that's
[212.96 --> 217.12]  the unfortunate part even though this is a good idea it hasn't really gained popularity or wide
[217.12 --> 221.60]  scale adoption and yada yada yada right and so i i'm like excited to see that we've moved the needle
[221.60 --> 225.70]  on that a little bit however like just because developers are talking about it doesn't mean it's
[225.70 --> 230.66]  actually being used at companies at scale as well right so hopefully we'll dig into all of that
[230.66 --> 235.86]  so before we get into kind of the the crux of like what is htmx can you just tell us a little
[235.86 --> 239.62]  bit about yourself carson you've got a really interesting background you've been working on
[239.62 --> 245.88]  the web a long time um so very eager to hear a bit about your backstory sure um so yeah i've been
[245.88 --> 253.22]  developing for the web for a very long time now started working with the web back in 98 99 was doing
[253.22 --> 259.44]  like java applets i actually it's kind of ironic that i'm now sort of an ambassador for hypermedia
[259.44 --> 266.14]  because early on i didn't like html i preferred the more thick client style applications that java
[266.14 --> 271.22]  applets and there was this thing called java web start that was around for a long time and i tried
[271.22 --> 277.22]  to use that rather than embrace the web but um eventually the web kind of got me and uh it just
[277.22 --> 284.22]  became compelling enough and uh so i started doing uh and i was my my primary web development like when i
[284.22 --> 290.52]  did structured well web development beyond just sort of cgi scripts which was the very early way you
[290.52 --> 297.68]  would do dynamic web pages was it was it was mainly in the rails environment so um did a couple of
[297.68 --> 304.02]  startups did some early work in java kind of built a worked for a company that built its own web platform
[304.02 --> 310.00]  that i worked on a little bit and then after that it kind of went over to rails mid to late 2000s
[310.00 --> 316.84]  from there you know i worked at a startup or me and a couple other guys i did a startup based on
[316.84 --> 323.86]  rails developed sort of a lot of more traditional uh web 1.0 style application application functionality
[323.86 --> 330.24]  and one of the things that came up when i was doing that was um this idea was actually working on a
[330.24 --> 335.52]  problem where i was trying to sort a table and i was trying to do this in probably around 2007
[335.52 --> 341.50]  and it was i was trying to do it in javascript on the client side because that was faster
[341.50 --> 347.68]  i had been told and it was like way slower i mean maybe it was a skill issue whatever but i just
[347.68 --> 353.82]  couldn't make it work and i just almost out of desperation tried this trick of like sorting it on
[353.82 --> 359.12]  the server side and then slamming it into the dom using the inner html of a table and it was really
[359.12 --> 366.76]  really fast and so uh i you know was kind of shocked but i i took that approach and i started
[366.76 --> 372.66]  using it and first i had like a little custom jquery based function i was using that but then
[372.66 --> 377.76]  it eventually grew into something called intercooler js i released that as an open source tool back in
[377.76 --> 384.34]  the early in like 2013 i think and like where does one release open source in 2013 like i can't remember
[384.34 --> 389.08]  where when github became a thing i probably around that time was this like did you put this up
[389.08 --> 395.76]  on github yeah it was up on github it was a github i think was 2010 ish it all blurs at this point but
[395.76 --> 400.58]  right but yeah so i you know open source it was my first real foray into open source software
[400.58 --> 406.14]  um and it went okay you know i it didn't take over the world obviously because at the same time sort of
[406.14 --> 413.10]  angular angular was the thing right when i was releasing intercooler js and then react came in and
[413.10 --> 418.52]  kind of shoved everything else out of the way at that point and so i feel like intercooler js was just
[418.52 --> 424.28]  sort of this interesting thing but it was based on jquery which is sort of old and weird and um
[424.28 --> 430.52]  it just wasn't right for the zeitgeist at the time and then i ended up moving i was in i was in
[430.52 --> 435.64]  california for a long time i'm a california native and i ended up moving to montana after the last
[435.64 --> 441.52]  startup i worked at kind of blew up and just wanted to change the scenery and so i moved out to montana
[441.52 --> 447.52]  and i i started teaching at montana state but during covid i took a look at intercooler which
[447.52 --> 452.66]  wasn't really going anywhere and was like man this it's probably time javascript has come a long way
[452.66 --> 460.32]  and so maybe we should uh try and rewrite this in vanilla javascript let's take intercooler js and see
[460.32 --> 467.52]  if we can rewrite it in vanilla javascript and uh so i did that and i ended up releasing it as htmx
[467.52 --> 474.08]  and uh that's kind of been the history of how how i got here anyways so it's sort of a clean room
[474.08 --> 479.48]  implementation of uh intercooler js although i don't know how clean room i'd call it because
[479.48 --> 485.88]  when i wrote it i was like i'm going to be internet explorer compatible so i sort of cut myself off from a
[485.88 --> 492.12]  lot of modern javascript when i did that and so um it's you know i think you could do an even cleaner
[492.12 --> 499.08]  room implementation of htmx if you came at it from like a pure uh javascript perspective that's such a
[499.08 --> 503.50]  great background thank you so much for for that summary um and i'm curious at one point you said
[503.50 --> 509.64]  web 1.0 and so can you kind of maybe just break down for folks like what you would put that like
[509.64 --> 515.86]  what's the um what's the delimiter between 1.0 and 2.0 sure yeah web 1.0 would be like forms and
[515.86 --> 525.62]  links and that's it not using forms with inputs and sort of uh the old ugly ka-chunk you know like
[525.62 --> 530.94]  you click although i have to say these days browsers are much better at what would be called web 1.0
[530.94 --> 536.90]  applications but but where you're you're interacting using full web pages like you click and go to a
[536.90 --> 543.06]  full new page or you submit a form and then it does the the i guess some of your listeners might not be
[543.06 --> 547.32]  familiar with this pattern but there used to be this thing where you would submit a form and if the
[547.32 --> 553.72]  form succeeded you would redirect to another page in order to avoid like resubmitting the form there
[553.72 --> 559.74]  were a lot of these sort of tricks around the early web and web 1.0 applications um but it's the older
[559.74 --> 565.56]  gronkier like i don't know if you ever used map quest i don't know if map quest is still a thing but
[565.56 --> 571.14]  sort of like where you had to click on something and wait for a whole new page to refresh that was that was
[571.14 --> 577.26]  sort of the web 1.0 style of application yeah and that's in contrast with the single page application
[577.26 --> 584.16]  right and like we're like sending up like full html pages you know yep and like using the web felt
[584.16 --> 590.62]  more taxing right and so that's why you know from a user experience perspective this like single page
[590.62 --> 595.86]  app you know it just felt like ah such a delight for users right because like here we're just using
[595.86 --> 600.74]  like ajax to like send bits of pieces back and forth and you're not having to do a full page reload
[600.74 --> 605.68]  and yeah with the 2.0 came like that rich interactivity because we could now all of a sudden
[605.68 --> 611.38]  we weren't doing these full round trips right but there's like a lot to kind of unpack there which
[611.38 --> 617.10]  we'll get into in just a second so let me let me toss the ball over to alex so alex i feel like
[617.10 --> 624.54]  mr uh wp3 3000 needs no introduction but please uh can you tell us a little bit about yourself as well alex
[624.54 --> 631.68]  i'm apparently a product manager on the edge team at microsoft but i you know i still work on making
[631.68 --> 638.04]  web pages faster and that work started when i was on the chrome team at google for a long time
[638.04 --> 642.86]  because we started to see that folks who are trying to build these kinds of rich experiences that we
[642.86 --> 647.76]  were just talking about were getting beached pretty frequently folks would start with high ambitions for
[647.76 --> 653.42]  the end user and then because of the tools and techniques and cultural assumptions that they had brought
[653.42 --> 660.32]  with them from what was in you know circa 2015 2016 the dominant ideology about how you built nice
[660.32 --> 666.64]  things on the web we ended up with teams who had built themselves into a corner with extremely tall
[666.64 --> 676.10]  piles of javascripts in a moment when the market was changing dramatically so since 2015 or 16 we've seen
[676.10 --> 682.48]  you know just the continued explosion of what happened in 2007 with the iphone moment but you know from
[682.48 --> 688.96]  20 i want to say 13 14 it was pretty clear that that diffusion was going to take hold worldwide not just in
[688.96 --> 696.36]  wealthy western markets and that that meant that we were going to see this extreme profusion of cheap devices
[696.36 --> 702.60]  where every year to the extent that moore's law continued to play out it meant that you could get more
[702.60 --> 710.06]  transistors per year per dollar but that didn't translate into faster phones for most people that translated into their
[710.06 --> 717.06]  first smartphone and that meant that every year the same capability got cheaper and that just grew the market and so it's only now
[717.06 --> 727.06]  2023 2024 that we're starting to see full saturation or the say replacement of what used to be the market for dumb phones
[727.06 --> 737.06]  being replaced by smartphones feature phone handsets were as late as 2019 half of the entire market in india and that has finally you know
[737.06 --> 742.46]  rounded the bend and so now we're in a place where folks are starting to get their maybe their second phones
[742.46 --> 748.40]  based on replacement rates and income worldwide that's not like what it is maybe where where we live but you know
[748.40 --> 753.76]  the global reality is continuing to change but that change for most of the last decade has meant that computers
[753.76 --> 761.06]  didn't get any faster they stopped getting faster and so our patterns and practices as a culture for people
[761.06 --> 788.58]  who were building on the web had been set they sort of cemented in 2013 on this idea of cpus get faster networks always get faster and that means we can afford more javascript every year and that has created one gigantic branch mispredict and that that great branch mispredict in the sky has caused us sort of at a cultural level to make choices that are not compatible with actually delivering good experiences for most people including people who are wealthy but just don't happen to be in the right time and place right now.
[788.58 --> 798.36]  And so it's been fascinating to see you know this turn to excess and then hopefully away but i'm excited about htmax and some of the patterns around it in that context.
[798.74 --> 818.50]  Yeah great points i i mean it's this interesting irony where like all of a sudden you know more people are accessing the web on mobile devices that have you know much tougher constraints you know especially in emerging markets like you're saying and we're also just kind of at the same time exponentiating the amount of javascript right because we're like oh we want these rich experiences and this
[818.50 --> 837.22]  and that but we're not really designing for like we're not really designing for like we're not really designing for those experiences in the way that these apps perform in the wild right and so so yeah very excited to kind of like unpack the how we got here question with both of you today.
[837.22 --> 865.60]  And so Carson let's talk a little bit about how we got here right so you've created this this popular library based on this kind of core primitive of the web that i think most people don't know about and when i say most people i really mean like probably most of our listeners most people writing javascript right this notion of kind of hypermedia and how you can leverage hypermedia to really just be talking in html right like jason has kind of been this language
[865.60 --> 893.70]  that we've you know been using as this kind of kind of like intermediary right between servers and clients and you know it's like oh this universal language that you know we can send over the wire and doesn't really matter what the consumer is it can be swift it can be flutter it can be javascript like in you know all these different like every single programming language knows how to deal with json and so it's like this universal connector but at the same time like it's you know i think htmx
[893.70 --> 923.32]  in this pattern of like sending htmx and this pattern of like sending htmx and this pattern of like sending htmx back and forth over the wire like it kind of highlights that like you know hey like maybe there isn't always a need for json right so yeah so let's can we talk a little bit about how we got here and then we can kind of dig into some of the merits of htmx for sure um so i think one of my core ideas is that the web the web is hypermedia the thing that made the web interesting at the start in any event was that hypermedia it was a hypermedia a distributed hypermedia system
[923.32 --> 953.30]  and there was a lot of thinking that went into that there were a lot of new ideas and it was something that was developed in reaction to the older sort of 1980s style thick clients this idea there's this thing that you know if you're familiar with roy fielding who i don't know how nerdy your listeners are but he wrote a really famous dissertation sort of about the web back you know in the i think the late 90s or and um the design of the web and the
[953.32 --> 983.30]  hypermedia works is it's designed such that there's a really strong recoupling between the client and the server and the client here is defined as the web browser and so one thing i try to stress to people is when they when they think about a web browser even just take javascript out of the whole equation here and think about the fact that you have a piece of software on your device that can talk to a pet shop it can talk to a car lot you can reserve a hotel with it you can get your news from it
[983.30 --> 1013.30]  and this one client that is sort of a universal client that's able to speak hypermedia is able to do all these things and if you told someone in the 1980s that they would be using the same piece of software to pay their taxes work with their bank pay their utility bills and you know do everything else order their you know the food or the dinner for the evening they would have looked at you cross-eyed because that's just crazy what how could you have a client like you know that it just wouldn't have computed for those people
[1013.30 --> 1041.16]  you know i i think that hypermedia it was really exciting i remember i was sort of like late in the game i was very young when the web sort of hit but looking back on it you can see the excitement around this sort of different way of building software that was based on this notion of hypermedia and just to give your listeners a definition of what hypermedia is is it's something that has hypermedia controls in it and hypermedia controls are things like links and forms
[1041.16 --> 1069.16]  that's like and if you're just talking about html so links and forms and what's special about links and forms or what's interesting about them is that they encode an interaction with a remote system within themselves so when you get a web page from you know some new website that you've gone to the links and forms that are in that web page have the urls and the interactions with that remote system baked into the html itself baked into themselves they're sort of self-contained
[1069.16 --> 1099.10]  they contain the remote they contain the remote logic necessary to do the things that that website wants to do and that that gets at something called the uniform interface from roy fielding's dissertation but it's really that idea of hypermedia controls that makes that's what defines a hypermedia in my you know my estimation and htmx what it does is it generalizes that idea it takes the two hypermedia controls most people are familiar with if they do web
[1099.10 --> 1107.10]  that is links and then generalizes it's like hypermedia control and then generalizes it so that any element can effectively act as a hypermedia control
[1107.10 --> 1121.10]  yeah and i think it's interesting it's like hyperlink which is like the kind of more like the tech the actual name for like anchor tags and all these other things i i've never made that connection until hearing you uh explain this so well carson
[1121.10 --> 1150.10]  you know but yeah but that is kind of like that is the web like right like this like series of links and things that like redirect you to other primitives you know and doesn't really matter what's coming back on the other end like you know it's going to be one of these three primitives right css html javascript and so alex can we can maybe dig into kind of this hypermedia protocol right because like it is it is a web primitive it is a web protocol and so why are we not talking about this more often
[1150.10 --> 1178.96]  and like how have browsers failed to maybe perhaps like expand on this protocol to enable like richer experiences yeah i think we don't talk about it as often in the web development community because we find that it's not something that we can personally influence right aside from building or rebuilding large piles of it in javascript in user land it's very challenging to imagine extending the vocabulary of the web in a kind of a
[1178.96 --> 1192.38]  a way that's simpatico with the built-ins because for many many many years it was fused shut right this this was the instinct for us to develop web components in the first place it's why you see there has been some intensity around form participation for custom elements that sort of thing
[1192.38 --> 1204.38]  and and i can report that it's finally here now that you know safari is mildly off the fence which is great we're in a position now where some of these expansions of the vocabulary are
[1204.38 --> 1216.90]  you know sort of easier to imagine doing inside of the system but for the longest time you just had to rebuild everything right that between the constraints of legacy and the need to have control for instance of things like styling
[1216.90 --> 1246.80]  the built-ins have not been the most simpatico way to try to get yourself a better version of a slightly upgraded version of that protocol whenever you want it and so one way to think about this is we kind of migrated culturally into javascript out of partial necessity and then i think beyond that to some degree we've stayed there out of storytelling and tribal identity the narratives are strong and it's hard to you know unseat them especially when you think you can afford
[1246.80 --> 1276.10]  what you're doing and then everything is going fine and if everything is going fine and if everything had been going fine i wouldn't be spending any effort trying to unseat those narratives because you know like i've spent most of my career trying to make life better for javascript programmers too but if if your listeners are interested or curious about this i'm fascinated by the progress that's being driven out of the open ui community group you know they have had a big impact on the thinking of kind of finishing some of the things that we intended when we started the web components journey around making pieces of
[1276.10 --> 1305.20]  markup markup uh existing form elements existing types more extensible or certainly from a styling and layout perspective and there's more to do there about the data types that we encode underneath right like that data type system is still a little bit fused shut in ways that i think are a little bit frustrating unless you go and build a form uh participating custom element today but the good news is that the the deltas that we need to apply on top of what the platform gives you in the 2024 moment are so much smaller than the deltas that we needed to apply previously
[1305.20 --> 1309.94]  and i think it really will be a mind shift change and i love what htmx is doing as a result
[1309.94 --> 1332.56]  okay so yeah let's like break that up a bit because you there's a lot there um so the open web ui group that you referenced is like this like kind of um standards working group that's trying to kind of create better higher level higher order components that are like more what you would think of when you know you think of like a react component or an angular component or something right like something like richer and easier to work with
[1332.56 --> 1362.46]  well you might sort of work back through the through the justification process and say why am i pulling in angular or react or something and and the answer might be as simple as well i can't style my select box right right i would like it to be reactive right because like the built-in elements they all have a kind of reactive belief about their own internal life cycles that just hasn't been opened up to us and so there's a fusing shot of the hood so you can't you can't go replace the bits just the bits that you want to get the change that you need you have to build a whole new vehicle and there's also the fact that the existing ones aren't very
[1362.46 --> 1368.88]  customizable uh nevermind uh serviceable right so they're pushing on both of those those doors and i think that's very helpful
[1368.88 --> 1392.08]  what's up friends i'm here with one of our good friends faras abukadijay faras is the founder and ceo of socket you can find them at socket.dev secure your supply chain ship
[1392.08 --> 1421.50]  with confidence but for ross i have a question for you what's the problem what security concerns do developers face when consuming open source dependencies what does socket do to solve these problems so the problem that socket solves is when a developer is choosing a package there's so much potential information they could look at right i mean at the end of the day they're trying to get a job done right there's a feature they want to implement they want to solve a problem so they go and find a package that looks like it might be a promising solution maybe they check to see that it has an open source license that it has good docs
[1421.50 --> 1451.48]  maybe they check the number of downloads or github stars but most developers don't really go beyond that and if you think about what it means to use a good package to find it to use a good open source dependency we care about a lot of other things too right we care about um who is the maintainer is this thing well maintained from a security perspective we care about does this thing have known vulnerabilities does it do weird things maybe it takes your environment variables and it sends them off to the network uh you know meaning it's gonna take your your api keys your tokens like that would be bad
[1451.48 --> 1481.46]  uh the unfortunate thing is that today most developers who are choosing packages and and going about their day they're not looking for that type of stuff it's not really reasonable to expect a developer to go and open up every single one of their dependencies and read every line of code not to mention that the average npm package has 79 additional dependencies that it brings in so you're talking about just you know thousands and thousands of lines of code and so we do that work for the developer so we go out we we fully analyze every piece of their dependencies you know every one of those
[1481.46 --> 1511.44]  lines of code and we look for strange things we look for those risks that they're not going to have time to look for so we'll find you know we detect all kinds of attacks and and kinds of malware and uh vulnerabilities in those dependencies and we bring them to the developer and help them when they're at that moment of choosing a package okay that's good so what's the install process what's the getting started socket super easy to get started with so uh we're you know our whole team is made up of developers and uh so it's super developer friendly we got tired of using security tools that send a ton of alerts and were hard to
[1511.44 --> 1539.44]  configure and and and and just kind of and and just kind of noisy and so we built socket to fix all those problems so we have all the typical integrations you'd expect a cli a github app an api all that good stuff but most of our users use socket through the github app and it's a really fast install a couple clicks you get it going and it monitors all your pull requests and you can get an accurate and kind of in-depth analysis of all your dependencies really high signal to noise you know it doesn't just cover vulnerabilities it's actually about the full
[1539.44 --> 1568.86]  picture of dependency risk and quality right so we help you make better decisions about dependencies that you're using directly in the pull request workflow directly directly where you're spending your time as a developer you know whether you're managing a small project or a large application with thousands of dependencies socket has you covered and it's pretty simple to use it's it's really not a complicated tool very cool the next step is to go to socket.dev install the github app or book a demo either works for us again socket.dev
[1568.86 --> 1572.26]  that's s-o-c-k-e-t dot dev
[1572.26 --> 1598.78]  anyone who's tried to style a form like a native form you know knows the pain of like yeah you can't get it to look the way you want it to look you know and there's a lot of really great work that's been happening over the years you know interop work with browsers and kind of improvements to like form elements that you know people have been working on which is great but yeah
[1598.78 --> 1628.76]  we're still far away from i think what web developers need for that like more turnkey experience that they're used to so that's really exciting work and so we talk about like okay um if the web had these components and we had like richer kind of elements that could help us tell this like hypermedia story why do we even need something like json like that's what i want to try to understand right so like if i can just have a conversation with my server in html i don't have to go through this like serialization process and blah blah blah what's the need for the
[1628.78 --> 1657.72]  need here for for something like json at all why are we using json it's a good question especially because html i mean http has the name right in it you know like why aren't we transferring html with this protocol so uh you know my one of my assertions here is that one of the problems we ran into was that html sort of froze as a hypermedia as far as the functionality it wasn't it wasn't taken forward as a hypermedia
[1657.72 --> 1684.48]  and so you only had links and forms now links and forms are very powerful you know all of web 1.0 was built with just links and forms which is pretty amazing to think about just two hypermedia controls let us do all of that um tremendous amount of wealth was generated a tremendous amount of information was distributed and so forth but the fact is that html really the form element which was part of html2 was the last hypermedia control and really the last
[1684.48 --> 1694.72]  part of html2 was the last part of html2 was the last part of html2 was the last time that html2 was moved forward as a hypermedia you know there's other stuff there's tons of other stuff that's happened to html2 but almost all of it
[1694.72 --> 1708.48]  or not almost all but the vast majority of it is in terms of either client side improvements or uh you know you get things like the the validation api they these things that didn't touch on the core idea of hypermedia controls
[1708.48 --> 1736.24]  and uh so i think what happened there was that that html2 was that that html2 stayed frozen and that necessitated a certain level of usability of user experience that was achievable with those you know hypermedia controls and so because of that almost out of necessity everyone switched to javascript or went javascript heavy and then when they went javascript heavy the obvious thing to use was json
[1736.24 --> 1743.12]  i mean it's again it's again it's in there in the name javascript object notation so i think that's why we ended up with json
[1743.12 --> 1750.44]  um is because yeah you know i don't think it was a mistake i just think it was there there was this unfortunate freeze
[1750.44 --> 1762.72]  in thinking about html and what's really unfortunate about it is that there was thinking earlier on about like very early on you know in the 70s and 80s about this concept of transclusion
[1762.72 --> 1792.16]  which is the idea of including one document and another document that i think is really sort of the crux of what html does or htmx i should say does because htmx by allowing you to have a hypermedia exchange where a piece of html comes back and then you place it inside an existing document it really gives you a big boost in usability over plain links and forms because you don't lose scroll state you get a huge amount of functionality just a much smoother feeling
[1792.16 --> 1821.62]  that comes with building an application just with that one feature of htmx and the the concept was around for a long time i actually wasn't familiar with it when i started making intercooler but i've come to go back and you know read up a lot more on the early hypermedia discussions and so it was there but just for you know reasons that sort of you know i i don't have the the back the background to answer html just kind of stopped and so that ended up pushing people who wanted more usability
[1821.62 --> 1831.04]  into javascript and then the natural communication medium was then you know we adopted this thick client sense like we're building
[1831.04 --> 1842.40]  applications like thick applications and so you're not going to use something like a hypermedia for that you're going to use a data format and json beat xml out you know so json was the way
[1842.40 --> 1851.48]  yeah yeah well i mean anything that's also a little bit closer to javascript right is yeah gonna just there's gonna be less friction to kind of adopt that as well like
[1851.48 --> 1862.76]  within code bases and and whatnot so i i can see that as well and so i think like this concept of transclusion like for me i when i think about the web and especially like early early web right like
[1862.76 --> 1875.62]  we're sharing documents and you know there's just a bunch of links that lead to like other documents and so like just from a mental model like that makes sense to me like html begets more html like that just that makes sense
[1875.62 --> 1884.34]  and so alex like you were kind of like smiling along when carson said the word transclusion and uh seems like you probably have some history with this you want to let us in on that
[1884.34 --> 1893.70]  uh yeah one of the uh contributors to one of the earliest javascript toolkits that i worked on something called dojo a guy named brad newberg who is i think spending most of his time on
[1893.70 --> 1900.66]  ml topics these days but i was lucky enough to work with for a while at google he got involved in a project
[1900.66 --> 1908.46]  you know with doug engelbart trying to rebuild a piece of the system that they had imagined for hypertext early on
[1908.46 --> 1916.60]  this is probably 2011 12 but you know working on ideas that had been husbanded by the doug engelbart and his group
[1916.60 --> 1922.70]  from the 60s and those transclusion ideas sort of made it into pieces of of this work and they are
[1922.70 --> 1929.78]  they are one of these things which is possible at the limit of our shared vocabulary and our shared performance
[1929.78 --> 1933.92]  right like to the extent that we can afford to represent the same concepts in a document that's
[1933.92 --> 1938.02]  hosted on someone else's computer then we get to do transclusions and to the extent that we can't we
[1938.02 --> 1942.24]  don't i think it's fascinating going back rolling back all the way to the json idea one way to think
[1942.24 --> 1948.10]  about this is why are we you know in the footer of every document that's been ssr'd quote unquote why do
[1948.10 --> 1954.48]  we have a copy of those same exact semantics living as a json structure which then gets rehydrated i think
[1954.48 --> 1959.50]  that's probably what we mean by json because this is this is actually the dumbest version of taking a
[1959.50 --> 1964.48]  local data model right like the one and done local snapshot of a data model is like the dumbest version
[1964.48 --> 1969.30]  of that data model and from the perspective of just going back and forth across several pages like if
[1969.30 --> 1974.70]  you just go look at the structure of i don't know just pick on anyone a new york times web page uh just
[1974.70 --> 1978.96]  view source on a new york times article and if it doesn't make you laugh you aren't looking hard enough
[1978.96 --> 1985.94]  because you get some html at the top and that html pulls in some javascript and then if you scroll
[1985.94 --> 1991.24]  halfway down you'll get to the bottom and it will have the same html as a json structure everything
[1991.24 --> 1996.34]  literally everything as a json structure and what does that tell us well it tells us that the the way
[1996.34 --> 2001.36]  that we want to make those things interactive has to bootstrap on to some representation that is not
[2001.36 --> 2005.50]  the html and so we don't actually share those html representations anymore we've tried to abstract
[2005.50 --> 2009.78]  ourselves up off of html and into some other thing and then we want to operate on that thing when we
[2009.78 --> 2015.92]  want to make changes and then splat it back out in some other way and this is kind of you know i think
[2015.92 --> 2021.72]  back to carson's point about having some necessity driving this without the ability to upgrade the
[2021.72 --> 2027.72]  semantics of html you know maybe because browsers get good at doing this again although we don't have
[2027.72 --> 2033.48]  a great track record there or because we have failed to bring along a system for doing it naturally
[2033.48 --> 2039.00]  ourselves we wind up in this logic of building a parallel world and then having to reconcile it with
[2039.00 --> 2043.78]  the displayed reality the thing that actually pumps our rendering system the thing that actually takes
[2043.78 --> 2048.38]  the diffs and turns them into dom diffs and turns them into css diffs against that and lay out trees
[2048.38 --> 2054.64]  and then render trees and then raster right that whole flow requires that we pump it with something
[2054.64 --> 2059.86]  and how far away we are from that that core semantic model that it's designed to be pumped by
[2059.86 --> 2065.76]  is this is this tension that we feel and that i think gets us into this question of like well why did
[2065.76 --> 2071.86]  we pile into the clown car of web 2.0 and it's interesting to me that all of the examples that
[2071.86 --> 2077.86]  we bring up about where that stuff was truly revolutionary are systems that had many clicks
[2077.86 --> 2085.16]  or taps or drags right they had many detailed drilled in interactions per session and it's in
[2085.16 --> 2091.08]  those places that that that local data model thing shines and it's in the other places which is i'm just
[2091.08 --> 2096.22]  going to like hand wave and say the vast majority of interactions on the web where you have shallow
[2096.22 --> 2101.76]  sessions whatever the designers intent where you aren't doing many clicks or taps against something
[2101.76 --> 2107.36]  that that would be better if it was a local data model that this stuff just feels like it's like it
[2107.36 --> 2112.06]  feels like cruft but we're not sure why even though we have some innate belief that it's good for us
[2112.06 --> 2117.20]  right because we're not looking at the diversity of session depth yeah i mean you know so i i'm surprised
[2117.20 --> 2121.28]  we've managed to get this far into the podcast without bringing up the word react like i don't
[2121.28 --> 2127.10]  think we have this i i'm the first to bring it up and i cannot wait to deconstruct react and like
[2127.10 --> 2132.18]  some of the paradigms with both of you because really like there's just so much that doesn't feel
[2132.18 --> 2137.58]  natural or that doesn't feel like it feels like we're using the web all wrong you know like we're not
[2137.58 --> 2141.90]  we're like working against it right and the fact that like the react core team at one point was
[2141.90 --> 2146.62]  creating a scheduling api which is you know still part of core i think you know it's just it's just
[2146.62 --> 2151.56]  mind-boggling to think that we are trying to manage scheduling threads in javascript instead
[2151.56 --> 2155.30]  of just actually just working with the browser and like working with these primitives in a way that
[2155.30 --> 2161.06]  makes not only sense but like it just greatly simplifies our code like and our and the complexity
[2161.06 --> 2165.98]  that we're managing as engineers you know let alone the like benefit that it gives to users as well
[2165.98 --> 2170.84]  right like that's we're all trying to to do so i don't know alex like this is kind of why i wanted
[2170.84 --> 2176.50]  to talk about like the how did we get here right because using angular and backbone you know
[2176.50 --> 2182.14]  over a decade ago i'm talking about like angular 1x single page apps were just like so sexy to
[2182.14 --> 2189.34]  everyone like it was just like oh you know and i don't know where we lost like sight of the complexity
[2189.34 --> 2194.72]  meter and where we lost sight of like does this make sense and you know and the other thing is like
[2194.72 --> 2200.02]  clearly there's some standards gaps that also pushed us to this right like let's take ownership here
[2200.02 --> 2205.32]  on the platform side like this is not just on web developers like they were just trying to get stuff
[2205.32 --> 2210.28]  done to you know to like ship things to their users and so like where did the platform fail us
[2210.28 --> 2214.88]  too right because we can't just take we can't we can't put all this blame on web developers right
[2214.88 --> 2220.46]  which are by the way world's smartest people i'll argue that with anyone but i think sometimes too
[2220.46 --> 2225.82]  smart for their own good you know so i don't know what are your thoughts carson well i think developers
[2225.82 --> 2232.48]  they tend to underestimate the complexity of state synchronization in general and one of the
[2232.48 --> 2240.86]  tremendous simplifying things about the web was the the web 1.0 model was that state was on the server
[2240.86 --> 2247.70]  and you rendered a representation of the state and that was it and uh i remember when i first saw that i
[2247.70 --> 2253.04]  had sort of a reaction against it too because i was i had built some thick clients and you know supported
[2253.04 --> 2257.98]  things like undo which if there's one great simplification of web applications that our
[2257.98 --> 2264.58]  users don't expect undo to work because holy smokes getting undo to work in a real big client is not
[2264.58 --> 2270.82]  trivial and uh so i think developers tend to underestimate that you know tremendous simplification
[2270.82 --> 2278.38]  of distributed systems that the hypermedia model gave them and uh they saw you know this clunky user
[2278.38 --> 2283.82]  interface and we're like man we can do better than that and they could and uh so the they they got
[2283.82 --> 2289.90]  attracted to that i think another dynamic i know dhh um you know say what you will about the guy he says
[2289.90 --> 2296.32]  interesting stuff um he he said that and he's kind of been on his own sort of riff on this where he's
[2296.32 --> 2301.44]  saying obviously he's been saying this for a while but he's not as he doesn't think single page
[2301.44 --> 2307.14]  application framework servers necessary as most be errors a lot of people do and um he's got his own
[2307.14 --> 2315.08]  a thing called hotwire which is in in some ways very similar to htmx and he said that a a lot of this was
[2315.08 --> 2322.60]  sold it was it was sales people were selling stuff there was a there was a slick aspect to it and i think
[2322.60 --> 2329.80]  there's something to that um i think that the broader dynamic though in technology is a fear of looking dumb
[2329.80 --> 2336.52]  and i think it's really hard for people when someone comes in with a really complicated system
[2336.52 --> 2342.20]  and is like look at this cool stuff that we can do for someone to be like man that is crazy
[2342.20 --> 2350.14]  maybe we don't need to do all that maybe could we do something dumb that's like an 80 20 solution to that
[2350.14 --> 2357.88]  and uh that i think is the broader problem in the tech world that that enabled us to go as far as we went
[2357.88 --> 2365.22]  again i'm sympathetic because we we work in an industry where your intellect is very highly valued
[2365.22 --> 2372.10]  and appearing dumb can be very bad for your career prospects and um the reality is there are people
[2372.10 --> 2380.72]  who have been left behind in technology like pearl developers you know in 1998 didn't see the java
[2380.72 --> 2387.82]  meteor coming at them and if they stuck with pearl and didn't you know get on the java bandwagon
[2387.82 --> 2393.60]  or go over to php or whatever they ended up really limiting their careers so it's just a dynamic that
[2393.60 --> 2398.98]  i think uh you have to acknowledge about the technology world yeah yeah no that's like so well
[2398.98 --> 2402.92]  said and by the way are you just trying to score points or something carson because like listeners
[2402.92 --> 2409.98]  on the show know how i'm like i beat that simplicity drum a lot and i beat the like 80 20 trade-off
[2409.98 --> 2415.40]  like a lot like in the sense that like everything you just said right like all these incentives that
[2415.40 --> 2421.56]  we have as engineers like to be smart work on hard problems be the hero crush it yada da da da
[2421.56 --> 2426.26]  be the bus factor like because i really do think some people strive to be the bus factor like and like
[2426.26 --> 2431.34]  you know bus factor being um to explain this it's like you know being an invaluable person to your
[2431.34 --> 2435.50]  company or team right you know where you're the only one who knows this esoteric code and you're the
[2435.50 --> 2439.26]  only one who can touch it and if somebody makes it like they have to call you at 3am to make an edit
[2439.26 --> 2444.94]  or approve a pr or whatever you know i i do feel like there's a little bit of fetishization of that
[2444.94 --> 2451.66]  like person that persona you know and we are not incentivized towards simplicity and i for me this is
[2451.66 --> 2455.92]  like a leadership problem like in terms of like our engineering leadership like our engineering
[2455.92 --> 2461.10]  leadership should be incentivizing simplicity because that's just better for everyone on all fronts you
[2461.10 --> 2465.64]  know but here we are in this complexity race and it's like a race to the bottom which is where we
[2465.64 --> 2471.94]  are now you know i i feel like things are so complicated in javascript like it's so hard for
[2471.94 --> 2476.86]  new people to come in and write modern web applications like when i say modern web applications
[2476.86 --> 2481.66]  it's quote-unquote modern web applications that are using popular tools and technologies right
[2481.66 --> 2487.88]  like a little hello world like you have to learn how to use a bundler you have to you have to learn how to
[2487.88 --> 2490.74]  you know potentially use typescript because the examples are all in typescript
[2490.74 --> 2495.52]  like whatever it is like there's all of these like barriers to entry because we've just like
[2495.52 --> 2499.54]  i don't i don't know what it is like maybe we're just trying to prove to everyone that like javascript
[2499.54 --> 2504.10]  is a serious programming language or like i like i don't know what it is but this like napoleon
[2504.10 --> 2508.98]  syndrome needs to go like because it's just it's hurting the web like literally hurting the web you
[2508.98 --> 2514.54]  know and alex i see you laughing so please chime in well i would just i would just cut the the question
[2514.54 --> 2520.70]  of why are we doing all of this complexity and how did we get here by trying to you know always
[2520.70 --> 2527.08]  challenge it by saying who are we tackling all this complexity for right like there is a there's
[2527.08 --> 2532.08]  a version which i think carson your point about people's hiring prospects gets to which is to say
[2532.08 --> 2538.92]  that there is a there is always and will always be some aspect of this which is about looking over
[2538.92 --> 2543.38]  your own back right for yourself and there's some aspect of this which i think is a little bit more
[2543.38 --> 2549.04]  inspirational and i hope more aspirational which is to say we're going to go make this get better for
[2549.04 --> 2555.70]  everyone and getting better for everyone is not about making it better for just me or people who
[2555.70 --> 2560.78]  are just like me or who are in the same situated you know physical geography or in the same situated
[2560.78 --> 2566.52]  socioeconomic bracket right those are questions about who do we want to have served looking back
[2566.52 --> 2572.16]  from our future selves and i think if i was just going to characterize today's technology landscape i would
[2572.16 --> 2577.06]  say that it is and this is not an indictment of any individual but it is an extremely selfish
[2577.06 --> 2582.44]  enterprise right it has bought into kind of a libertarian trickle-down developer experience
[2582.44 --> 2588.02]  idea and it's just as falsifiable today and the evidence that we're getting from imp and all the
[2588.02 --> 2595.74]  rest as it ever was in the data you know in the 80s from some some various uh tax experiments right
[2595.74 --> 2601.92]  like these things um these are ideas that don't work as well today um as they didn't work in the past
[2601.92 --> 2606.16]  and we don't have to keep trying them right we don't have to keep believing in trickle-down dx we
[2606.16 --> 2609.72]  can just say that the way that you make something better for the user is to focus on the user
[2609.72 --> 2614.86]  and that the problems that are worth solving are the problems that we can identify being as problems
[2614.86 --> 2620.32]  that users face rather than problems that we face and yes we can also say in a very cross-pressured way
[2620.32 --> 2624.44]  that it is important to solve problems for ourselves so that we can get problems for users right like
[2624.44 --> 2627.92]  this kind of developer experience bait and switch operates on the kernel of truth
[2627.92 --> 2634.04]  that there is something there that is so valuable that if we solve it we will have also solve problems
[2634.04 --> 2639.48]  for users along the way but i would just say that we have got so much evidence now of not marking
[2639.48 --> 2645.38]  those ideas to market along the way and that when we don't do that it turns out that it's just a bezel
[2645.38 --> 2652.52]  right it's just a failure that we don't account for yet and we can call them out as such in the future
[2652.52 --> 2656.90]  right we don't have to keep pretending that the next thing that the react team ships is going to solve
[2656.90 --> 2660.66]  anything because it actually isn't phrased in terms of solving something for the end user so if it's
[2660.66 --> 2666.36]  not solved and phrased in terms of solving something for the end user to a first approximation it doesn't
[2666.36 --> 2672.10]  matter and at a second order effect we definitely need some evidence to show that it's actually going
[2672.10 --> 2678.00]  to move the needle for us right and like if we don't have that evidence then a la hitchens razor we
[2678.00 --> 2681.90]  just get to throw it out we just get to ignore it the way we should have ignored it all along yeah i mean
[2681.90 --> 2687.44]  and and and standing ovation like i'm just gonna fake i'm gonna not it's not a fake clap it's a real
[2687.44 --> 2695.28]  clap we're just gonna okay seriously yes also how much of this do you think is a leadership problem
[2695.28 --> 2702.02]  because like i like as an engineering leader now myself i am like holy moly like i'm like i need to
[2702.02 --> 2706.48]  start blogging and i need to start helping these other engineering leaders like learn how to set some
[2706.48 --> 2712.46]  darn standards you know what i mean set some damn standards for your team 100 so can we talk about
[2712.46 --> 2717.34]  that yeah and i want to put responsibility where it belongs i don't mean to say that you know the
[2717.34 --> 2723.42]  enthusiasms of engineers are things that we should like pin industry-wide failure on like that's not
[2723.42 --> 2728.42]  true right there's a lot of technology that i love that hasn't taken off and probably never will
[2728.42 --> 2733.68]  and i just have to like be sad about that that's okay but you know i wish it was different in some ways
[2733.68 --> 2738.70]  but also managers have responsibilities in these environments and if anyone is supposed to be
[2738.70 --> 2744.04]  asking the question of who are we doing this for who does it benefit setting bunch marks that help
[2744.04 --> 2749.56]  you do it setting up environments where we can make that legible and visible you know like the overlap
[2749.56 --> 2754.84]  between teams that i consult with and i do a lot of consulting with teams here at microsoft to um to dig us
[2754.84 --> 2759.70]  out of the the ditches that we have reliably put ourselves in with regards to performance on the web
[2759.70 --> 2764.34]  the number of teams that that actually need the kind of help that we can provide from the browser
[2764.34 --> 2770.60]  side and the overlap in those teams between folks who have done bake-offs to find out what actually
[2770.60 --> 2776.68]  works for the user right like it's not it's a venn diagram in the style of two circles that don't touch
[2776.68 --> 2783.18]  you know folks who do bake-offs managers who are wise enough to put the user into the calculus up front
[2783.18 --> 2787.32]  and then make sure that they stay there or that they've got the kind of metrics that they need to do it
[2787.32 --> 2792.00]  they generally don't have these problems now that's not true you can get yourself into a place where
[2792.00 --> 2796.96]  you've got such a large organization that it's hard to you know contain any of these effects but
[2796.96 --> 2802.38]  the difficulty in containing those effects is a core argument for stack simplicity in the first place
[2802.38 --> 2806.72]  right because you know i've written a bit in the last couple years about what i've called the
[2806.72 --> 2812.78]  performance management maturity kind of uh cliff that you have to scale as a team and if you've got
[2812.78 --> 2818.44]  simpler technology your problems are generally simpler on the other side of trying to solve a
[2818.44 --> 2822.58]  problem a particular way now you might resent things about that stack but it didn't leave you
[2822.58 --> 2829.02]  with the most complex problems as a residual kind of side effect of doing the work whereas if you buy
[2829.02 --> 2834.16]  into complex stacks or stacks that leave you with complexity up front or try to hide complexity from
[2834.16 --> 2838.58]  you you own all of it on the other side anyway and now your problems are more complex and your
[2838.58 --> 2843.74]  solutions actually take much longer to execute so teams that get beached or stranded are teams that
[2843.74 --> 2848.32]  have bought into stacks that they don't actually manage and the outputs of those stacks manage them
[2848.32 --> 2853.12]  and that's the worst place to be and so this is a management maturity problem and that's where a lot
[2853.12 --> 2858.20]  of people are now right like they're just on this like bandwagon where i'm like looking at some of the
[2858.20 --> 2863.62]  new things that are coming out of react and i'm like whoa man like i wouldn't want to be stuck on that
[2863.62 --> 2869.32]  roadmap you know having to upgrade and and start using some of those patterns so like but anywho
[2869.32 --> 2873.92]  all right so we're going to come back to some of this stuff um because as we kind of do some compare
[2873.92 --> 2878.76]  and contrasts um because there's kind of a lot more to unpack here but you know since we've been
[2878.76 --> 2885.16]  focused on rendering patterns and the how how do we get here problem let's just shift into htmx carson
[2885.16 --> 2890.24]  so you know this is going to be like this quickest part of this discussion because i think it's such a
[2890.24 --> 2893.62]  simple framework it's going to be like super easy to explain it it's going to be like three minutes
[2893.62 --> 2898.42]  and then we're done we can all go home sure but but but why don't you just like lay the groundwork
[2898.42 --> 2906.24]  for us so kiss us out what is htmx okay so htmx the way to think about htmx is it's a few attributes
[2906.24 --> 2912.50]  that there's probably 10 to 12 core attributes and really there's only like five or six that can get
[2912.50 --> 2917.92]  you started and those attributes are html attributes so you put them on html elements
[2917.92 --> 2925.08]  and what they do is they uh generalize the idea of hypermedia controls which is a nerdy way of saying
[2925.08 --> 2932.08]  they make elements do things uh over the network and so um just as an example if you have a button
[2932.08 --> 2939.88]  and you want that button to issue a put to slash liked then you put an attribute on that button that's
[2939.88 --> 2947.90]  called hx put and you say hx put equals and then slash liked and that's similar in many ways
[2947.92 --> 2953.06]  to what you would put on you know an anchor tag you put have an href and that would tell the browser
[2953.06 --> 2958.56]  when someone clicks on this load that whole page in so uh when you put that hx put on a button
[2958.56 --> 2964.12]  what that's going to htmx which is javascript which looks for that attribute and then hooks up
[2964.12 --> 2969.60]  an event listener what htmx is going to do is it's going to issue a request to that endpoint and then
[2969.60 --> 2975.06]  that endpoint is going to return html and that's really the crux that's the really major difference
[2975.06 --> 2981.14]  between so you know thinking about things in a javascript centric world and the htmx approach
[2981.14 --> 2986.52]  is these are what i call hypermedia exchanges we're we're making a request of the server and we're
[2986.52 --> 2991.84]  getting back hypermedia and uh so then the question becomes okay i've issued this request i've gotten
[2991.84 --> 2998.34]  back uh hypermedia where do i put it um we've already talked about transclusion and so htmx has a few
[2998.34 --> 3005.70]  attributes um one's called hx swap and one's called hx target the hx target attribute uses a css selector
[3005.70 --> 3011.40]  which you know hopefully web developers are familiar with to pick an element in the dom to put this
[3011.40 --> 3020.06]  content into and then the hx swap attribute lets you tell htmx how to put that into the dom so maybe
[3020.06 --> 3024.06]  you want to put it inside the element maybe you want to replace the element so that's like the outer
[3024.06 --> 3029.02]  html maybe you want to put it after the element and so forth there's a few different options there
[3029.02 --> 3034.30]  and so that's really the crux is you know those attributes there's the one other attribute the one
[3034.30 --> 3041.00]  other generalization of htmx is that there's an attribute called hx trigger which lets you pick
[3041.00 --> 3049.54]  which event causes an http request to occur and so you know all these those attributes come together to
[3049.54 --> 3055.62]  generalize the idea of hypermedia controls and they let you implement more rich applications within
[3055.62 --> 3060.82]  the hypermedia model so a good example a good practical example and i would encourage your
[3060.82 --> 3067.28]  listeners to go to htmx.org slash examples because that probably doesn't sound like very much and it's
[3067.28 --> 3073.82]  not that's kind of the idea but despite that fact you can actually do quite a bit with htmx
[3073.82 --> 3080.08]  some user patterns that people ux patterns i should say that most people wouldn't expect those
[3080.08 --> 3088.26]  very simple or not trivial but still it's it's not a big step beyond plain html and the hypermedia
[3088.26 --> 3092.54]  controls we're already used to so to give you a simple example this is one of my favorite examples
[3092.54 --> 3099.00]  because it's two attributes but if you had a web page that had a chunk of it that was taking a while
[3099.00 --> 3105.82]  to render so you had some components say graph for example that took a little bit to render and you
[3105.82 --> 3112.24]  wanted to render it on a web page with htmx what you could do is you could take a div and you could
[3112.24 --> 3120.20]  put hx trigger equals load on that so trigger the request when this div loads and then you could point
[3120.20 --> 3126.22]  the url you could say hx get from slash graph and then what you could do is you could move that
[3126.22 --> 3134.26]  complicated graph computation out to another endpoint and remove it from the the first paint
[3134.26 --> 3139.68]  of that initial web page so maybe that graph isn't super important maybe the there's other actions you
[3139.68 --> 3146.22]  want the user to be able to do but these two attributes hx trigger equals load and then hx get
[3146.22 --> 3152.68]  equals slash graph allow you to take this piece of html and move it out to another endpoint and have the
[3152.68 --> 3158.98]  the initial page because it's able to use transclusion do a first paint without that content
[3158.98 --> 3165.38]  and so that's an example this lazy loading is a it's a great perf win it you know can get users to a
[3165.38 --> 3171.06]  user interface they can interact with a lot more quickly and uh if i first you know talk to you when
[3171.06 --> 3175.22]  when most people first start looking at htmx it wouldn't occur to them that they could do a pattern
[3175.22 --> 3180.24]  like that with this with this concept and so for whatever reason i just love that example because i've
[3180.24 --> 3186.58]  used it very effectively in a lot of web applications to make just to make a particular page faster
[3186.58 --> 3193.56]  yeah oh my god so this is that's super cool and wow and that kind of partial loading i feel like
[3193.56 --> 3197.64]  javascript developers have kind of recreated that with the islands architecture a little bit uh if
[3197.64 --> 3203.70]  you're familiar carson you know where we are able to kind of do this graceful lazy loading by kind of
[3203.70 --> 3209.98]  drawing boxes around different parts of our app but here like we can do that very simply and cleanly
[3209.98 --> 3217.46]  using htmx is like ability to use transclusion like duh you know yeah it's so duh it's like huh
[3217.46 --> 3222.90]  you know um okay so let's talk about this like ajax with attributes so that's so first of all i want
[3222.90 --> 3228.28]  to say congrats on like being probably one of the best marketers i think of of a library framework i
[3228.28 --> 3232.74]  don't even know who does your marketing if it's you or if you know people from the community but you
[3232.74 --> 3238.32]  y'all have some awesome marketing like your twitter pictures literally just me it's you okay well
[3238.32 --> 3244.32]  you're awesome and uh like if i ever have a library that i want to go viral like i know who i'm coming
[3244.32 --> 3250.28]  to i have no idea what i'm doing oh that's so funny okay so can we talk about ajax uh with attributes
[3250.28 --> 3255.40]  right so yeah you know folks uh you know many folks are probably familiar with like data attributes as a
[3255.40 --> 3261.76]  thing on html elements right but now you have all this other stuff and because html has this like
[3261.76 --> 3267.78]  very graceful extensibility right where you can have all these custom like attributes you're able to
[3267.78 --> 3273.56]  like leverage that similar to like somebody might say a prop right but these props are like a bit
[3273.56 --> 3278.64]  more specific so can we can we talk a little bit about this like how big is this api that you have
[3278.64 --> 3282.96]  for like these built-in attributes and can you give us some examples of some yeah it's not very big
[3282.96 --> 3288.34]  because there's there's really so when i think about hypermedia controls i think about four areas
[3288.34 --> 3294.32]  where they can be generalized so if you think about like a link or a form really those what makes them
[3294.32 --> 3300.34]  their essence from a hypermedia standpoint is that an event occurs in the case of the link it's a
[3300.34 --> 3307.40]  click or in the case of a form it's a submit and then a request is issued and then that response is
[3307.40 --> 3314.10]  used as a document to replace the whole page and so the generalizations there are okay let's let other
[3314.10 --> 3321.62]  elements issue those requests let's let any event trigger that request let's let any type of request
[3321.62 --> 3327.92]  be made one of the sort of tragedies of html is that in the standard hypermedia controls you can
[3327.92 --> 3335.18]  only issue gets and posts but http has you know put and patch and delete which these all have you know
[3335.18 --> 3341.22]  meanings and it's a shame that you can't access them directly from html and then finally that last one
[3341.22 --> 3346.42]  which is instead of replacing the whole document let's make it possible to do transclusion a flexible
[3346.42 --> 3354.54]  transclusion mechanism and those attributes boil down to hx get through delete so you know hx get
[3354.54 --> 3363.80]  post patch put and delete hx trigger which is the event and then hx target and swap which is sort of
[3363.80 --> 3370.14]  how to transclude the the content that came back into the dom and so the you know and for better or for
[3370.14 --> 3378.10]  worse i tend to use just hx get you can use data dash hx get if you want to be a better web citizen i
[3378.10 --> 3384.42]  don't know how alex feels about that but i've always just kind of used i sort of like how sloppy the web
[3384.42 --> 3390.14]  that's never mattered and it will never matter okay there perfect an adult has said it doesn't matter i
[3390.14 --> 3395.34]  love it so i would just say that the whether or not you use a data dash prefix in terms of attribute
[3395.34 --> 3401.26]  names has never practically mattered i can see the case for why it might um we've had cases in the javascript
[3401.26 --> 3405.54]  standard where people have sort of camped out on global names and that's been challenging to introduce
[3405.54 --> 3412.70]  things in but we have not as far as i know run into a case of that happening with data attributes or non data
[3412.70 --> 3418.66]  prefix attributes that yeah that that's awesome that's great context and so i'm just amazed at how you have just
[3418.66 --> 3425.98]  such a simple api like simple interface but it's so powerful right because it's really like it's the
[3425.98 --> 3431.84]  stuff that it's you know what are we doing on the web we're sending back a bunch of actions you know put
[3431.84 --> 3438.94]  delete get you know post and we're we're updating information on a screen based on the results of
[3438.94 --> 3445.12]  those actions you know and here now we have this framework or this library that allows you to do that
[3445.12 --> 3450.70]  gracefully and elegantly with html and for me like the beauty of html is you know it can handle
[3450.70 --> 3457.64]  structural complexity very well you know and then with that structural complexity if you do it well
[3457.64 --> 3464.74]  you also get nice semantics and nice ways of organizing your code and for me the best part about
[3464.74 --> 3471.62]  kind of moving more towards an html first world is that we now get to say hello to a bunch of other
[3471.62 --> 3478.36]  classes like we've lost a class of developers you know over the past 10 15 years we had css and html
[3478.36 --> 3484.34]  experts that we've kind of shoved to the corner in this javascript first world and i miss those folks
[3484.34 --> 3490.68]  those folks are amazing those folks know html better than we do as javascript developers those folks know
[3490.68 --> 3496.26]  css better than we do as javascript developers those folks know how to write accessible experiences
[3496.26 --> 3502.36]  right that are performant and clean and organized and i feel like we've kind of i don't know like
[3502.36 --> 3509.42]  we've just shoved them aside and i'm just i hope that this is like our new reality of focusing more
[3509.42 --> 3514.98]  on html right because i i'm excited to have to welcome back that class of developer right that's
[3515.00 --> 3520.68]  super into javascript but is into the other two big primitives of the web i see you nodding heavily
[3520.68 --> 3527.30]  alex oh yeah i think there's a file sale on talent right now and if you were going to try to
[3527.30 --> 3534.76]  determine whether or not someone who uh was sort of i would say you know given the median uh level of
[3534.76 --> 3539.16]  uh familiarity with css versus the median level of familiarity with javascript who's going to turn
[3539.16 --> 3545.10]  out the better experience for most users i would give it to the css expert or journeyman every time
[3545.10 --> 3549.86]  every single time uh just because most experiences are not composed of the kinds of
[3549.86 --> 3554.38]  extremely deep sessions that require us to pile into the javascript clown car we don't need that
[3554.38 --> 3559.58]  local data model to operate against with low latency with speculative application of data model
[3559.58 --> 3565.96]  diffs if we aren't going to keep the page around forever so in most cases uh you know you want to
[3565.96 --> 3571.54]  hire people to solve problems with html and css with as little javascript as possible not to pay them
[3571.54 --> 3573.16]  to make new problems with javascript
[3573.16 --> 3590.76]  this is a changelog news break curl creator slash maintainer daniel stenberg documents his frustration
[3590.76 --> 3598.64]  with recent ai tooling advancements quote i have held back on writing anything about ai or how we
[3598.64 --> 3605.40]  do not use ai for development in the curl factory now i can't hold back anymore let me show you the
[3605.40 --> 3613.06]  most significant effect of ai on curl as of today with examples end quote daniel is clearly of the
[3613.06 --> 3618.82]  opinion that we haven't gained much of value from generative ai tooling but he does seem more optimistic
[3618.82 --> 3625.50]  about the future than he is about the present quote i am convinced there will pop up tools using ai
[3625.50 --> 3630.86]  for this purpose that actually work better in the future at least part of the time so i cannot and
[3630.86 --> 3636.70]  will not say that ai for finding security problems is necessarily always a bad idea i do however suspect
[3636.70 --> 3643.70]  that if you just add an even so tiny intelligent human check to the mix the use and outcome of any
[3643.70 --> 3649.18]  such tools will become so much better i suspect that will be true for a long time into the future as
[3649.18 --> 3655.10]  well end quote my mind is open and willing to be changed but i'm with daniel here the human touch is
[3655.10 --> 3661.34]  absolutely necessary today and i suspect that will remain the case for much longer than some would
[3661.34 --> 3668.86]  have us to believe you just heard one of our five top stories from monday's changelog news subscribe to
[3668.86 --> 3674.82]  the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news
[3674.82 --> 3681.56]  to also receive our free companion email with even more developer news worth your attention once again
[3681.56 --> 3684.42]  that's changelog.com slash news
[3684.42 --> 3695.08]  let's actually get into that a little bit because i i want to talk about this session and types of web
[3695.08 --> 3700.38]  apps right because we've kind of danced around this a little bit and this kind of data model that's kind
[3700.38 --> 3705.80]  of conscious of like session time right and like architecture that's conscious of like how long are
[3705.80 --> 3710.98]  people spending on this site right for example netflix's login page i remember this this was a
[3710.98 --> 3717.60]  fun story like they they rewrote their login and sign up page like just in html and css and they
[3717.60 --> 3722.66]  removed react because it was just too slow right and so like they're why did they do that well they
[3722.66 --> 3728.88]  were optimizing for performance and hey we don't want to make people feel like it's taking too long to
[3728.88 --> 3735.44]  sign up or log in you know so you know that's smart let's optimize for that right so let's like have
[3735.44 --> 3740.96]  more of a static architecture so that we can you know meet our users as quickly as possible so we
[3740.96 --> 3747.98]  don't lose them to another tab or another like a tiktok video or whatever right um so so that's one
[3747.98 --> 3752.18]  but like can we talk a little bit about this like these different types of architectures and session
[3752.18 --> 3757.60]  depth and like i'm also curious to hear from you carson like when is htmx not a good idea for the
[3757.60 --> 3763.80]  thing that you're trying to do right sure so alex you want to go first here go for it okay well i you
[3763.80 --> 3769.68]  know the idea of session depth i i learned about it a couple days ago and i feel like i'm not in a
[3769.68 --> 3774.82]  great spot to talk about that particular way of looking at things but the way i look at things
[3774.82 --> 3780.08]  is sort of what alex was getting at earlier where if you have a bunch of events that need to drive
[3780.08 --> 3786.04]  interactivity then hypermedia is a bad idea um roy fielding said this he said you know it's designed
[3786.04 --> 3791.72]  for what he called coarse grain uh hypermedia interactions and so if you're trying to respond and
[3791.72 --> 3798.68]  who's roy fielding just uh roy fielding uh being the guy who wrote his dissertation sort of formed
[3798.68 --> 3804.28]  the basis the dissertation guy okay yeah he's the dissertation guy that he gave us the term rest and
[3804.28 --> 3809.02]  hadios if you've heard that term so hypermedia is the engine of application state i've always
[3809.02 --> 3815.30]  called it hetos is it hetios i don't know hetios it's sound it's a bad acronym he actually prefers
[3815.30 --> 3820.46]  the term the hypermedia constraint so that would probably be better for everyone involved yeah i speak
[3820.46 --> 3824.36]  too many languages to nobody should trust my pronunciation on anything because i'm multilingual
[3824.36 --> 3831.04]  and so whatever you know but i think alex's point that you know if you have a lot of interact like
[3831.04 --> 3835.82]  interactions that you know you can't put a hypermedia exchange in between those interactions
[3835.82 --> 3842.22]  um and you know you mentioned earlier the idea of island this island architecture to me one of the
[3842.22 --> 3847.98]  missing links in the discussions around a lot of these things is the notion of events like having an
[3847.98 --> 3852.56]  island of interactivity be it a web component or whatever something that does or gives a richer
[3852.56 --> 3857.52]  experience but then that integrates with a broader hypermedia system using what are hopefully not
[3857.52 --> 3863.72]  super frequent events you know someone gets a rich text editor that's a an amazing piece of software
[3863.72 --> 3869.26]  an amazing extension to the web they maybe they put markdown in it or whatever it is and then they
[3869.26 --> 3877.30]  click a save button and okay now an event occurs that triggers a bigger hypermedia exchange where that
[3877.30 --> 3881.94]  you know that markdown is sent to the server and rendered into html and plays somewhere else in
[3881.94 --> 3888.58]  the document or whatever it is and so just to give your listeners uh an idea of what htmx wouldn't be a
[3888.58 --> 3894.72]  good idea for it would not be a good idea for google maps i don't think it would be very difficult to make
[3894.72 --> 3901.12]  google maps work well with htmx it would be difficult to make google sheets work well with htmx because you
[3901.12 --> 3907.74]  have a lot of very crazy dependencies you can't afford to just sort of replace parts of the dom but
[3907.74 --> 3912.18]  you know one thing i often say is that on the other hand those two applications probably have settings
[3912.18 --> 3919.02]  pages they could use htmx where you know you're much closer to the standard form uh where you've got
[3919.02 --> 3924.74]  some check boxes and you know this and that and that that's sort of wheelhouse for for the web and so
[3924.74 --> 3930.20]  i don't think it's an either or necessarily um but there's definitely you know the more fine grain
[3930.20 --> 3936.18]  your event handling needs to be the less uh ideal the hypermedia infrastructure is going to be yeah
[3936.18 --> 3941.70]  i know that's that's a great summary and i think for me like it just you're just uh reinforcing this
[3941.70 --> 3947.52]  notion for me that it's okay to have different parts of your app be architected differently right
[3947.52 --> 3955.12]  like optimize for each experience you know using the best tool for the job it doesn't have to be one
[3955.12 --> 3959.56]  size fits all it doesn't have to be one size fits all that's right i have uh taken in some of
[3959.56 --> 3964.94]  these cases to working with teams to break down their apps into different experiences so i think
[3964.94 --> 3970.40]  the one that we may be most familiar with uh is you know maybe a blogging piece of software
[3970.40 --> 3977.28]  wordpress is probably a good example so wordpress has a viewing mode right and that is a query against
[3977.28 --> 3980.78]  the database or a bunch of different queries against the database nested with some templating and it
[3980.78 --> 3985.56]  spits some stuff out and the set of interactions that each of the viewers who go to each of the responses
[3985.56 --> 3991.22]  from those queries has about that content is extremely shallow those are shallow sessions
[3991.22 --> 3994.86]  that's and they're mostly scroll and scroll is handled by the browser so they don't count in
[3994.86 --> 3999.36]  your total like denominator number of interactions right so if you think about the number of interactions
[3999.36 --> 4004.08]  that we're counting here the interaction where you clicked on a link or typed in a url or tapped on
[4004.08 --> 4009.32]  something to get to it that's the first one so you get to one to start and every subsequent interaction
[4009.32 --> 4014.98]  in the session is is another added to the denominator but scrolls don't count so if we take that as our
[4014.98 --> 4021.54]  model viewing a piece of content and maybe scrolling down it it's one interaction right whereas the editor
[4021.54 --> 4026.78]  for a blog post inside of wordpress or something else that's going to be hundreds thousands of
[4026.78 --> 4032.34]  interactions right like you're typing right you're you're doing this stuff and one way of maybe testing
[4032.34 --> 4038.34]  this theory is could you benefit from having a local copy of the data model and having it sync up
[4038.34 --> 4045.32]  with a server so to the extent that that makes good sense from a sort of user latency perspective
[4045.32 --> 4052.54]  and from a user experience perspective of the total end-to-end experience you know should i have a
[4052.54 --> 4057.66]  crdt or should i have repli cache in my architecture you know is kind of this but you can disaggregate a
[4057.66 --> 4062.12]  lot of these applications and say it's got a viewing mode in which case the denominator is one or maybe less
[4062.12 --> 4066.60]  than five on average and then you've got an editing mode and that editing mode is a much more
[4066.60 --> 4071.64]  sophisticated application which may benefit from i don't know having a local offline copy of your
[4071.64 --> 4075.98]  stuff so you can modify and edit your stuff and sync it later and in the multiplayer version be able to
[4075.98 --> 4081.64]  do that stuff too so kind of disaggregating some of these applications is is a pro move but also just
[4081.64 --> 4086.94]  thinking about it from a you know top level perspective of who are my users who is my median session who's
[4086.94 --> 4091.96]  my p95 session how deep are their sessions and if their sessions are pretty shallow you know like every
[4091.96 --> 4097.52]  e-commerce site has basically it yearns for deep sessions but they're generally pretty shallow if
[4097.52 --> 4102.46]  they're generally pretty shallow then the denominator that you can divide the costs per interaction on
[4102.46 --> 4108.60]  is low and so if you think about this in terms of you know the ideal architecture serving you up
[4108.60 --> 4115.94]  only the delta in what you need when you need it you know per interaction style to get to the lowest
[4115.94 --> 4121.86]  total cost per interaction over the amortized session depth then you're getting into a place
[4121.86 --> 4124.98]  where you can start to make these kinds of trade-offs we don't do that today with these
[4124.98 --> 4130.10]  things we sort of kind of eyeball it and go i don't know smells like an app but you know most things
[4130.10 --> 4135.18]  aren't most things just aren't apps they aren't apps in that style of like having deep sessions which
[4135.18 --> 4140.44]  again kind of reinforces our intuition that things like stuff that need lots of scrolling and panning
[4140.44 --> 4145.70]  in any session to be moderately useful like maps probably need more infrastructure on the client
[4145.70 --> 4151.52]  versus things that you know we could offload more to the runtime for us to do right like the vs code
[4151.52 --> 4158.22]  in the browser google maps gmail right like these like things where you know you have like deep
[4158.22 --> 4163.80]  sessions and you have a ton of interactions and it's too expensive to kind of do those round trips and so
[4163.80 --> 4170.00]  for that case it's like have a local data model have like an architecture for kind of syncing like as
[4170.00 --> 4176.58]  often or as infrequent as makes sense for for that application and you know for things like
[4176.58 --> 4182.04]  your shopping websites and for things where yeah you want you you know everyone has this fantasy of
[4182.04 --> 4186.50]  people spending hours and hours on their application right like but like really you know yeah and you can
[4186.50 --> 4189.44]  investigate your logs you can find out whether or not people spend hours and hours in your application
[4189.44 --> 4194.12]  yeah you know yeah use data use data to make that decision to figure out how long are people actually
[4194.12 --> 4198.62]  on your site or on that page you know it won't surprise you to to find out that a lot of these
[4198.62 --> 4202.44]  things again they've got multiple humps they've got their you know their multimodal distributions
[4202.44 --> 4208.76]  you know working with the word team the word team in their data know that some large fraction of
[4208.76 --> 4214.54]  sessions are basically viewer sessions they they look like reading a blog post but it's also an editing
[4214.54 --> 4221.40]  interface which means that they can for people who are going to do long editing sessions afford to load up a
[4221.40 --> 4227.58]  bunch of stuff but most people aren't so they can't right so the overriding concern because you don't
[4227.58 --> 4232.06]  know who's who about most documents when you load them up but wouldn't this be like a and by the way
[4232.06 --> 4236.74]  when you say word team i'll just talk about like the microsoft word team and so for example with
[4236.74 --> 4242.62]  microsoft word wouldn't that be an opportunity to kind of break up that experience into two paths where
[4242.62 --> 4248.68]  you have like a read path and an edit path and by you default you assume that everyone's just doing a read
[4248.68 --> 4254.18]  and then when they decide to do an edit you you flip over or you use that time you use some background
[4254.18 --> 4260.04]  process to kind of like buy you some time while people are in read mode to get ready for edit mode
[4260.04 --> 4264.36]  or whatever it is like i'm just saying like wouldn't something like that make sense absolutely it does
[4264.36 --> 4270.86]  and those are you know there's a there's a range of tools you can employ to to make that mode switch
[4270.86 --> 4277.76]  more gradual but it's really i think informative to be thinking about what the costs are for most users
[4277.76 --> 4283.32]  foremost uh first and foremost rather than to fetishize your most engaged user because your
[4283.32 --> 4287.28]  most engaged user is going to be super valuable to you but if you're not taking care of most of the
[4287.28 --> 4292.34]  people who are using your service most of the time then you're failing by default right like so you
[4292.34 --> 4296.36]  coming back to this question of like what is the project manager engineering manager's job in this
[4296.36 --> 4301.80]  it's to ask who are we doing this for and then what does it mean to succeed and then to phrase that as a
[4301.80 --> 4307.48]  series of metrics that get pushed back to the engineering organization to say these are the
[4307.48 --> 4311.80]  things that we're going to drive up and they if you're not phrased in terms of user success again
[4311.80 --> 4316.40]  your organization is just going to be you know a stop clock yeah it's right twice a day but no not
[4316.40 --> 4320.88]  more frequently than that yeah no that right twice a day but not more frequently than that that's so
[4320.88 --> 4328.26]  funny yes yes and yes and i would say for me like there's an education gap like there's a it's a
[4328.26 --> 4333.80]  knowledge and skills gap here and on multiple fronts you know for example on the engineering
[4333.80 --> 4341.06]  side you know we don't have enough kind of discourse dialogue examples of you know multi-architecture
[4341.06 --> 4346.98]  applications right so like how do i support this these different paradigms under one code base you
[4346.98 --> 4352.02]  know in one monolith or whatever it is right so that's one the other thing is like on the engineering
[4352.02 --> 4358.08]  leadership and product management side there's you know just gaps and i think in the way that we
[4358.08 --> 4364.36]  work which like don't really make space for this kind of data-driven decisioning right and like
[4364.36 --> 4369.54]  here's some targets that we want to set and kind of this this kind of obsession with the user like
[4369.54 --> 4375.66]  you know uh and so i i mean honestly alex i feel like you and i should work together to like
[4375.66 --> 4380.20]  either write a bunch of blog posts or like do a bunch of talks you know on this topic really
[4380.20 --> 4384.70]  because i i do i think this is something that you know needs to be taught and it needs to be part of
[4384.70 --> 4388.86]  the wider discourse and it's it's just not can you give me an example of who's doing this well
[4388.86 --> 4394.24]  like outside of microsoft and google places that you've worked i mean doing doing which well oh
[4394.24 --> 4402.56]  like this kind of setting benchmarks and you know targets and using analytics to kind of help drive
[4402.56 --> 4409.42]  architecture decisions and so forth so most of the teams that i see who eventually get to a place where
[4409.42 --> 4413.50]  their systems are and i just want to i want to talk about this in terms of not in terms of like
[4413.50 --> 4417.46]  which technologies you pick but in terms of whether or not you are managing the technology
[4417.46 --> 4422.30]  versus whether the technology is managing you a lot of teams this never comes up in because they
[4422.30 --> 4426.82]  pick simple enough technologies that like they maybe have to fix some image loading or encoding
[4426.82 --> 4431.02]  issues somewhere along the lines or maybe something went sideways with the font these in terms of
[4431.02 --> 4435.24]  performance or your problems will be just as simple with accessibility because you you know to
[4435.24 --> 4441.66]  carson's point piled into html rather than rebuilding the entire universe on top of a very small
[4441.66 --> 4445.36]  footprint of you know the javascript runtime compared to the completeness of the rest of
[4445.36 --> 4450.36]  the platform by default for you and so so lots of teams end up with very small problems and they
[4450.36 --> 4455.86]  fix them quietly and we don't tend to talk about them the teams that i end up spending most of my
[4455.86 --> 4461.16]  time with are teams that have gotten themselves into the ditch and they get themselves there on good
[4461.16 --> 4465.76]  intentions no one's trying to do a bad job no one's trying to do the wrong thing for the user
[4465.76 --> 4471.72]  it's just that the user was not put front and center through the entire requirement process and
[4471.72 --> 4477.88]  pulling back from that requires management support right if you just do it as as an engineer if you
[4477.88 --> 4482.72]  just try to rock you know roll the boulder up the hill you will feel like suspicious at the end because
[4482.72 --> 4486.32]  without management support it's just going to be it's going to be rough so the places that have fixed
[4486.32 --> 4493.74]  this are you know like i've seen great results out of wix right they did they had a many year
[4493.74 --> 4502.04]  remediation challenge where they had bought into the usual react nonsense and that tanked their
[4502.04 --> 4508.38]  metrics and then they got management support to go fix it and then that turned into many years of
[4508.38 --> 4513.76]  not shipping features but instead fixing the stuff that they had meticulously broken with way too much
[4513.76 --> 4517.86]  javascript and then at the end of it you end up with the infrastructure that you would have needed to
[4517.86 --> 4523.50]  keep any piece of technology in line right teams that have climbed the management maturity mountain
[4523.50 --> 4530.08]  can manage anything teams that have not climbed it will be done in by anything but the simplest
[4530.08 --> 4536.32]  technology so from a management capacity perspective the real magic is to marry the simplicity of the
[4536.32 --> 4541.42]  solution to the capacity of the organization and its willingness to spend on keeping the complexity
[4541.42 --> 4546.62]  in check so that that means that the pro move for every manager who's looking at a new project
[4546.62 --> 4551.52]  is to do a bake-off because it's going to cost you a lot less to spend the time to actually try stuff
[4551.52 --> 4558.40]  to set up some pro user and pro marginal user metrics that you can judge against and then to
[4558.40 --> 4563.22]  pick the simplest thing from your set of potential available options right the most option value that
[4563.22 --> 4568.00]  you get is the option value of not having to be dead in the water for six months uh while you try to
[4568.00 --> 4572.10]  remediate something that's on fire like i've seen dozens of teams do you know people talk about like
[4572.10 --> 4576.16]  oh well if we do this and we had we can we could do all that do you remember the i don't know if you
[4576.16 --> 4580.94]  oversaw arrested development like the of course i think it was like the one netflix only season oh
[4580.94 --> 4585.38]  oh i haven't finished the netflix only season it's yeah they're buying a house and the conversation
[4585.38 --> 4592.54]  with a uh um a circa 2007 mortgage broker goes well you know if you have the extra bedroom then then
[4592.54 --> 4596.00]  then you've got it and they look to each other and go oh yeah then we've got it and that's kind
[4596.00 --> 4600.78]  of how i think carson to your point earlier about how we've got this aspirational complexity
[4600.78 --> 4608.02]  budget in our heads which is much larger than our our execution stomachs are you know those eyes
[4608.02 --> 4612.98]  um are outmatched by but what we can actually handle and that turns into a bad time predictably so
[4612.98 --> 4619.18]  um it's the role of managers to keep that in check yeah yeah here here and we're gonna link there's
[4619.18 --> 4624.20]  gonna be a lot of links in the show notes everyone like a lot like actually alex like while we're in
[4624.20 --> 4629.06]  this discussion this is how i'm like i want to know if alex is human or not because i'm like i know
[4629.06 --> 4634.78]  typical human being is not capable of like doing two things at once he's literally like talking and
[4634.78 --> 4640.64]  sending us links at the same time i'm just like what's going on do you like but we have a ton of
[4640.64 --> 4646.50]  links from alex but um the visual that you know i i really want you all to see is this like lovely
[4646.50 --> 4652.36]  diagram that he put together around interaction depth and you know the local data models and
[4652.36 --> 4658.58]  anyways it's it's pretty cool so check that out and i think for me the the cherry on the cake here is
[4658.58 --> 4663.68]  that like we are starting to wake up to this you know slowly but surely like i think people are
[4663.68 --> 4668.80]  starting to see that like the world that we're in is like this is not sustainable right and you can't
[4668.80 --> 4673.26]  have a ferrari for you can have an appetite for a ferrari but you can't be driving a ferrari when you
[4673.26 --> 4678.38]  have like a corolla budget you know what i mean and that is most teams most teams like don't have that
[4678.38 --> 4684.08]  ferrari budget and i think your your blog post alex uh market for lemons which we talked about last time
[4684.08 --> 4687.76]  we had you on the show which was you know web developments kind of last decade i think that's what the show
[4687.76 --> 4693.88]  was called you know we talked about how you know one of your frustrations has been that like hey
[4693.88 --> 4700.72]  for example tools like react aren't up front about how much infra and maintenance and time you need to
[4700.72 --> 4704.74]  spend on pruning and maintaining and blah blah blah blah blah it's not just just it doesn't doesn't
[4704.74 --> 4709.34]  doesn't just come for free right so your first your whole point was like hey like be honest about
[4709.34 --> 4713.32]  this stuff so people can make informed decisions but the problem is is like we have this like hype
[4713.32 --> 4718.24]  hype cycle hype train whatever and no one wants to go against that like it's it's actually like i
[4718.24 --> 4723.68]  can't i feel so sorry for like the engineering managers that have to even talk about tools that
[4723.68 --> 4729.30]  are not react with their directors or their engineers or their ics because it's like well like why would
[4729.30 --> 4734.20]  we use something that's not react react is going to be easy to hire for there's all these existing
[4734.20 --> 4739.74]  open source things blah blah blah blah you know and so like there's this like that that's the argument
[4739.74 --> 4743.74]  that i think a lot of people are like coming up against you know these are all nonsense arguments
[4743.74 --> 4748.50]  by the way i i don't mean that in the sense of like they are not marginally true that there's not
[4748.50 --> 4753.52]  a kernel of truth in them it is possible to find lots of resumes that say react on them but the idea
[4753.52 --> 4759.08]  that someone has made it to the end of the journey of putting all of the nut the just totally useless
[4759.08 --> 4764.82]  stuff that you have to learn to sort of make a react app go that that person can't also learn html
[4764.82 --> 4772.38]  javascript and css or get their hands around the platform or pick up htmx that idea is it's insulting
[4772.38 --> 4776.96]  to the people that you would hire it's true and it's so dumb that it really makes you think less
[4776.96 --> 4780.74]  of the person saying it because they obviously haven't thought hard about this claim either
[4780.74 --> 4787.40]  so it's a it's a dead idea and we can call it dead and we can call it you know unacceptable in
[4787.40 --> 4791.38]  conversation because it doesn't ever come with evidence other than there are a lot of resumes that say
[4791.38 --> 4798.18]  this but i can tell you right now we just put out a rec for some web components developers and a lot
[4798.18 --> 4802.36]  of these people say oh well we couldn't possibly hire for those skills and my intuition has been
[4802.36 --> 4806.30]  well that means you're not looking but now that you know we've just put out some some web components
[4806.30 --> 4812.32]  recs for uh for a team that i work with on design system side at microsoft i can tell you people are
[4812.32 --> 4817.14]  coming out of the woodworks for this stuff you can hire for whatever skill you're willing to pay for
[4817.14 --> 4821.42]  so if you're willing to pay for platform fundamentals and then little sprinkling of
[4821.42 --> 4826.38]  javascript with htmx or platform fundamentals and then a little sprinkling of web components or
[4826.38 --> 4831.26]  whatever your flavor of the month is for a little sprinkling of javascript i promise you those people
[4831.26 --> 4835.56]  are available i promise you they're awesome and they're not going to reach for things that are going
[4835.56 --> 4839.48]  to create a larger problem than they solve most of the time you'll actually get better culturally
[4839.48 --> 4844.46]  aligned values out of that population than you would by sort of the usual thing that people claim
[4844.46 --> 4849.52]  that they must have one thing you you mentioned earlier that class of their web developers but
[4849.52 --> 4856.68]  they were they were css and html specialists to an extent it overlapped with design and they got kind
[4856.68 --> 4863.04]  of pushed aside by the javascript world and i i do have to say because i don't live in react i don't
[4863.04 --> 4870.16]  have the same negative i don't have the same negative vibes that you and alex have um towards it um and
[4870.16 --> 4877.02]  obviously htmx is a different approach to things but one thing i do want to say to especially listeners
[4877.02 --> 4884.80]  of for you know js party is like i would like to see htmx de-escalate the language here like there's
[4884.80 --> 4890.24]  not a silver bullet that's coming from the react team htmx is not a silver bullet the web platform
[4890.24 --> 4895.86]  is good for some things and it's bad for other things and it would be amazing if we could get to a
[4895.86 --> 4901.50]  point where we could discuss those in a mature way without you know saying okay this will never work
[4901.50 --> 4908.16]  well it can be made to work i've seen bad design decisions be made to work and if people could you
[4908.16 --> 4914.06]  know especially listeners on a jsparty could look at this as like this is another tool i can use it to
[4914.06 --> 4921.20]  save complexity here and the irony of htmx for many javascript developers is that it actually makes
[4921.20 --> 4926.60]  the value per line of javascript that you write much higher because you're writing a lot less
[4926.60 --> 4932.68]  javascript you're saving javascript for those high value spots where it's important to get it right
[4932.68 --> 4939.84]  for the user and you leverage the platform for the other stuff like it's kind of a waste of the power
[4939.84 --> 4945.32]  of javascript to use it to get a form into a database like that's not what it was designed to do
[4945.32 --> 4950.60]  it was designed to help you know again roy fielding the guy who wrote that dissertation
[4950.60 --> 4956.74]  said that the scripting is there in order to provide functionality that the platform doesn't
[4956.74 --> 4965.18]  already have and so okay make drag and drop work for elements on an html page that's something that
[4965.18 --> 4970.76]  is not baked into the browser and that's a great use an amazing use of javascript that makes the user
[4970.76 --> 4977.56]  experience significantly better use it for something like that and again the value that you derive per
[4977.56 --> 4984.00]  line of javascript written goes up significantly so you know i just sometimes you know you see this
[4984.00 --> 4989.62]  and it's true there are people who really hate javascript and love htmx because they don't have to
[4989.62 --> 4996.94]  write any javascript but the truth is to use javascript as effectively as possible you have to understand
[4996.94 --> 5001.64]  the platform and javascript is part of that platform and so there's an opportunity you know one thing i've
[5001.64 --> 5009.28]  said is that i think that the most effective htmx users five years from now will be people who really
[5009.28 --> 5017.04]  understand the web platform in its entirety css html and javascript and who also have a strong sense of
[5017.04 --> 5023.84]  what they can accomplish on the back end i often say in sql but in sql sql is just a stand-in for you know
[5023.84 --> 5029.62]  whatever back-end technology but i think there's an opportunity and and and that would allow some of
[5029.62 --> 5035.60]  the the people who've been pushed aside because their knowledge is mainly css and html it htmx also
[5035.60 --> 5043.88]  boosts the relative value of html and css because it takes out this layer of junk you need to deal with
[5043.88 --> 5050.06]  to make those effective for modern user experiences so just it's just something i especially being on
[5050.06 --> 5055.48]  jas party i want to mention you know i don't want htmx to be viewed as anti the anti-javascript
[5055.48 --> 5061.40]  framework um it will to some extent because of the way it's set up but i really do think that
[5061.40 --> 5067.14]  again it drives up the value per line of javascript that good javascript developers who know the platform
[5067.14 --> 5072.78]  well can achieve yeah so well said uh carson and thanks for that excellent point i mean you know
[5072.78 --> 5077.72]  have to understand alex and i have been ranting we have like we have a we have a text thread we have
[5077.72 --> 5081.36]  threads on different platforms i should say but like we've been ranting about this stuff for years
[5081.36 --> 5085.84]  right so i think it's like you get two salty people together that have been ranting about this
[5085.84 --> 5090.36]  and it really it makes it sound like the opposite of what you said but yes to what you said and i think
[5090.36 --> 5095.18]  we're both definitely aligned with that and i would say that like i want to make sure that alex you know
[5095.18 --> 5100.02]  i think his point about react specifically it's not that it can't work it's just that it you need
[5100.02 --> 5104.70]  all these other things to make it work in the way that you think it should work or could work right
[5104.70 --> 5110.46]  yeah and if you if you're happy to pay that cost yeah then your team is paying full freight the place
[5110.46 --> 5114.28]  that i spend a lot of my time and therefore have a departure and experience with maybe some other
[5114.28 --> 5119.52]  folks is that i spend a lot of time with teams who are having a terrible time and because of the kind
[5119.52 --> 5124.76]  of toxic positivity bubble in the javascript community for the last decade around a lot of
[5124.76 --> 5129.08]  this complexity we haven't talked honestly about those costs and that means that teams get ambushed by
[5129.08 --> 5132.80]  those costs and that's bad for the teams and it's bad for the products and it's bad for the end users and
[5132.80 --> 5137.72]  i care about all those constituencies so it's not a this can't work you know like you said
[5137.72 --> 5142.96]  carson you can push a lot of bad ideas a long way with enough effort it's just that i want us to get
[5142.96 --> 5147.30]  to a place where we're having an engineering conversation around that delta in both cost
[5147.30 --> 5151.88]  and capability rather than sort of you know reiterating a bunch of old wives tales about
[5151.88 --> 5156.74]  how it could possibly go um when we have more data available to us yeah totes and i think one
[5156.74 --> 5161.30]  discussion that we are not going to have time to really dig into here but i would advise everyone to go
[5161.30 --> 5166.02]  listen to the the interview that carson did with the go time team we'll link that i think it's episode
[5166.02 --> 5171.14]  266 around kind of the full stack developer right like i i want to have that conversation with you
[5171.14 --> 5174.78]  carson like you know i don't care what you discuss with the go team but like you and i need to talk
[5174.78 --> 5180.04]  about that on air one day in the future because honestly like there's so many i have so many thoughts
[5180.04 --> 5185.88]  on this and i think there's a crisis identity around that you know what is front end what is back end and
[5185.88 --> 5190.94]  as these things are like interdependent merging talking to each other with the translation layer
[5190.94 --> 5196.44]  like json or you know now kind of being able to make that simpler with just html i mean there's just
[5196.44 --> 5201.28]  there's so much to discuss there we can't get into it today but i do want to touch upon web components
[5201.28 --> 5209.18]  and and how htmx plays with javascript specifically so i i haven't used htmx in like any production context
[5209.18 --> 5215.52]  right just outside of looking at the docs i'm very eager to try it and so you know for me i've cut my
[5215.52 --> 5221.10]  mental model of kind of looking at this is a it feels like it kind of like draws the outer boxes
[5221.10 --> 5226.88]  you know it kind of it helps you manage that transclusion but like what's inside the html
[5226.88 --> 5233.24]  that's being transcluded like this like the swap right this element or whatever or tree that's getting
[5233.24 --> 5238.92]  swapped in like that can be anything right the custom elements web components right so i just want to
[5238.92 --> 5244.14]  talk about this like lit elements like are my favorite thing in the world like i love the lit api
[5244.14 --> 5249.86]  just makes it so easy to work with up components and lit's having its um you know it's having a
[5249.86 --> 5255.06]  huge surge in kind of adoption eager to have uh justin fagnani on the back on the show again for those
[5255.06 --> 5259.12]  of you who missed it highly recommend checking out that episode we had him on on the show a few
[5259.12 --> 5265.24]  months ago and so how do web components and htmx like how how well do they play together how well
[5265.24 --> 5270.16]  do they work together um they play pretty well together in htmx too uh we have an engineer
[5270.16 --> 5276.18]  who's been working on making attributes within web components htmx attributes within web components
[5276.18 --> 5281.28]  work there's always that you know the getting across the fence to the other side um is always
[5281.28 --> 5286.62]  a trick my theory on web components they obviously they work you know it's just html that's one of the
[5286.62 --> 5292.84]  nice things about htmx is it's leveraging the platform and so as long as you know we don't do
[5292.84 --> 5298.68]  anything too screwy they they just kind of work but i i think the integration story between web
[5298.68 --> 5306.76]  components and htmx is again events that to me is what the dom is it's this hierarchy uh this tree
[5306.76 --> 5312.06]  of elements and the way they should communicate there's just looking back historically the way
[5312.06 --> 5318.54]  that you've done loosely coupled user interfaces that sort of interact with one another without a
[5318.54 --> 5325.92]  hard interface between them because there's not there's no type safe interface on the dom is via
[5325.92 --> 5331.92]  events now the event you know events are tricky and i i'm old so i programmed in something called
[5331.92 --> 5337.20]  hyper talk which was this thing called hyper card back in the day and so i just always had a soft spot
[5337.20 --> 5342.24]  in my heart for events event oriented programming does take a little bit to get used to particularly
[5342.24 --> 5346.54]  if you're not just saying i just want to handle clicks on this button if you start saying things
[5346.54 --> 5353.44]  like i want to listen for uh you know an update event from this point in the dom and uh so there's a
[5353.44 --> 5359.42]  different mindset to adopt but my again my theory here is that any sort of client side enhancement
[5359.42 --> 5363.80]  you know even if you were to say we've got this little bit we're going to do it in react because
[5363.80 --> 5368.42]  react has this feature that's super important to us for this part but we want to integrate it with
[5368.42 --> 5373.38]  htmx i would say use an event have that thing when it's done doing its mutation when it's built up
[5373.38 --> 5379.52]  the state locally that is ready to be synchronized to the server at that point have it emit an event
[5379.52 --> 5385.16]  to htmx and uh and then htmx can take over and do the state synchronization which is what it's good
[5385.16 --> 5389.74]  at um so i think the same thing with web components that's that's what i would look to in the web
[5389.74 --> 5393.70]  component world and that's what you know i say the same thing with javascript libraries people
[5393.70 --> 5400.62]  ask me how can i make my javascript library work better with htmx and i say emit a bunch of events
[5400.62 --> 5408.98]  because the more events you can emit in your life cycle um the the better and an htmx user can
[5408.98 --> 5413.84]  respond to those events in the ways that it's appropriate for their use cases that makes so much
[5413.84 --> 5420.86]  sense this matches with my sort of belief about why we built web components right was to return the
[5420.86 --> 5427.14]  idea of the component model to being something about creating things that platonically feel just
[5427.14 --> 5432.38]  like html elements and that means that they coordinate with their tree peers and siblings
[5432.38 --> 5440.40]  and parents through events and that they respond to attributes and javascript property changes like
[5440.40 --> 5447.68]  everything else and so htmx as a thing that just lives in and with and around html should if your
[5447.68 --> 5453.36]  web components are built well should just work right like this is the magic of things being composable
[5453.36 --> 5457.40]  on the dom interface and the idea of the platform being a platform for you rather than being uh
[5457.40 --> 5463.42]  an inconvenience that you target by side effect later yeah yeah here here and and to just i guess
[5463.42 --> 5467.44]  another point to add here was um and you put this in the chat alex so this is actually your point
[5467.44 --> 5473.32]  which is not a react event but a real event right because react uses synthetic events so the events
[5473.32 --> 5479.50]  so if you're if you're trying to pub or like wait for events and all of that just use use the real dom
[5479.50 --> 5485.40]  events and i have to say the unload events on elements like that's probably been the like api
[5485.40 --> 5491.02]  that i've used most consistently throughout my entire career like i mean the dom is really rich
[5491.02 --> 5495.02]  in events it'll tell you when things are done loading it'll tell you all kinds of things you
[5495.02 --> 5501.24]  just gotta listen you know so thank you for that amazing psa uh carson and so just gonna end this
[5501.24 --> 5506.84]  conversation on just talking a little bit about like the delta that you see i want to i want to hear
[5506.84 --> 5511.68]  from you carson on like what is the platform missing you know what what's missing in browsers
[5511.68 --> 5516.72]  to kind of really elevate us to like the next that'll take us through the next uh era of the web
[5516.72 --> 5521.66]  right so what are we missing yeah i will i mean you know i hope at this point people are starting to
[5521.66 --> 5527.04]  take an interest in htmx as far as just the concepts you know one thing i say is that i think the ideas
[5527.04 --> 5532.92]  of htmx are probably more important than the implementation um which is you know written by a flawed person
[5532.92 --> 5538.24]  but that idea of like generalizing hypermedia controls i'd like to see discussions around that
[5538.24 --> 5545.28]  at the platform level and the the tricky part there and this is another long conversation is
[5545.28 --> 5551.00]  getting accessibility right for a lot of the stuff is hard and improving that so that things are more
[5551.00 --> 5556.60]  accessible by default um i think it's unrealistic one thing i say is we should try and make accessibility
[5556.60 --> 5561.74]  accessible and it's one of the glories of the web is that anyone can create a web page
[5561.74 --> 5568.46]  and i think it's a shame to you know to gatekeep that like it's i loved the early web when you
[5568.46 --> 5574.56]  could right click and view the source of a page and see what was going on and uh so taking just this
[5574.56 --> 5579.36]  idea of generalizing hypermedia controls another big thing and this is boy this is pretty nerdy
[5579.36 --> 5587.34]  but the ability to reparent an element in the dom without losing the state associated with that element
[5587.34 --> 5594.48]  so right now um if you take a video element and move it in the dom the video stops playing
[5594.48 --> 5602.32]  and kind of restarts and uh similarly if something has focus and you change it you move it from one spot
[5602.32 --> 5609.32]  to another uh you it loses focus and so forth and if you were able to move things around and not have them
[5609.32 --> 5617.12]  lose that sort of uh in flight state you could do a lot of very interesting transclusion work where
[5617.12 --> 5624.38]  elements could be preserved between navigations and you know even at the top level you know like
[5624.38 --> 5630.04]  imagine a world where you could just have an anchor tag and you could mark a video as like keep this
[5630.04 --> 5635.62]  thing around and all someone has to write is an anchor tag and they can click and go to another maybe a
[5635.62 --> 5641.54]  detail page for the video the video keeps playing but they've just authored html they haven't had to
[5641.54 --> 5646.40]  do anything beyond that that ability to do i'd call it stable reparenting where where elements don't
[5646.40 --> 5651.04]  lose state that would be a huge feature in browsers i think a lot of javascript platform like people
[5651.04 --> 5655.36]  are building on top of javascript would love that feature i don't hear a lot about it but i think if
[5655.36 --> 5660.16]  you showed it to them they would it would be pretty mind-blowing yeah i mean that's that sounds amazing
[5660.16 --> 5665.24]  i'm like take me there i want that future that sounds really excellent um and i just
[5665.24 --> 5671.94]  really you know carson like you're just so humble and like i'm just so thankful for your
[5671.94 --> 5678.48]  contributions to like these important not only discussions but i would say like paradigm shifts
[5678.48 --> 5685.34]  you know that like i think we're slowly but surely hopefully going to have and it's just so great to
[5685.34 --> 5691.30]  hear that you're not antagonistic to javascript either right that you understand that it takes three
[5691.30 --> 5697.66]  to tango on the web right javascript css and html you need all three to tango well you know you can
[5697.66 --> 5702.84]  do a pretty bad tango with with just like one or two of those but you know to get the right mix you
[5702.84 --> 5708.00]  know you need three you know so i i think for me as as kind of someone that's really passionate about
[5708.00 --> 5714.38]  technical education um you know it's definitely a drum that like i hope to you know be able to kind
[5714.38 --> 5720.28]  of continue beating throughout my tenure here on this podcast and hope to have more discussions
[5720.28 --> 5724.72]  with folks like you hope to have you back on the show carson i'm so there's there's so many takes
[5724.72 --> 5730.78]  that i want to hear from you including like your take on uh inp which we kind of briefly like so i
[5730.78 --> 5734.32]  think alex mentioned it like an hour ago or something like that but we didn't even get to click
[5734.32 --> 5739.72]  into that as interaction to next paint um which is a new core web vital that's landed that we're all
[5739.72 --> 5745.38]  really excited about we'll probably do a show on that at some point soon so just again many thank
[5745.38 --> 5750.52]  you carson and many thanks to you alex alex any kind of closing thoughts from you before we kind
[5750.52 --> 5756.20]  of wrap i would just say that um we touched a little bit on how the browser kind of stopped
[5756.20 --> 5761.36]  delivering you know we kind of got ourselves into a rut after the initial burst of energy around
[5761.36 --> 5766.88]  uh the initial to borrow your phraseology carson uh the hypermedia controls and those built-in
[5766.88 --> 5770.92]  controls are extremely powerful and they have not been configurable enough and that has meant that
[5770.92 --> 5775.72]  people have lost faith in them and sort of moved to other places to get what they need done so i
[5775.72 --> 5781.16]  would say if you care about those things improving the open ui community group is is still looking at
[5781.16 --> 5785.74]  those and they can use your input and we are starting to be able to deliver some of those things into the
[5785.74 --> 5790.58]  platform a little bit more credibly now because browser competition is actually potentially going to
[5790.58 --> 5795.22]  become a real thing again and i know this is a much much much much much much longer conversation and i'm
[5795.22 --> 5799.92]  looking forward to hearing your yeah i forgot that we like we wanted to talk about this and we
[5799.92 --> 5804.52]  completely missed it alex like yeah browser choice well i'm looking forward to hearing your conversation
[5804.52 --> 5810.26]  with the open web advocacy folks because they've been doing the most important work i think on the
[5810.26 --> 5815.50]  web uh in the last couple of years i i mean this in an absolute sense like of any group they are the
[5815.50 --> 5820.96]  probably the most leveraged set of people who have who have created a larger better potential future
[5820.96 --> 5826.74]  for us because in a lot of ways what we can ask of the platform is gated by the total channel capacity
[5826.74 --> 5832.46]  of the teams that implement browsers and so if those teams are underfunded or they're stalled then we
[5832.46 --> 5837.84]  can't ask for very much and therefore we don't get very much and so they have been doing the most to
[5837.84 --> 5842.92]  unblock that pipe and keep it open so again i can't wait to hear what they've got to say on your on
[5842.92 --> 5847.74]  your episode uh with them but i would just say uh if folks aren't aware of what they're doing they are
[5847.74 --> 5853.38]  looking for volunteers that open-web-advocacy.org they've got a discord they've got a uh they've
[5853.38 --> 5858.82]  got a whole kind of you know rigmarole going and um and you can be part of the solution too yeah yeah
[5858.82 --> 5864.58]  and uh just thanks for ruining the surprise alex you know folks don't know that i was gonna have
[5864.58 --> 5869.00]  them on the show i guess they do know now but yes we're gonna do a show with the folks that started
[5869.00 --> 5874.18]  the open web advocacy group it's a group that's really been kind of fighting really hard um and
[5874.18 --> 5879.96]  literally like consulting with like nation states like they're like meeting with korea and france
[5879.96 --> 5886.68]  and the eu and like it's crazy like but they are like talking to all these large important entities
[5886.68 --> 5891.86]  about the importance of the web and the importance of like the free and open web with choice browser
[5891.86 --> 5897.88]  choice um and that's just like one thing i think like i know there's other aspects that they're also
[5897.88 --> 5902.48]  advocating on and that they're just like regular developers like us and when i say regular of course
[5902.48 --> 5908.02]  like it's like regular in quotes but i mean like these aren't like policy phds or like these are
[5908.02 --> 5913.80]  like engineers that we know including our very own for us for our own for us as part of that group so
[5913.80 --> 5918.26]  excited to have them come on the show and talk about that important topic um you know obviously safari's
[5918.26 --> 5925.24]  slowly gotten off the bench uh with kind of their support for pwas but but it's far from like where it
[5925.24 --> 5929.86]  needs to be and there's just bugs in the implementation and blah blah blah blah blah it's really interesting to
[5929.86 --> 5935.14]  see dhh kind of yell about this on the internet as well this past week uh as he's like having trouble
[5935.14 --> 5940.76]  getting his uh app on the apple's app store approved the hey calendar like it keeps getting rejected
[5940.76 --> 5945.06]  because according to him it's because like he thinks it's because they're not willing to do kind
[5945.06 --> 5950.14]  of in-app purchases and give apple that 30 but you know but who knows either way though like no one
[5950.14 --> 5955.32]  should no company should stop you from putting out a product onto the internet and this is why like we need
[5955.32 --> 5961.42]  to fight for the open web and so we'll put links in to the show notes for you all to see funny tweets
[5961.42 --> 5967.54]  from dhh including like a really funny did you all see the one where he alex i know you're not on
[5967.54 --> 5972.10]  twitter but i sent you this link oh and by the way everyone you remember i last week i talked about
[5972.10 --> 5977.04]  a friend who judged me one of one of the friends who judges me every time i send him a twitter link
[5977.04 --> 5983.78]  it's alex alex russell judges me pretty hard yeah he's put his hand up yeah so i send links
[5983.78 --> 5988.06]  twitter don't be on twitter y'all there's there's other places you don't have to go to the nazi bar
[5988.06 --> 5995.68]  it's fine oh good lord anyways nazi bar oh my gosh anyways so there was this tweet where he what
[5995.68 --> 6001.62]  did the dhh do this one was hilarious yeah he basically sent his mob of reply guys to apple
[6001.62 --> 6006.46]  because apple basically said like what do you want the app store to do or something i don't even know
[6006.46 --> 6012.10]  what are your favorite apps i think of the year or productivity apps and then like all his reply guys
[6012.10 --> 6016.64]  started like hounding apple's marketing team around like here's an app that i wish was on the
[6016.64 --> 6022.82]  store so anyways pretty hilarious sorry for the tangent but so to wrap up our show this was epic
[6022.82 --> 6028.74]  long discussion it's gonna require i think a couple of listens for me as i like unpack all the
[6028.74 --> 6034.28]  information that was shared carson any kind of closing thoughts from you before we wrap yeah um you
[6034.28 --> 6041.42]  know again i i just want to stress that de-escalation like hypermedia is a tool you know and uh i i think
[6041.42 --> 6046.74]  it's an interesting tool even if your listeners don't end up using it we did release a book it's
[6046.74 --> 6054.22]  available for free online at a hypermedia.systems and that particularly for developers who just have
[6054.22 --> 6059.08]  never really worked with like a web 1.0 style application that'll kind of walk them through
[6059.08 --> 6066.02]  the history of hypermedia and then it builds a simple web 1.0 style web application and then um
[6066.02 --> 6071.34]  and then enhances that with htmx um so that might be a good sort of more long form introduction
[6071.34 --> 6079.02]  uh to htmx there's a lot of stuff on the essays page htmx.org slash essays um some of those are
[6079.02 --> 6083.28]  pretty serious some of them are less serious and definitely the least serious of the bunch is my
[6083.28 --> 6090.02]  i'm sorry alex but my twitter account which is uh twitter.com slash htmx underscore org every time i think
[6090.02 --> 6096.82]  about going to a mastodon server there's always a there's always a no posting stipulation and i'm
[6096.82 --> 6104.64]  like oh man i don't know how to do it without so funny all right well and are you available for hire
[6104.64 --> 6109.64]  for other like library authors or maintainers that need some marketing help carson i'm just curious
[6109.64 --> 6115.78]  you don't you don't know this is i'm literally the dog flying the airplane that has no idea what
[6115.78 --> 6122.48]  it's doing i'm just like i don't know man at some point this all ends in tears oh my gosh you're too
[6122.48 --> 6127.74]  humble well again many many many thanks to both of you um so carson where can folks find you on the
[6127.74 --> 6131.92]  internet same question for you alex how if they want to connect what's the best way for them to
[6131.92 --> 6137.96]  connect with y'all big sky.software is my software company it's just me i don't know go to montana
[6137.96 --> 6142.44]  state i teach you computers teach you some computer science if you go to montana state
[6142.44 --> 6147.88]  are you guys available like online uh is there like an online course that people could like join
[6147.88 --> 6152.44]  where you are their professor no we don't have anything online so they have to literally fly
[6152.44 --> 6157.48]  to montana yeah yeah unfortunately at this point you have to go to montana state i don't know you know
[6157.48 --> 6163.24]  okay that's not bad montana's a beautiful state i would love to go yeah montana is very it's very cold
[6163.24 --> 6171.48]  but it is very pretty for sure how about you alex uh you can find many links at uh infrequently.org
[6171.48 --> 6179.24]  and a lot of very long blog posts that cover some of the background about my agitation um and uh you
[6179.24 --> 6184.20]  know links to other ways to get a hold of me yeah one of the best blogs on the internet by the way so
[6184.20 --> 6190.28]  everyone should like rss feed that like hands down like incredible writing um and thank you for all the
[6190.28 --> 6196.44]  advocacy and the work that you do as well alex super appreciate you and so with that said we are
[6196.44 --> 6202.68]  gonna wrap kids it's been a long one many thanks i hope you learned a few things and hope you all get
[6202.68 --> 6218.28]  to play around with htmx and also lit play around with lit too all right take care everyone bye
[6220.28 --> 6231.64]  that is our show for this week thanks for partying with us next up on the pod front end feud yes our
[6231.64 --> 6238.76]  award-worthy game show is back and the css podcast is back to defend their title against our challengers
[6238.76 --> 6247.80]  from compressed.fm subscribe to the pod so you don't miss it head to jsparty.fm for all the ways or just
[6247.80 --> 6255.08]  search for js party in your podcast app of choice you'll find us thanks again to our partners at fly.io
[6255.08 --> 6260.84]  to our beat freak in residence break master cylinder and to you for listening we appreciate you spending
[6260.84 --> 6275.80]  time with us that is all for now but come back and party with us again next week
