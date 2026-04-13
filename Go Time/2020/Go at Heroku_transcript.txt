[0.00 --> 8.04]  what is up everyone adam stakowiak here editor-in-chief of changelog we teamed up with some
[8.04 --> 13.12]  friends of ours over at heroku to promote their podcast called codish you can check it out at
[13.12 --> 19.66]  heroku.com slash podcasts slash codish and today we're dropping a full-length episode of codish
[19.66 --> 26.04]  into the go time feed this episode features johnny boricico panelists on go time on the mic with
[26.04 --> 30.86]  guests ed moller and rasheed wasson talking about go at heroku here we go
[30.86 --> 44.72]  hello and welcome to codish an exploration of the lives of modern developers join us as we dive
[44.72 --> 50.44]  into topics like languages and frameworks data and event-driven architectures and individual and
[50.44 --> 56.28]  productivity all tailored to developers and engineering leaders this episode is part of our
[56.28 --> 63.08]  heroku in the wild series hello and welcome to codish my name is johnny boricico and i will be
[63.08 --> 70.16]  your host for this episode of codish today we will be talking about go at heroku i am pleased to be
[70.16 --> 75.46]  joined by two of my colleagues ed moller and richard wasson who will share their experiences with the
[75.46 --> 81.48]  language and add some color to how they've seen it used within the organization um so let's begin
[81.48 --> 87.66]  with you ed how long have you been at heroku and in what capacity uh let's say i've been at heroku now
[87.66 --> 99.18]  for uh eight years uh and during that time i've been on well pretty much all the teams um i started uh on our
[99.18 --> 106.40]  database team and transitioned through some infrastructure uh teams uh that worked on aws
[106.40 --> 114.28]  and eventually metrics and and logging after that i wanted a little bit of challenge and uh became the
[114.28 --> 122.84]  go language owner and uh eventually though found my way back to metrics and now into sre land uh where
[122.84 --> 130.66]  i'm working on uh go tooling uh some open telemetry stuff and uh generally observability uh but rishab
[130.66 --> 137.22]  um i know even less about you and what you've been up to at heroku so how long have you been at heroku
[137.22 --> 143.80]  yeah so i've been at heroku for about a year and a half um i'm pretty new to the industry this is
[143.80 --> 151.60]  actually like my first job and um a bit of a brief history about myself i recently graduated from
[151.60 --> 158.46]  uc berkeley about two years ago um after studying some computer science and prior to that i was
[158.46 --> 164.58]  actually a future force intern on one of the other clouds at salesforce called salesforce iot cloud
[164.58 --> 171.16]  and most recently i've started as a software engineer on the runtime infrastructure team
[171.16 --> 177.76]  very cool so as for me um i'm relatively new into heroku still i'd say at least you know
[177.76 --> 183.70]  relative to the two of you uh it's uh been what maybe my sixth i think i'm entering my sixth month
[183.70 --> 191.14]  at heroku uh i joined as an as an sre um and and ed and i are also part of the sre org within within
[191.14 --> 197.40]  heroku and this is this has been an awesome journey for me so ed i know you've been at heroku the longest
[197.40 --> 203.12]  so i know i know internally right now that you're definitely one of the people who looks after the
[203.12 --> 207.76]  build pack so whenever there's a there's a new version of go that comes out um sort of uh you're
[207.76 --> 212.48]  sort of one of one of the sort of the first people the org looks to to make sure that we're running the
[212.48 --> 216.54]  latest and greatest we're patching and we're basically you know keeping up with the the releases
[216.54 --> 221.22]  of go like can you can give us a little bit of insight into sort of what the process is like is it
[221.22 --> 226.50]  something that's difficult to do hard to manage like you know is is you have automation around it how
[226.50 --> 231.90]  how easy is it to keep the build pack fresh and serving our customers keeping go up to date on the
[231.90 --> 238.18]  build pack itself is relatively straightforward we have a little script inside the build pack repo
[238.18 --> 245.84]  itself that we can use to to do the work to bump versions and then things like ci and cd for the most
[245.84 --> 253.12]  part you know validate that the existing tests and everything are are good um there are challenges
[253.12 --> 260.14]  supporting every new major release so like go 112 to go 113
[260.14 --> 269.64]  uh etc etc etc um for instance like the default is currently still uh one of the go 112 lines um
[269.64 --> 276.06]  because there are a whole bunch of implications with uh turning to modules being the default on
[276.06 --> 283.80]  and yeah we're not yet sure we understand all of the implications of it from the standpoint
[283.80 --> 290.64]  of the build pack anyway and how that affects all the users of the build pack but the general process
[290.64 --> 295.78]  of like bumping for point versions and things like that is is really simple pretty much since i've been
[295.78 --> 301.38]  in heroku every new project it's it sounds like it's it's being written in go um but we still have a lot
[301.38 --> 306.22]  of projects that have been written in ruby um some new projects even are either ruby and we have some
[306.22 --> 314.16]  elixir as well um so we're truly a polyglot sort of organization um the we have a set of sort of go-to
[314.16 --> 319.72]  languages that we use um but go is increasingly being a a a sort of a one of the first ones we look at
[319.72 --> 324.18]  especially for for for back-end kind of systems and services that need to talk to each other that
[324.18 --> 330.46]  kind of thing so this is how we do metrics and how we do sort of uh um when folks hit the api.heroku.com
[330.46 --> 336.82]  um that stuff is is most of that stuff is in go private spaces are run um that most of that stuff
[336.82 --> 342.60]  is controlled in in go so we have a lot a lot of go so does that mean do you think does that mean we
[342.60 --> 348.94]  have a lot of go expertise in house and along those lines perhaps rishab you can sort of chime into this
[348.94 --> 355.04]  one how have you how easy has it been for you right coming out of school and this being your first job
[355.04 --> 360.08]  were you doing go you know at school or did you learn go on the job how easy has it been for you to
[360.08 --> 366.06]  sort of learn go and be productive with the language at heroku uh at college actually i never
[366.06 --> 373.16]  even heard of go um the main languages that i used was actually java and python and coming to heroku
[373.16 --> 378.92]  and starting my my first job uh it was quite a bit of a surprise just hearing that um i would be
[378.92 --> 386.12]  working in go and ruby and learning like a new language so specifically there were like a couple of
[386.12 --> 392.04]  resources that really helped me um gain a bit of an understanding about the go ecosystem and learn
[392.04 --> 399.46]  how i can actually like start writing um idiomatic go um for example the runtime team like specifically
[399.46 --> 406.70]  uh we have a program called runtime university and it has a huge section on go which it also references
[406.70 --> 413.26]  go by example and other resources where an engineer who is like relatively new to go or wants a refresher
[413.26 --> 419.42]  can actually go in and do some practical exercises and learn for example syntax about the language
[419.42 --> 426.94]  or like how to actually write um good go also for myself um one of the biggest things that has really
[426.94 --> 435.56]  um helped me learn go at a at a at a good rate is um reading a lot of go code so taking like an
[435.56 --> 441.92]  existing microservice that we have and then reading it end to end um really helped me understand how to
[441.92 --> 449.72]  build a service and go and then also when i'm making changes to an existing service um reading that
[449.72 --> 459.14]  whole like code base um was very helpful so i think overall um as like a new engineer uh we have some
[459.14 --> 466.18]  patterns at heroku such as like runtime university um that really support a new engineer um to learn
[466.18 --> 474.30]  some go so one of the things that that you as a go developer start to sort of uh hear as a new go
[474.30 --> 479.10]  developer you start to hear more and more of the more go you do is this concept of idiomatic go right
[479.10 --> 485.02]  so it's you could write go that looks kind of like java a little bit or some other language that you're
[485.02 --> 490.86]  familiar with you know but you wouldn't be sort of um sort of doing it the way most go developers do
[490.86 --> 494.84]  right so and this is something that basically is more subjective than it is sort of a you know a
[494.84 --> 499.04]  specific set of sort of a um you know if you don't write it a certain way then your code will compile
[499.04 --> 503.02]  kind of thing but it's more along the lines of this is the expectation right out in the go community
[503.02 --> 507.62]  and this is you know when you look at a go code base and ed i know you've been sort of the the
[507.62 --> 513.00]  leading sort of person internally behind our go design guide maybe you can sort of add some flavor
[513.00 --> 518.54]  there as to basically how much of sort of the the community's sort of concept right of idiomatic go
[518.54 --> 524.74]  how much of that basically is impacting or influencing uh how we approach go development internally
[524.74 --> 534.34]  i like to think of as our go design guide first of all it's a it's a living doc right so i uh expect it
[534.34 --> 545.02]  to evolve over time it's an attempt to basically try to get all the engineers on the same page about
[545.02 --> 554.66]  um how to structure projects and how to write um heroku's version of idiomatic go
[554.66 --> 565.94]  i do feel that a lot of things captured in that guide are inspired by the things you see in the
[565.94 --> 573.36]  community at large and for instance the guide has many call outs to everything from like dave cheney's
[573.36 --> 584.18]  blog um to yana's blog to the go wiki and things like that and usually has text um for
[584.18 --> 595.20]  purposes of clarification or to uh you know better relate the contents that are linked out to to the
[595.20 --> 604.04]  context of heroku and the types of services and tools that that that we need to write and like i said
[604.04 --> 612.24]  some of the the main the main motivation for me uh starting it several years ago was um as the go
[612.24 --> 620.02]  language owner then uh i would read a lot of go code internally and different projects were trying
[620.02 --> 628.00]  different things which is something you know we want to continue to encourage but as the code bases um
[628.00 --> 636.66]  go from experimentation phase uh into production and things like that in order to have that code base
[636.66 --> 645.30]  uh easily maintainable and modifiable by a large swath of engineers it my my opinion is uh that
[645.30 --> 655.32]  it's better if we do thing x in the same way um across as much of our code our go code bases as possible
[655.32 --> 663.90]  and the intent the attempt for the design guide is to say is to state what those ways are um and the
[663.90 --> 672.46]  reason uh and motivation behind why we feel that that is the right way for us to do it and to provide
[672.46 --> 679.86]  examples and all that context uh for uh for posterity uh and again since it's a living doc though it doesn't
[679.86 --> 685.46]  mean it's going to all like if we say do this for these reasons it doesn't mean in six months from
[685.46 --> 691.54]  now it might not give different advice for the same thing because we've learned something in the in the
[691.54 --> 701.84]  interim um and we have a process in place um through an internal rfc or request for comment um process uh
[701.84 --> 708.18]  to modify that doc and rishabh uh i know you want to add some flavor to that yeah um so i this is actually
[708.18 --> 713.04]  something i forgot to mention earlier the go design guide for myself has actually been like a fantastic
[713.04 --> 719.96]  resource as a new engineer um i think for example when i start working in a new code base um with like
[719.96 --> 725.90]  go like learning the learning the language as a beginner um you're always looking and asking around
[725.90 --> 732.64]  for patterns or questions around is the way that i'm writing this correct and does it make sense and
[732.64 --> 737.36]  the go design guide being there as kind of like an artifact that you can look at and
[737.36 --> 745.30]  see patterns and standards which to most people make sense um provides kind of like a sense of
[745.30 --> 752.56]  proof or like prior art to say hey this code makes sense because the go design guide references this
[752.56 --> 759.98]  pattern so i'm going to implement it this way and also um when doing code reviews for example um i also
[759.98 --> 767.10]  reference like the go design guide as a reason um as to why certain code should be written in a certain way
[767.10 --> 775.50]  so it provides a lot of examples and provides a lot of explanation as to writing um a good standard of go
[775.50 --> 785.36]  so as as someone who says sort of learn go on the job i do want to sort of ask though like as sort of a
[785.36 --> 792.62]  newcomer to go what have you found to be the hardest thing right to learn about the language what what have
[792.62 --> 796.78]  been sort of your stumbling blocks what things you keep coming back to and over and over that has
[796.78 --> 803.36]  taken some time to sort of sink in for you yeah so i think there were like a few things that i found
[803.36 --> 810.32]  difficult along the way when learning go um one of them was actually dependency management so knowing
[810.32 --> 816.64]  so different code bases used different tools to manage their dependencies some code bases that we have
[816.64 --> 825.10]  used depth others uses used go mod or modules so understanding like initially when i was starting
[825.10 --> 831.28]  i had no idea how like dependency management work can go so knowing when to use either was a big issue
[831.28 --> 838.62]  also a difficulty along the way that i had was knowing that the code that i was writing was idiomatic
[838.62 --> 846.56]  so i would look to other resources such as the go design guide or dave cheney's blog to really validate
[846.56 --> 853.00]  whether or not the code that i was right writing was idiomatic and another issue or another difficulty
[853.00 --> 859.76]  along the way was knowing if the pattern that i was using to solve a problem uh was appropriate at the
[859.76 --> 867.74]  time and it's very similar to writing idiomatic go but knowing if the solution that i had
[867.74 --> 875.88]  uh was appropriate and have you found if you found that uh basically team members to be sort of a
[875.88 --> 883.56]  go-to resources as well um so how much how much sort of a um face-to-face you have you had have you had
[883.56 --> 889.70]  to to to to do right and then how much of it do you think you spend in sort of a um pull request going
[889.70 --> 894.12]  back and forth kind of thing like did you find have you thought i guess what i'm asking what has the
[894.12 --> 899.26]  experience overall been like for for somebody who's didn't know go before and has has sort of been
[899.26 --> 905.58]  learning on the job yeah definitely um so i think being very new to go um just asking a lot of
[905.58 --> 912.70]  questions and always questioning like why something was done the way it was done um so just being open
[912.70 --> 917.54]  to like asking a lot of questions especially to like senior engineers who've been like writing go for
[917.54 --> 925.76]  a multitude of years and specifically in pull review or pull requests um asking targeted questions to
[925.76 --> 931.52]  the reviewers and saying hey does this section of code make sense based on this pattern that i found
[931.52 --> 939.62]  here and really soliciting specific feedback um so yeah i also definitely took advantage of like
[939.62 --> 945.00]  pairing uh while doing code reviews so we would hop on a call together uh look at the code together and
[945.00 --> 952.30]  i would explain and do some kind of like a walkthrough um explaining the reasons why it took um when
[952.30 --> 958.34]  writing a certain piece of code and really got a chance to add some more flavor to the code review
[958.34 --> 965.34]  process so ed i'm curious do you do you think your journey i mean you've been doing go for many many
[965.34 --> 972.86]  years um what do you where do you see yourself at this point in your sort of a career in terms of you
[972.86 --> 977.36]  know your your your expertise with go like do you do you still think the language has a lot to offer
[977.36 --> 983.56]  you you still you still think you there's a lot to learn like is it the has the way you've written
[983.56 --> 989.52]  go along those lines has the way you you write go today has that changed over the years oh it's totally
[989.52 --> 999.16]  changed um goes not my first language um it's maybe my seventh eighth sixth something like that language
[999.16 --> 1005.74]  professionally i did what everybody does or at least i assume what everybody does when they first
[1005.74 --> 1017.62]  learn a new language and that is mix in you know styles picked up and or used in their uh in the
[1017.62 --> 1024.76]  language that they used previously most previous to ruby for instance i had used python a lot so when i
[1024.76 --> 1031.68]  first came to ruby i wrote my ruby like python um and was quickly yelled at by a bunch of rubyists
[1031.68 --> 1044.40]  um and uh so when i came to go i wrote what i currently call um gooby which is the mishmash of go and ruby
[1044.40 --> 1053.48]  which i've seen plenty of i've also seen plenty a guython i've seen plenty gava um i i've seen all of
[1053.48 --> 1059.50]  these and i and i'm not and i don't say that to like cast derision on the people doing that but i i
[1059.50 --> 1068.04]  believe it's also important to recognize that that's part of the process of getting like transitioning and
[1068.04 --> 1074.86]  and and and learning uh a new language uh as far as uh new people coming into go though i think like
[1074.86 --> 1080.00]  uh i think the best thing we can do for new engineers is pair with them uh and pair with them
[1080.00 --> 1092.16]  on um specific uh tasks i have offered and continue to offer pairing um with any any engineer on any
[1092.16 --> 1100.36]  project and uh those who have taken me up on it the sessions have been most productive i i believe for
[1100.36 --> 1109.38]  myself as well kind of experiencing the beginner mindset uh which i'm so removed from now so uh you
[1109.38 --> 1117.04]  know experiencing that firsthand and then uh i hope for them as well because i i you know through that
[1117.04 --> 1126.22]  process of pairing we can explore like the design philosophies that i think are enigmatic go where
[1126.22 --> 1132.60]  some early attempts at this people i was pairing with attempted to use me as like an as i go encyclopedia
[1132.60 --> 1140.72]  and i i feel like neither one of us uh you know neither party came away from that experience uh
[1140.72 --> 1148.14]  feeling like they had gotten good use of that time uh so that's something else i i recommend for more
[1148.14 --> 1155.70]  senior go engineers when you when you offer something or do pairing with somebody uh try to do it on a
[1155.70 --> 1163.38]  like have a specific focus um and a goal to accomplish you know refactor uh new implement
[1163.38 --> 1170.08]  something new uh both of those whatever not just like hey look at this code and tell me how it could
[1170.08 --> 1177.34]  be better because there's no there's no absolute right answer to that it it involves too many contexts
[1177.34 --> 1187.18]  right that are specific to the the project how the deployment uh the engineers involved etc etc where
[1187.18 --> 1195.38]  where do we see go sort of uh going at heroku the obviously we've already mentioned that a lot of our
[1195.38 --> 1202.20]  a lot of our control plane um software is written in go and you know everywhere i turn i think you know
[1202.20 --> 1208.14]  within the organization i see more and more go do you think that's that's sort of the the the language
[1208.14 --> 1213.80]  the the bulk of the of the engineering teams at heroku are going to be writing software for the
[1213.80 --> 1223.90]  foreseeable future um in your mind i'd certainly like that um i i suspect um a lot of rubyists might
[1223.90 --> 1230.20]  uh be more immediately attracted to something like elixir that's a theory not something i know
[1230.20 --> 1238.36]  uh but i think elixir can give uh like the rubyist some of the advantages that you would get from go
[1238.36 --> 1243.88]  while keeping some of the things that they like about ruby and those are the same a lot of those
[1243.88 --> 1250.12]  things are the same things that kind of drive me crazy about ruby um and you know ruby and go are
[1250.12 --> 1260.14]  different um with that said uh i do think like go is embedded into our infrastructure um to
[1260.14 --> 1271.10]  the extent that it will likely continue to be uh one of one to four primarily primary languages that
[1271.10 --> 1278.88]  haroku engineering ends up using um especially while things like docker and kubernetes uh and stuff like
[1278.88 --> 1287.18]  that continue to um kind of like dominate mindshare uh in the industry so rishab what what are you most
[1287.18 --> 1293.22]  looking forward to um on your end with regards to working with go are you do any project you get
[1293.22 --> 1299.06]  to work on or that that involves go you're happy with or do you have a specific kind of project that
[1299.06 --> 1303.98]  you find the most fun to write in go like where where where your head where's your head at so
[1303.98 --> 1309.42]  currently i have the pleasure of actually writing a new service that actually deploys to our kubernetes
[1309.42 --> 1317.70]  clusters in a secure and scalable fashion and that service is where didn't go so it's been kind of
[1317.70 --> 1322.00]  like a journey for myself in the sense that it's like a foundational project where i get to actually
[1322.00 --> 1329.60]  like bootstrap a new service and go and like really figure out for myself um good design patterns and
[1329.60 --> 1337.34]  writing good go code so it gives me the space and the time to actually experiment and learn
[1337.34 --> 1344.92]  um which i'm pretty happy about well i am glad we're able to to have this chat and and i personally
[1344.92 --> 1351.74]  learned a bit more about how provoked users go and and knowing that there are folks who are sort of a
[1351.74 --> 1356.90]  brand new to go in the organization as well um that are sort of uh learning how to how to write go
[1356.90 --> 1363.70]  um and how to write idiomatic go and and folks like uh rishab and also folks like ed who have been
[1363.70 --> 1369.50]  doing it for a while i'm providing some guidance and and you know me having joined the organization
[1369.50 --> 1374.82]  and knowing knowing that go was a was one of the determining factors for me joining the organization
[1374.82 --> 1380.00]  i'm glad to see that there's there's there's a lot more um to the org a lot more to the services and
[1380.00 --> 1385.98]  everything else that we're doing that that's written in go and that makes me happy so i am uh yeah i'm
[1385.98 --> 1390.88]  grateful that we're able to sort of get on the chat have this chat uh and thank you for being i guess
[1390.88 --> 1394.52]  i'm sure today yeah yeah thank you thanks for hosting thank you johnny for having me
[1394.52 --> 1402.14]  thanks for joining us for this episode of the codish podcast codish is produced by heroku the
[1402.14 --> 1406.74]  easiest way to deploy manage and scale your applications in the cloud if you'd like to
[1406.74 --> 1412.78]  learn more about codish or any of heroku's podcasts please visit heroku.com slash podcasts
[1412.78 --> 1413.28]  you
