[0.00 --> 12.18]  This is JS Party, your weekly celebration of JavaScript and the web.
[12.68 --> 18.86]  Thanks as always to our partners at Fastly for shipping all of our pods super fast all around the world.
[22.52 --> 24.84]  Check them out at Fastly.com.
[24.84 --> 32.22]  And to our friends at Fly, host your app servers and database close to your users, no ops required.
[32.66 --> 34.36]  Learn more at fly.io.
[34.92 --> 38.14]  Okay, hey, it is party time, y'all.
[46.24 --> 48.76]  Hello, world. It's your internet friend.
[48.88 --> 53.90]  I'm Jared, and I am excited to party with two of my JS Party friends.
[53.90 --> 54.96]  What's up, Nick?
[55.42 --> 56.04]  Ahoy, hoy.
[56.68 --> 59.22]  Ahoy, hoy. Back at you. What's up, K-ball?
[59.54 --> 60.94]  Happy to do this on a Friday.
[61.16 --> 65.32]  I started rocking out a little too much to the music, though, and my body's like, what are you doing, man? You're 41.
[66.98 --> 69.24]  Wow, your body talks to you like that. It's kind of strange.
[69.60 --> 70.48]  That's the skill I don't have.
[70.48 --> 71.98]  Yeah, it sounds like, ow!
[73.86 --> 74.88]  Love it, love it.
[74.88 --> 86.26]  Well, as always, we are excited, which is, I think, probably, if JS Party had a word, especially if Nick had a word, as I listen to many of Nick's shows in production, it's the word excited.
[89.86 --> 91.04]  Nick is always excited.
[91.12 --> 92.14]  What would my word be?
[92.98 --> 95.54]  Aha! I found you, you stinking bug!
[95.90 --> 96.90]  That's your word right there.
[96.90 --> 107.22]  Today, we are going to talk about something that I had never heard of before, so that's cool. It's called Class Variance Authority.
[107.48 --> 112.22]  Listener Michael brought this to my attention via our episode request form.
[112.22 --> 116.72]  Yes, we take requests at jsparty.fm slash request.
[116.84 --> 118.00]  We do want to hear from you.
[118.38 --> 120.52]  What would you like to hear about on the pod?
[121.14 --> 129.26]  Michael says, this thing, Class Variance Authority, which sounds very official, seems like, he doesn't say that, I just said that.
[129.38 --> 130.34]  Here's what he says.
[130.70 --> 136.78]  Seems like a wonderful DX for applying Tailwind styles, but nobody seems to be talking about it yet.
[137.54 --> 139.86]  Would love to know more about it.
[139.86 --> 145.96]  This is a library from Joe Bell, and I think Michael wanted us to get Joe Bell on the show, but we didn't do that.
[146.04 --> 148.34]  Instead, we got this on the show.
[152.62 --> 155.36]  Can you explain it like I'm five?
[155.98 --> 162.52]  So, yes, we are playing for the first time in months, Explain It Like I'm Five.
[162.52 --> 167.60]  And so we have the master explainer here from Monad's Hook.
[167.72 --> 168.74]  It's Nick Neese.
[168.74 --> 173.16]  See, who can weave tales that we all enjoy listening to.
[173.64 --> 178.98]  Nick has volunteered to explain Class Variance Authority to us like we're five.
[179.22 --> 179.96]  Nick, take it away.
[180.32 --> 184.76]  You just said that I can explain tales, but today I'm just full of wind.
[185.10 --> 185.54]  Oh.
[186.08 --> 186.62]  Oh, no.
[188.22 --> 189.90]  Is that going to be the theme today?
[190.18 --> 191.18]  We're not actually.
[191.40 --> 192.78]  Disclaimer, we're not actually five.
[192.78 --> 194.12]  We're not.
[194.36 --> 196.64]  And it's going to be hard.
[196.74 --> 198.94]  I am so excited about this library, though.
[199.34 --> 201.06]  And I do love the name, too.
[201.12 --> 205.78]  It's like I don't live in a city that has like a port authority or anything like that.
[205.78 --> 208.26]  But I just that's what I think of when I hear this name.
[208.32 --> 210.04]  So that's really cool.
[210.04 --> 215.06]  But this tool lets you combine classes together.
[215.06 --> 221.52]  And so it like lets you define your own action figures and then play with them.
[221.78 --> 223.86]  Anyway, I'm trying to explain this to a five-year-old.
[224.84 --> 225.92]  And you get you get to.
[226.06 --> 229.44]  So like sometimes you have lots of different Legos, let's say.
[229.70 --> 229.90]  Right.
[229.96 --> 231.54]  You have all of these tailwind classes.
[231.70 --> 233.06]  Those are action figures or Legos?
[233.12 --> 233.46]  Where are we going?
[233.76 --> 234.84]  I knew you'd call me out.
[237.42 --> 239.12]  Two levels of abstraction, Jared.
[239.12 --> 242.74]  The Legos are the styles and the action figures are the classes?
[244.26 --> 244.66]  Yes.
[245.16 --> 245.48]  Okay.
[246.10 --> 247.16]  No, I don't know.
[247.26 --> 249.20]  I was going to say, K-Wall, you're giving him too much credit here.
[250.00 --> 250.40]  No.
[251.24 --> 253.66]  He just switched objects on accident.
[254.08 --> 254.10]  I did.
[254.10 --> 256.62]  And he's like, Legos make more sense than action figures.
[256.90 --> 257.06]  Yeah.
[257.06 --> 257.44]  Okay.
[257.60 --> 260.46]  So he's the AI with no memory.
[260.88 --> 261.12]  Yes.
[261.12 --> 261.86]  That's what's going on.
[261.92 --> 263.92]  So he wants us to forget and start fresh.
[264.02 --> 264.20]  Okay.
[264.26 --> 264.80]  You got Lego.
[264.88 --> 265.80]  You're building Legos.
[266.00 --> 266.14]  Go.
[266.14 --> 268.78]  See, you got these connects and you build.
[272.50 --> 274.68]  You've got these Lincoln Logs.
[275.94 --> 276.86]  Those are cool.
[276.98 --> 278.76]  All you can build is like a log cabin though.
[279.00 --> 279.38]  That's all it.
[279.50 --> 280.58]  Oh, you can build a whole farm.
[281.02 --> 281.26]  Yeah.
[281.78 --> 282.02]  Well.
[282.62 --> 284.34]  You can build various log cabins.
[284.64 --> 286.96]  What does this have to do with class variance authority?
[288.48 --> 291.90]  This authority is the one that gives you the permits to build those homes.
[292.36 --> 292.88]  No, but.
[293.24 --> 293.40]  Okay.
[293.40 --> 299.92]  So you got these, these Duplos and individually, you know, they're great, but they come in all
[299.92 --> 301.52]  shapes and sizes individually.
[301.78 --> 304.08]  You know, it's not very creative to just have them on their own.
[304.16 --> 307.16]  You combine them together to make something better.
[307.86 --> 314.48]  And sometimes if you were a really skilled five-year-old, you're going to have like an
[314.48 --> 318.84]  assembly line where, you know, offsite, you're going to build the, um, the trusses for the
[318.84 --> 319.58]  roof or whatever.
[319.58 --> 324.36]  And, and then you're going to ship those to the build site to actually put them together.
[324.36 --> 324.80]  Right.
[324.82 --> 327.76]  You're not going to be like smelting everything right there.
[327.76 --> 330.58]  You're going to be building these things offsite and bringing them over.
[330.58 --> 339.22]  And so what CVA lets you do is to do that building offsite, not in your react component or in
[339.22 --> 345.06]  your, your component of Svelte, Astro, uh, view, any of those, like it can be used anywhere.
[345.28 --> 347.26]  You're not going to be doing it directly in the component.
[347.26 --> 352.30]  Instead, you're going to be doing it in this, this, uh, class variance authority object.
[352.30 --> 357.44]  And you can define that when you you're building this type of variant.
[357.44 --> 360.58]  So maybe you have your, you know, your roof piece.
[360.58 --> 361.44]  Are those called trusses?
[361.46 --> 362.08]  I don't even know.
[362.54 --> 364.00]  Showing my ignorance here.
[364.38 --> 365.18]  Don't ask me, man.
[365.42 --> 366.48]  I'm a software developer.
[367.42 --> 368.42]  The triangle things.
[368.60 --> 368.78]  Right.
[368.84 --> 370.32]  I think trusses sound good.
[370.78 --> 371.00]  Sure.
[371.30 --> 372.14]  Those are built.
[372.14 --> 373.70]  Can we go back to smelting for a moment?
[373.88 --> 377.36]  Because surely child labor laws come into effect at a certain point.
[377.76 --> 380.00]  I mean, can a kid be smelting at five?
[380.00 --> 383.84]  In certain States, it's probably found including ours.
[384.14 --> 384.90]  Including ours.
[385.02 --> 385.12]  Yeah.
[385.20 --> 385.40]  Okay.
[385.60 --> 386.12]  Fair enough.
[386.56 --> 387.26]  Five year olds smelting.
[387.36 --> 387.68]  Keep going.
[387.84 --> 388.06]  Yeah.
[388.48 --> 390.70]  We don't condone that on JS party, by the way.
[390.82 --> 391.88]  No, there should be at least six.
[392.26 --> 392.88]  It's like Nebraska.
[393.12 --> 395.68]  It's not for everyone, but it is for five year olds smelting.
[396.14 --> 396.48]  That's right.
[398.06 --> 399.68]  So yeah, you put those together.
[400.04 --> 404.06]  There are these variants that you can put together with all of the building blocks that
[404.06 --> 405.86]  would be in that.
[405.86 --> 409.88]  And then you can have these different pieces that then you can combine into the actual
[409.88 --> 414.66]  components or shapes or Lincoln log homes that you want.
[414.78 --> 415.40]  Duplos, man.
[415.48 --> 416.42]  You're stuck on Duplos.
[416.66 --> 417.18]  Yes.
[417.62 --> 422.88]  And so when you actually go to use those, you've got those all defined and shipped and put together
[422.88 --> 423.84]  as separate pieces.
[423.84 --> 430.12]  And then you can use those pieces to combine together to make your actual components and
[430.12 --> 436.38]  combine them together with mixing in your props and your styles to actually create the
[436.38 --> 437.44]  components that you want.
[437.44 --> 446.72]  And this is really great idea because it lets you manage those as your own custom blocks.
[446.72 --> 451.36]  Because when you're putting those little Duplos together, you're making bigger Duplos that
[451.36 --> 453.00]  are your own custom Duplos.
[453.70 --> 459.46]  And then you can just apply those custom Duplos everywhere in a more manageable way.
[460.22 --> 462.78]  And that is what CVA is letting you do.
[463.10 --> 465.08]  So I'm totally lost in the metaphor.
[465.08 --> 467.38]  Can you explain it to Cable like he's 41?
[467.88 --> 468.80]  I know, right?
[469.12 --> 471.60]  Or maybe this time use magformers, right?
[471.70 --> 474.36]  And that's going to help us because they'll...
[474.36 --> 474.64]  Whoa.
[475.54 --> 475.94]  Yeah.
[476.32 --> 477.94]  I don't know what magformers are.
[478.00 --> 478.78]  I wasn't that cool.
[478.92 --> 483.20]  Oh, they're these cool magnetic things that snap together.
[483.40 --> 487.36]  They're also number six on the list chat GPT gave me for alternatives to Lego.
[487.36 --> 487.72]  Okay.
[491.30 --> 491.66]  Yeah.
[491.80 --> 492.80]  Maybe let me try...
[492.80 --> 496.08]  Let's explain it in normal style and see if we can follow because...
[496.08 --> 496.62]  Yeah, yeah, yeah.
[496.74 --> 497.44]  That's what I was going to do.
[497.44 --> 498.56]  Explain to a 41-year-old.
[498.70 --> 499.44]  Yeah, yeah, yeah.
[499.44 --> 504.56]  So what this lets you do is it lets you define these variants in different fashions.
[504.70 --> 510.18]  And so you can say, give a list of variants and they call them intents in there.
[510.28 --> 514.24]  And the intent would be like what you would pass as like a...
[515.04 --> 521.12]  You'd pass an object to the CVA function that you create and they call them intents.
[521.18 --> 524.66]  So you could say like my intent is primary, but I would call them like variants, right?
[524.66 --> 526.88]  Or I would call it variant specifically.
[527.28 --> 530.98]  So let's say you're creating like a button and you might have like a primary button and
[530.98 --> 534.96]  a secondary button and your primary colors for one, secondary colors for the other.
[535.10 --> 537.20]  And it switches between the two of those.
[537.68 --> 542.10]  Then you might have other variant pieces of that where you might have different sizes.
[542.10 --> 547.54]  You might have like a small button, a medium-sized button, or like a full width button where
[547.54 --> 549.02]  it takes up as much space as it can.
[549.50 --> 552.08]  So you'd have all of those together as different variants as well.
[552.08 --> 557.58]  And what you want to do is be able, you call CVA and you can pass in a number of classes
[557.58 --> 560.94]  that are just always applied as an array as the first argument.
[561.24 --> 566.08]  And then the second argument is an options object that you can pass in these variants.
[566.08 --> 571.66]  And so we could call that inside of the variants, we could have like a variant or call it intent.
[572.08 --> 577.78]  And then you could have like size and any other properties that you would normally pass to
[577.78 --> 580.82]  a button, whether it's disabled or not, for example.
[580.82 --> 587.48]  And then you can say that when the variant is of this value, meaning like primary, then
[587.48 --> 588.64]  you apply these colors.
[588.64 --> 592.92]  Like you could have like a green color for the primary button and a white text color.
[593.20 --> 599.24]  And then for the secondary, you could have it be a blue background color also with a white
[599.24 --> 600.22]  text color.
[600.72 --> 606.26]  And the way that you can apply those is through just passing in what values will be in the class
[606.26 --> 608.52]  name, like in React for the style.
[608.64 --> 613.84]  So what classes you're passing, which is why this works really well for Tailwind, because
[613.84 --> 618.78]  you've got tens of thousands of classes to pass and manipulate in there.
[618.84 --> 620.04]  So those are your Duplo blocks.
[620.56 --> 622.70]  And then it has this other cool feature.
[622.86 --> 627.78]  So when you do that, you just say like, you know, in your React component, you say, you know,
[627.78 --> 630.86]  return my button JSX.
[631.14 --> 637.48]  And then in the class name is where you can call CVA and pass in those values.
[637.48 --> 642.74]  You can call the value that you got back from CVA, which would be like your the classes to
[642.74 --> 643.56]  apply for a button.
[643.88 --> 649.22]  And then you can pass in what you want the variant to be, what you want the size to be.
[649.22 --> 656.10]  And it will automatically generate the appropriate class list and add it to that class name property
[656.10 --> 657.02]  for React.
[657.52 --> 658.08]  Okay.
[658.38 --> 659.54]  I think I'm with you.
[659.58 --> 660.36]  Cable, are you with him?
[660.78 --> 661.26]  I think so.
[661.38 --> 666.94]  So if I'm understanding, it's essentially a utility for central management of your CSS classes.
[667.26 --> 667.80]  Correct.
[668.12 --> 668.44]  Yes.
[668.62 --> 669.02]  Right.
[669.18 --> 674.90]  And allowing you to like group them based on some other, you know, semantic word that you
[674.90 --> 676.88]  choose, such as secondary.
[676.88 --> 680.72]  And secondary can represent these 10,000 tailwind classes.
[681.00 --> 682.80]  And primary can represent these other ones.
[683.38 --> 687.56]  And all you have to do is say primary or secondary, and it gets the right class list.
[687.68 --> 693.54]  And then you can also have this merging, munging thing where it seems like there's a tree there.
[693.70 --> 695.14]  I'm just looking at the data structure itself.
[695.80 --> 700.74]  And you can kind of have, you know, melding of the class list in order to get the right thing
[700.74 --> 702.66]  out with another name kind of a thing.
[702.86 --> 703.00]  Yeah.
[703.10 --> 705.86]  It has this ability to make compounds of that.
[705.86 --> 709.44]  So you can say when it's a primary of size large, also apply these.
[710.52 --> 717.30]  So I think there's value here, but it also feels like part of the value here is fixing
[717.30 --> 721.26]  the brokenness that is the way that tailwind makes you think about CSS.
[722.86 --> 724.20]  Well, if you think it's broken.
[724.56 --> 724.84]  Yeah.
[725.06 --> 726.24]  I'm prepared to have this war.
[726.24 --> 730.20]  Some people prefer this over CSS and JS or, you know.
[730.62 --> 732.36]  I am being deliberately provocative there.
[732.46 --> 739.24]  But I do think, so tailwind solves a set of problems and introduces another set of problems.
[739.68 --> 747.08]  And part of that another set of problems is the incredibly verbose class list that you end up with all the time.
[747.24 --> 747.48]  Right.
[747.48 --> 752.48]  Where in, you know, one of the things that tailwind does really nicely is it pushes you to standards.
[752.64 --> 752.96]  Right.
[753.00 --> 757.26]  And it says, okay, you're not going to worry about thinking about your spacing for every component.
[757.40 --> 758.62]  You have a class that is your spacing.
[758.74 --> 759.64]  It's always going to be the same.
[759.64 --> 762.20]  And you have like five of them and you can apply whichever one's appropriate.
[762.44 --> 763.32]  And that's great.
[763.32 --> 766.34]  And in a well-designed design system, you have that anyway.
[766.74 --> 768.70]  And you're composing them into your classes.
[768.70 --> 773.56]  You're not, you know, doing everything with, you know, starting your CSS over every time.
[773.86 --> 785.40]  So I think what I'm understanding here is it's kind of taking you that step of what I've heard in theory you're supposed to do with tailwind is you start to recognize, oh, here's the pattern of things that I put together all the time.
[785.50 --> 789.16]  Let me pull that out and make a new class out of it because I can reuse it.
[789.48 --> 789.56]  Right.
[789.58 --> 791.10]  But nobody actually does that.
[791.10 --> 794.72]  And this is saying here, let us make it easy for you to do that in JavaScript.
[795.12 --> 805.38]  So you don't have to worry about modifying your tailwind config and we'll solve the problem that tailwind introduced in a new way that maybe you're like more likely to use than the one that tailwind also introduced.
[805.62 --> 806.02]  Yeah.
[806.24 --> 807.08]  And nobody uses.
[807.58 --> 809.02]  It's exactly that, I think.
[809.12 --> 816.44]  And if you were to just do this in CSS, you know, you can use tailwinds at apply pragma in CSS and combine a bunch of classes together into one.
[816.44 --> 828.60]  And the downside of that is that you lose the dynamicness of doing it in JS where like CSS and JS is more beneficial because you can apply logic based on state and stuff.
[828.72 --> 828.82]  Right.
[828.82 --> 829.46]  Exactly.
[829.68 --> 836.08]  You would have to predefine all of those different states in those classes in CSS because you can't define them on the fly.
[836.08 --> 842.24]  And so this kind of lets you get the best of both worlds where you're doing it in this JavaScript way.
[842.40 --> 844.84]  And you're just saying when it's like this, I apply these classes.
[844.96 --> 846.24]  And when it's not like that.
[846.26 --> 849.88]  And really, there's nothing that's stopping you from just doing it in a vanilla way, too.
[849.98 --> 855.34]  But you just end up with a lot of like conditional or ternaries of like, you know.
[855.34 --> 867.02]  Right. It's moving you back to the declarative nature of CSS rather than what often ends up happening when you write too much CSS and JavaScript, which is this very imperative if this, then that and do your ternary and what have you.
[867.42 --> 867.56]  Yep.
[867.80 --> 871.30]  But you also get the benefit of this working.
[871.30 --> 883.38]  Like, so one of the pain points that I'm running into right now with my CSS and JS stuff is that I'm trying to use like Next13's new app directory and play with 3x server components.
[883.64 --> 895.92]  But every component that I use or create has to be a client component because it needs to access this JavaScript state to understand how to properly apply theme values and things like that.
[895.92 --> 903.18]  Whereas all of that actually, if we used Tailwind, all of that is predefined in Tailwind and with the Tailwind config and with those classes.
[903.46 --> 911.76]  So if it's just using JavaScript to try and figure out, you know, apply this class versus that class, it can be a server component and still work 100%.
[911.76 --> 920.90]  Right. So does Tailwind proper allow, like with this add apply deal, can you build the compound class list like this thing can?
[920.90 --> 926.96]  Like, is it feature for feature inside of Tailwind or is this giving you something you don't have there? I don't know.
[927.46 --> 934.20]  It is feature for feature in that. I've only done that a number of times in Tailwind with the add apply pragma.
[934.86 --> 938.94]  But it's just like, you know, I can define, you know, dot button.
[939.20 --> 943.86]  And then these are all the classes that it should apply from Tailwind whenever I use button somewhere.
[944.00 --> 945.60]  Right. And I can have one called secondary.
[946.22 --> 946.44]  Yeah.
[946.60 --> 949.46]  And I can say secondary button and it gets both.
[949.46 --> 951.76]  Right. You would have to have button and secondary together.
[952.22 --> 956.64]  Or I can say a secondary checkbox and it would get the secondary style.
[956.80 --> 967.16]  Well, checkbox is actually an input type, but I'm saying I can have some other component class and merge secondary with that and get the cross section of those two, the union.
[967.52 --> 977.38]  So the other interesting thing here that I think connects to that, so I'm going to jump in, is this is written in TypeScript and you're doing type safe composition, right?
[977.38 --> 984.98]  So this and this is a place where I think this actually has potentially unique or interesting value.
[985.10 --> 986.54]  It's not unique because I think there's other things.
[986.54 --> 1001.04]  But like what you can do with this then is, if I'm understanding correctly, is like your class that you've designed or your variant can like specify what types of things you can mix into it.
[1001.04 --> 1004.82]  Because you have like, here's the set of types this will accept as arguments.
[1004.82 --> 1012.42]  And you can pass in, okay, you know, this is a primary, this is a secondary, and those must satisfy these particular values.
[1012.42 --> 1016.84]  And so that now lets you create reusable modifiers.
[1017.02 --> 1025.82]  Modifiers that you can statically verify up front can apply correctly to whatever sets of components you're trying to modify them with.
[1025.82 --> 1055.80]  Yeah, exactly.
[1055.82 --> 1061.90]  And then pass in the type of the return type that I get from calling CVA with all of my defined things.
[1062.04 --> 1066.44]  And then it knows that I can pass in an intent of either primary or secondary.
[1067.06 --> 1069.92]  And if I don't pass it in, it has a default value of this.
[1070.54 --> 1076.66]  And so you end up not having to redefine everything over and over, which is, yeah, the cool TypeScript part of it.
[1076.66 --> 1076.70]  Yeah.
[1080.62 --> 1083.46]  Well, as always, TypeScript sucks all the air out of the room.
[1083.96 --> 1090.10]  And now we're all just, we're just basking in the glory of what is the cool TypeScript parts.
[1090.38 --> 1091.60]  Are there other cool parts?
[1091.66 --> 1093.16]  Is there, is there more to plumb here?
[1093.22 --> 1100.20]  Maybe we go above and beyond and do an episode with Joe, who can probably explain it like we're five better than we can.
[1100.20 --> 1102.98]  But cool idea, small little library.
[1103.14 --> 1103.78]  So that's nice.
[1104.00 --> 1107.22]  But the ergonomics look great from where I'm sitting.
[1107.98 --> 1110.78]  And especially if you're using Tailwind, I think it makes a ton of sense.
[1110.86 --> 1111.88]  If you're not using Tailwind.
[1112.26 --> 1114.70]  Looks like it works all right for those cases as well.
[1114.70 --> 1125.82]  And I, you know, I was pushing a little bit snarkily there because the value prop that Nick had laid out to me felt like it was mostly a value prop for Tailwind users who have this very long list of classes.
[1126.08 --> 1138.18]  But I actually think this type safe composition piece of it is super cool and will be, would be helpful for whatever approach you're taking to your CSS and design system.
[1138.18 --> 1149.54]  I have been looking at it through the lens of Tailwind because right now Tailwind seems like the really green grass on the other side of the fence that I really want to get to.
[1149.86 --> 1151.24]  It's always greener over there.
[1151.70 --> 1156.02]  But then when you get there, you realize actually it's the same as it was over here.
[1156.46 --> 1158.28]  That's what the whole cliche is about, Nick.
[1158.30 --> 1159.20]  I'm not sure if you know that.
[1159.38 --> 1159.76]  It is.
[1159.86 --> 1162.20]  But in this case, it's really, it really is.
[1162.20 --> 1163.32]  It actually is over there.
[1163.86 --> 1165.32]  That's what you'll think until you get over there.
[1165.32 --> 1165.58]  Okay.
[1165.68 --> 1167.92]  The library is called Class Variance Authority.
[1168.18 --> 1169.18]  You can call it CVA.
[1169.46 --> 1170.64]  That's what the function name is.
[1171.10 --> 1172.06]  It's a lot easier to say.
[1172.38 --> 1173.88]  At cva.style.
[1174.20 --> 1177.70]  So check it out if it can help you, especially if you're using Tailwind.
[1178.30 --> 1181.72]  As K-Ball says, it'll help fix some of those pain points that Tailwind has introduced.
[1182.62 --> 1185.56]  It's like fertilizer for that grass over there, you know?
[1185.98 --> 1190.52]  Put some nitrogen into the grass, make it actually greener on that other side of the fence.
[1190.52 --> 1199.30]  I'm Jared, and this is a changelog news break.
[1199.30 --> 1212.60]  In what appears to be a particularly security unaware move, Google has added eight new top-level domains, two of which are quite concerning, .zip and .mov.
[1212.60 --> 1213.64]  Yikes.
[1213.64 --> 1216.52]  Ars Technica writes, quote,
[1216.52 --> 1244.44]  End quote.
[1244.44 --> 1247.36]  Fishers and scammers rejoice.
[1247.36 --> 1256.28]  The rest of us, beware and be ready to help protect your family and friends from this otherwise completely avoidable new threat vector.
[1257.14 --> 1268.34]  The linked Ars Technica article demonstrates a few URLs scammers could now craft, and they're darn near indistinguishable from the legit URL, even to someone like myself with trained eyes.
[1268.34 --> 1276.66]  One such URL in the example is a Kubernetes release, which, yes, is distributed as a zip file.
[1276.66 --> 1282.24]  You just heard one of our five top stories from Monday's changelog news.
[1282.58 --> 1294.96]  Subscribe to the podcast to get all of the week's top stories and pop your email address in at changelog.com slash news to also receive our free companion email with even more developer news worth your attention.
[1295.38 --> 1298.86]  Once again, that's changelog.com slash news.
[1298.86 --> 1306.34]  Let's change gears now.
[1306.50 --> 1308.16]  K-Ball has a new stack.
[1308.66 --> 1310.40]  I mean, I'm a week into playing with it.
[1310.60 --> 1313.06]  So he's got a one week old little stack over.
[1313.16 --> 1314.08]  He's been working on it.
[1314.20 --> 1315.60]  One week old little stack.
[1315.78 --> 1322.42]  You know, I got inspired by the last episode that Nick and I did talking with the creator of Joist ORM.
[1322.42 --> 1328.24]  Because Joist sort of fit a couple of things that I've been looking for in the JavaScript ecosystem for a while.
[1328.94 --> 1339.74]  One piece was just a nice ORM that got back to feeling like the sort of productivity levels that I used to have with ActiveRecord and the Rails world and Ruby and Rails.
[1340.18 --> 1347.36]  And the other was something that is async and performant by default and does nice sort of coalescing and collection of different queries.
[1347.36 --> 1351.90]  So it makes it really easy to write very high performance backend code.
[1352.54 --> 1360.84]  And I paired that with playing around or introducing with Quick and QuickCity, which is something we've talked a couple of times with Mishko Heveria about.
[1361.24 --> 1370.70]  Because it does a very nice job of letting you get good developer economics while still being extremely performant by default in frontend land.
[1371.24 --> 1374.22]  And, you know, having good performance by default.
[1374.22 --> 1381.48]  And so where I've landed with this is, you know, frontend, backend with Quick and QuickCity as how I'm structuring my app.
[1381.68 --> 1386.88]  Now QuickCity has, you know, kind of a nice separation backend, frontend, so you can write your whole app.
[1387.08 --> 1389.72]  And then on for my data management using Joist.
[1389.72 --> 1404.96]  And now I have a nice little full stack JavaScript framework without having to, you know, pull together lots and lots of different pieces that looks like from my playing around with it for this week is going to be pretty productive.
[1405.32 --> 1409.90]  I still want to do a little bit more work to kind of, I like generators.
[1410.04 --> 1412.74]  I like things like that to like make it really fast to roll things out.
[1412.74 --> 1414.48]  And there's some already, but I want to do some more there.
[1414.90 --> 1424.18]  But the nice thing about it is it looks like I'll be able to reach very high levels of productivity while also being extremely performant by default.
[1424.30 --> 1435.88]  And I think that is a thing that I've been looking for for a while because we've had a lot of conversations on the pod about, you know, you build an app in the de facto framework, which is React.
[1435.88 --> 1438.22]  And it works great.
[1438.22 --> 1439.54]  And you're shipping a lot of JavaScript.
[1439.78 --> 1443.52]  And as you add more things, you're shipping more JavaScript and everything has to be booted up.
[1443.58 --> 1446.82]  And your app just kind of slows down over time as it gets more complex.
[1446.82 --> 1450.50]  And you have to do a lot of work to make it performant.
[1450.58 --> 1452.56]  It's not performant by default.
[1453.58 --> 1462.66]  And, you know, I think a lot of solutions that we have for backend data management also just are not performant by default.
[1462.66 --> 1467.72]  You have to think about how am I structuring my data access and how am I doing all those things.
[1467.80 --> 1477.06]  And this gives me both of those out of the box by default and in an environment that feels like it's going to be very good for productivity as well.
[1477.44 --> 1478.44]  Quick question for you, K-Ball.
[1479.02 --> 1484.14]  Could your quick city use a central variance authority to be responsible for the...
[1484.14 --> 1485.92]  You know, I was just thinking about that.
[1486.04 --> 1491.16]  I was actually thinking that I might try pulling this in and then I've got a full stack there.
[1491.16 --> 1492.50]  There I'm dealing with my styles.
[1492.60 --> 1494.90]  I've got something there and we'll see.
[1495.06 --> 1499.82]  So maybe I'll have to just, you know, I know there's a guy named Tanner who shipped TanStack.
[1499.90 --> 1505.48]  Maybe this will have to be K-BallStack and I'll, you know, ship you a wrapped everything up together.
[1505.86 --> 1506.16]  I don't know.
[1506.22 --> 1509.28]  I mean, as I said, I'm a week into tinkering with this, right?
[1509.30 --> 1513.26]  So I haven't had time to uncover all of the rough edges, all of the challenges.
[1513.26 --> 1522.68]  I haven't yet fully scaled something out, though, you know, having spent a while digging into these tools, I think that they should scale extremely well.
[1522.78 --> 1528.18]  They're built in a way that solves a lot of the scaling issues that I know I've seen in other places.
[1528.18 --> 1539.80]  But yeah, I will say the one big drawback I've found so far is these are tools that have been mostly developed after the training cutoff for ChatGPT.
[1540.34 --> 1544.02]  And they've mostly developed their less well-known tools.
[1544.14 --> 1548.00]  So I'm like playing around with Codium as a code completion thing.
[1548.12 --> 1553.54]  And it keeps trying to complete my migrations with configurations from a different migration tool.
[1553.54 --> 1557.94]  It keeps trying to complete things in ways where I'm just like, you know what?
[1558.94 --> 1563.12]  Using newer technology means that the AIs don't know about them yet.
[1563.20 --> 1565.02]  And that is not great.
[1566.18 --> 1580.08]  Yeah, I think at some point there will be standardized tooling for all libraries, services, etc., where they can embed their docs or their knowledge into all of the AIs that you might want to use.
[1580.08 --> 1584.90]  And so you'll have more quick information about QuickCity, for instance.
[1585.50 --> 1586.84]  That being said, have you tried BARD?
[1587.02 --> 1593.08]  Because BARD now is competing with ChatGPT and has full access to the internet.
[1593.60 --> 1600.24]  I found it to be just as wrong with certain things, but more up to date with its incorrect information.
[1600.92 --> 1602.50]  I have not tried BARD for coding yet.
[1602.84 --> 1607.36]  GitHub Copilot for docs is a natural home for things like this.
[1607.42 --> 1609.12]  Is that part of GitHub Copilot X?
[1609.12 --> 1610.86]  It is. I think it's still in beta right now.
[1610.98 --> 1612.64]  And it's like a limited subset.
[1612.76 --> 1614.88]  It's like React and TypeScript and a couple of others.
[1615.12 --> 1616.70]  But you can ask questions to the docs.
[1616.92 --> 1619.22]  Kind of like Astro's Houston.
[1619.82 --> 1620.14]  Right.
[1620.44 --> 1625.22]  Yeah, I think that will become standardized to where everybody will be able to just roll out.
[1625.36 --> 1630.90]  You build a new library, you write your docs, and you just plug into the ecosystem.
[1631.22 --> 1633.54]  And all the tools know about it.
[1633.68 --> 1635.20]  So eventually we'll get there.
[1635.26 --> 1636.42]  It's still early days.
[1636.42 --> 1636.46]  Right.
[1636.90 --> 1640.56]  So KBAL, on your full stack, what's your backend?
[1640.80 --> 1644.24]  It's joist, but are you proxying to Postgres, SQLite?
[1644.32 --> 1645.26]  You got Mongo on the backend?
[1645.78 --> 1646.06]  Postgres.
[1646.06 --> 1646.18]  Postgres.
[1646.32 --> 1646.54]  Okay.
[1646.80 --> 1648.14]  Because that's another piece.
[1648.50 --> 1650.36]  Postgres just kind of works everywhere.
[1651.02 --> 1653.68]  You can run it locally, but you can also scale it way up.
[1653.68 --> 1655.34]  It's got all sorts of plugins.
[1655.56 --> 1663.60]  So if you want to do a fancy vector store, you can get started with a Postgres plugin and doing your vector stuff.
[1663.90 --> 1665.18]  We're all in this AI world.
[1665.26 --> 1666.04]  What are we doing here?
[1666.52 --> 1668.50]  But JSON-B is really great.
[1668.50 --> 1673.70]  So if you have unstructured document data, you just want, or lightly structured document data, you want to be able to dump in there.
[1673.98 --> 1676.18]  It's got support for that.
[1676.28 --> 1679.78]  You don't need something that's like a Mongo or whatever with all of its challenges.
[1680.14 --> 1687.44]  But then also for the core relational data that makes up the bread and butter of many applications, it just works.
[1687.76 --> 1688.46]  And it's fast.
[1688.46 --> 1692.64]  So is Quick and QuickCity, and I don't understand the distinction between the two.
[1692.76 --> 1696.00]  I know one is like the UI deal and the other one's like...
[1696.00 --> 1698.90]  Quick is to React as QuickCity is to Next.
[1699.20 --> 1699.56]  Okay.
[1699.66 --> 1701.14]  So QuickCity is the framework.
[1701.80 --> 1703.62]  And is it, that's a full stack framework?
[1703.80 --> 1712.46]  Like you submit forms to yourself and you have server-side code that you are still inside of QuickCity writing like endpoint handlers?
[1712.46 --> 1716.38]  Or is it, what's it look like on the back in like an express kind of thing?
[1716.82 --> 1717.42]  Yeah, basically.
[1717.42 --> 1723.04]  They have some affordances because they kind of control the bundler piece for QuickCity.
[1723.14 --> 1735.56]  So there's some things that you can, you know, you can actually do type safety across front end and back end and make sure you have the types the same and things like that in a nice way without having to bundle all of your back end code up to your front end.
[1735.82 --> 1737.88]  Because they cheat, basically.
[1738.96 --> 1739.74]  What do you mean by that?
[1740.02 --> 1741.42]  They do some things that are not...
[1742.02 --> 1747.40]  So they kind of go down the Svelte road where they're extending the JavaScript language and they're breaking semantics.
[1747.42 --> 1750.52]  And they do it in a predictable way.
[1750.76 --> 1754.40]  They do it so that they can make various types of optimizations and other things.
[1754.94 --> 1764.68]  But they've essentially, and this is something we've talked about before, but they've extended the JavaScript language to make a little micro DSL that has slightly different semantics than JavaScript.
[1764.68 --> 1778.24]  So what I guess maybe I should go back and listen to the deep dive episode because some of this is ringing a bell.
[1778.42 --> 1781.42]  But what exactly are they doing to do that?
[1781.42 --> 1789.26]  So one of the big things, and this is something that I'm still, you know, as I'm playing with this, wrapping my head around all the implications.
[1789.26 --> 1793.94]  So like we should, we could come back to this in a month or two and I'll be able to go much deeper on this.
[1793.94 --> 1809.80]  But one of the things that they do is they have a, essentially a set of, or a way of identifying functions that tells their bundler, this can be run either server side or client side.
[1809.80 --> 1823.92]  And they kind of hoist those out of their context and package them up in a way so that when you hit like a quick app, it'll run up to a point on the server and essentially do a continuation over to the client.
[1823.92 --> 1840.26]  So then if, when somebody interacts with it, it's already ready to go and it's sort of packaged up, not just the application state of here's what's going on with my application, but actually the framework state of here's what was already rendered and what state the framework got to on the server side before this went out to the page.
[1840.42 --> 1845.16]  So that if they then, you know, click on that button or whatever it is, it can just keep running right from there.
[1845.16 --> 1857.60]  So to enable that, you know, if you end a function in a dollar sign, it is saying this is a function that is being behave or is behaving in a way where you don't actually know if it's running on the server or the client.
[1857.74 --> 1860.86]  And so you, you have to kind of constrain yourself a little bit and how you.
[1860.98 --> 1862.68]  Specific rules for those functions.
[1862.94 --> 1863.34]  Exactly.
[1863.58 --> 1864.04]  Makes sense.
[1864.66 --> 1866.68]  What if you're like me and all your functions are just money?
[1866.80 --> 1868.68]  So you're, you got dollar signs on all of them.
[1868.68 --> 1877.90]  Well, either you're going to set yourself up for a world of pain or you're going to adjust quickly and then all your money will be fast by default.
[1878.26 --> 1879.38]  I like the sound of that.
[1879.48 --> 1880.00]  Fast money.
[1880.38 --> 1882.22]  Easy come, easy go.
[1882.32 --> 1883.32]  What are you building, K-Ball?
[1883.46 --> 1884.74]  What are you working on, man?
[1884.92 --> 1885.52]  Can you tell us?
[1885.54 --> 1886.16]  Is it too early?
[1886.32 --> 1888.48]  No, I mean, I can tell you the idea.
[1888.92 --> 1891.56]  It's very early and it's not my main thing.
[1891.76 --> 1892.36]  And so like I'm.
[1892.36 --> 1893.24]  Do you have a pitch deck yet?
[1893.48 --> 1893.84]  Nope.
[1894.40 --> 1895.90]  Here, we're developing it right now.
[1895.92 --> 1897.36]  All right, let's develop your pitch deck.
[1897.36 --> 1902.86]  So the pitch deck here is a personal CRM that makes you the hero.
[1903.28 --> 1909.64]  So the idea is I have a lot of people that I wish I was better at keeping up with.
[1910.14 --> 1913.58]  And it's not that I, you know, mind reaching out to them.
[1913.62 --> 1914.64]  It's that I forget, right?
[1914.68 --> 1916.10]  Like when should I reach out?
[1916.12 --> 1917.38]  And I'm terrible at that.
[1917.42 --> 1919.94]  I'm terrible at remembering, oh, this is that person's birthday.
[1920.02 --> 1921.94]  I should send them a happy birthday or whatever.
[1921.96 --> 1924.36]  And I'm not on Facebook, so I don't get like those things.
[1924.36 --> 1931.58]  So the idea here is put somebody in, put important dates around it, set a sort of reminder cadence
[1931.58 --> 1935.00]  of like, hey, I'd like to talk with this person, you know, once every six months or whatever.
[1935.22 --> 1939.22]  And then it just nudges me and it, you know, six months have gone by, it sends me an email
[1939.22 --> 1942.96]  or text or whatever that says, hey, have you talked to so-and-so recently?
[1943.38 --> 1944.06]  You probably should.
[1944.06 --> 1948.88]  And the vision is I want to make it a little smarter so it can pull in my calendar.
[1949.12 --> 1954.90]  I can pull in our email history and from the calendar, it can keep track of when did I
[1954.90 --> 1956.56]  actually last have something with that person?
[1956.82 --> 1958.62]  So it could be smarter about reminding me though.
[1958.68 --> 1960.84]  For some things it might be, hey, so-and-so's birthday is coming up.
[1960.88 --> 1962.12]  You said you wanted to buy them a present.
[1962.34 --> 1963.56]  Now would be a time to do it.
[1964.08 --> 1965.02]  That type of thing.
[1965.42 --> 1971.20]  And if I get really far down the road experimenting with LLMs, I can take my email history and
[1971.20 --> 1973.92]  summarize for me and be like, here's the things that you-
[1973.92 --> 1974.62]  Don't you dare have to email them for you.
[1975.16 --> 1976.40]  I was going to suggest that.
[1976.80 --> 1977.66]  I know you were.
[1977.88 --> 1979.06]  Here's a key thing.
[1979.46 --> 1980.32]  Here's a key thing.
[1980.84 --> 1986.18]  I never want it to do something for me because I want to be the hero, not the app, right?
[1986.18 --> 1988.08]  It's never going to reach out to them for me.
[1988.52 --> 1992.66]  It's always going to nudge me and say, hey, you should reach out to this person.
[1992.90 --> 1995.58]  Maybe here's a suggestion of what you could talk about, right?
[1995.62 --> 1997.76]  Like, I know you've talked about these five things.
[1998.44 --> 2000.62]  You could write them an email that looks like this.
[2001.20 --> 2007.46]  But it's always putting the person in the driver's seat rather than, you know, and it's
[2007.46 --> 2011.70]  always about them, not about like the app.
[2012.32 --> 2012.44]  Right.
[2012.88 --> 2016.68]  Dearest Bob, do you remember that time that I reached out to connect to you on LinkedIn?
[2018.14 --> 2021.94]  That's scanning your email and then passing it to an LLM.
[2022.76 --> 2026.34]  I would still like to add you to my professional network, but I haven't heard from you.
[2026.34 --> 2032.40]  Well, it's kind of like, you know, a politician will have their person right there who's like,
[2032.46 --> 2034.98]  you know, they're shaking hands and they're like, here comes somebody.
[2035.10 --> 2037.76]  And the person's like, that's Frank George Paul.
[2038.06 --> 2039.04]  He's 47.
[2039.22 --> 2040.08]  He's got three kids.
[2040.36 --> 2041.70]  Two went to Stanford, you know.
[2042.04 --> 2043.50]  And you're like, oh, hey, Frank George Paul.
[2043.58 --> 2044.26]  How are the kids?
[2044.42 --> 2045.38]  You know, how's Stanford going?
[2045.78 --> 2047.74]  That is exactly what I want, right?
[2047.74 --> 2053.78]  I want something that is going to help me be the type of person in terms of remembering
[2053.78 --> 2058.92]  these people in these relationships that I would like to be at a much greater scale than
[2058.92 --> 2060.62]  I actually have the capacity to be.
[2061.00 --> 2061.38]  Okay.
[2061.58 --> 2062.22]  I would use that.
[2062.50 --> 2063.14]  Next buy-in.
[2063.54 --> 2067.12]  Well, right now it's a side project that I'm putting a few hours a week into.
[2067.32 --> 2069.22]  So, you know, we'll see where it goes.
[2069.46 --> 2070.44]  Now you're underselling it.
[2070.78 --> 2071.52]  You had a buyer.
[2071.66 --> 2072.70]  Now we're out again.
[2072.90 --> 2073.90]  Or we were in, now we're out.
[2074.94 --> 2076.06]  You know, I think I would use it.
[2076.06 --> 2078.80]  It would, it's really going to depend on the, on the execution.
[2079.18 --> 2080.82]  As all ideas do.
[2080.92 --> 2081.10]  Totally.
[2081.30 --> 2085.86]  Because I have some of that, like with, but with calendars, you know, you have birthday
[2085.86 --> 2088.36]  reminders, you have certain things.
[2088.40 --> 2090.46]  Obviously you can just use the reminders app.
[2090.52 --> 2091.04]  You can kind of like.
[2091.04 --> 2091.90]  You can cobble it together.
[2092.16 --> 2092.30]  Yeah.
[2092.30 --> 2093.16]  You can cobble it together.
[2093.16 --> 2098.62]  But having a solution that's really slick and handles all these diverse use cases, you
[2098.62 --> 2099.96]  know, where people work and live.
[2100.70 --> 2103.68]  If it did that for me, yeah, I might be interested in this.
[2104.42 --> 2104.64]  I don't know.
[2104.64 --> 2106.30]  It's also just fun to be coding again.
[2106.30 --> 2110.20]  Cause I hadn't been coding that much recently and it's good to be diving in.
[2110.42 --> 2110.76]  Right.
[2111.50 --> 2113.84]  What's the most fun part about coding?
[2114.36 --> 2116.06]  The most fun part about coding?
[2116.20 --> 2116.28]  I mean.
[2116.32 --> 2116.48]  Yeah.
[2116.48 --> 2118.64]  Like what, you know, it's good to be coding again.
[2118.64 --> 2118.92]  Why?
[2119.46 --> 2120.34]  What do you like about it?
[2120.64 --> 2121.40]  You ever think about it?
[2121.96 --> 2123.16]  I have been thinking about that.
[2123.16 --> 2124.06]  All right, Nick, go.
[2124.34 --> 2125.76]  Give all a chance to think.
[2126.42 --> 2131.42]  Well, I don't know that I have an answer, but I've been thinking about this because.
[2131.42 --> 2134.28]  Oh man, you really set me up and then you just let me down there.
[2134.66 --> 2137.56]  Like I've been thinking about that, but I haven't come to any conclusions.
[2138.26 --> 2140.36]  How long have we talked on this podcast before?
[2140.60 --> 2141.68]  I should know better.
[2141.68 --> 2149.36]  No, like I was thinking about this in terms of like LLMs and the future, like of this
[2149.36 --> 2153.14]  profession and all professions potentially, like what could it possibly do?
[2153.14 --> 2158.22]  And I think in the short term, at least, or maybe not the short term, but one of the things
[2158.22 --> 2163.48]  that I think that it can do is suck all of the joy out of what we do in terms of like
[2163.48 --> 2165.78]  what part of coding is actually fun.
[2166.14 --> 2170.94]  And that part can probably be done by the LLM and you're stuck with all the crap parts.
[2171.54 --> 2174.50]  And is that really what we want to do going forward?
[2174.50 --> 2175.46]  So what parts are?
[2175.58 --> 2176.00]  Okay, then.
[2176.10 --> 2178.28]  So you must have identified what parts are fun then.
[2178.28 --> 2182.98]  If you're like the man, like actually typing into a keyboard.
[2183.22 --> 2185.76]  Maybe not even that configuring my editor is like.
[2188.22 --> 2189.70]  That's where you and I diverge.
[2189.72 --> 2190.86]  Nick, you can do that for me.
[2190.92 --> 2191.64]  In fact, you do.
[2191.74 --> 2193.22]  I just suck down your dot files.
[2193.28 --> 2193.74]  That's right.
[2193.90 --> 2195.78]  That's basically how my editors configure.
[2195.92 --> 2198.42]  Nick configures all of our editors for us.
[2198.92 --> 2200.12]  You see who needs an LLM?
[2200.18 --> 2202.00]  You got Nick Neesey on your editor config.
[2202.18 --> 2205.68]  But then, yeah, like from there, like, I guess you want, I want to write code.
[2205.68 --> 2208.54]  I want to test that it actually works.
[2208.86 --> 2209.98]  My editor config, I mean.
[2210.58 --> 2213.24]  I think that's what for me, having put 30 seconds of thought into this.
[2213.32 --> 2214.90]  I think it works.
[2215.10 --> 2217.10]  Like those two words is the fun part.
[2217.12 --> 2217.70]  That's the fun part.
[2217.82 --> 2217.98]  Yeah.
[2218.38 --> 2226.64]  I think for me, I like the process of building up the mental model of what is this system
[2226.64 --> 2228.12]  and how do the pieces work together?
[2228.12 --> 2234.54]  And honestly, I think I actually like that even more coming into an existing piece of
[2234.54 --> 2237.34]  software, not writing like something from scratch.
[2237.72 --> 2244.52]  I love the exploration of like, wait, how is this all working together and how do I connect
[2244.52 --> 2244.76]  things?
[2244.80 --> 2248.34]  And so in some ways, like the fun part of my project right now, and one of the reasons
[2248.34 --> 2254.68]  it's moving pretty slowly and I'm not promising any progress is I'm using it as a way into like
[2254.68 --> 2257.50]  starting to dig into, wait, how is Quick actually doing this?
[2257.50 --> 2258.28]  How are they working?
[2258.38 --> 2259.48]  What is the, what are those pieces?
[2259.58 --> 2261.68]  And similarly, like how is Joyce actually working?
[2261.78 --> 2262.78]  Why isn't that working?
[2262.88 --> 2263.96]  Why is this going that way?
[2264.30 --> 2270.66]  And so using it as a kind of wedge into exploring these libraries, which to me is actually where
[2270.66 --> 2271.64]  a lot of the joy is.
[2271.64 --> 2274.70]  It's not in the writing, the lines of code itself.
[2274.70 --> 2275.60]  It's not in the testing.
[2275.60 --> 2277.04]  It works as nice.
[2277.48 --> 2285.18]  But really for me, the true joy is like when something clicks around, oh, that's how these
[2285.18 --> 2286.42]  things are working together.
[2287.50 --> 2288.38]  That's funny.
[2288.50 --> 2290.12]  We're so different because I couldn't care less.
[2290.28 --> 2291.70]  Like I don't want to know how it works.
[2291.98 --> 2293.78]  And when I have to, I get mad at the tool.
[2293.98 --> 2296.02]  I'm like, why am I reading this tool source code right now?
[2296.32 --> 2299.70]  Because it's not doing what the docs say or what I expect it to do.
[2300.14 --> 2302.66]  And I'm rarely ever happy because I just want it to work.
[2302.78 --> 2305.12]  Like I'm, I guess, pragmatic in that sense.
[2305.12 --> 2310.32]  Like I really am goal oriented or like I'm looking for a finished thing and everything else
[2310.32 --> 2315.72]  is just, you know, busy work and like, you know, stumbling blocks and this and that.
[2315.80 --> 2318.46]  And I do over time, I appreciate tools that work well.
[2318.76 --> 2321.38]  And over time you do learn a tool, even when it does work well.
[2321.60 --> 2322.92]  And I do appreciate that.
[2322.98 --> 2329.48]  But I don't usually have like, oh, that's why this thing won't, you know, lazy load like
[2329.48 --> 2330.18]  it's supposed to.
[2330.24 --> 2331.34]  I'm so happy I found out.
[2331.40 --> 2334.22]  I'm like, you should be lazy loading like you said you're going to.
[2334.22 --> 2335.86]  Well, and let me be clear.
[2336.16 --> 2339.26]  It's the mental model of how the thing works that I'm looking for.
[2339.38 --> 2340.32]  Everything fitting together.
[2340.46 --> 2341.40]  Everything fitting together.
[2341.58 --> 2345.34]  If I can get that from the docs and using it, I don't have to dive into the source code.
[2345.42 --> 2346.08]  Like that's fine.
[2346.68 --> 2346.88]  Sure.
[2347.62 --> 2348.08]  Fair enough.
[2348.60 --> 2351.28]  But neither one of you like to just tweak our editor configs like Nick does.
[2351.86 --> 2352.64]  No, no.
[2352.74 --> 2356.94]  I actually, it pains me every time I have to go and tinker with my editor config.
[2357.54 --> 2360.14]  That's why I just pull down from Nick and the things that aren't working right.
[2360.20 --> 2360.98]  I'm kind of like, damn it.
[2361.08 --> 2361.42]  All right.
[2361.54 --> 2362.20]  Well, damn it.
[2362.20 --> 2362.62]  All right.
[2362.62 --> 2366.76]  And just like kind of let it sit there because it's more painful to go in and try to figure
[2366.76 --> 2368.44]  out what the heck is going on with the editor config.
[2368.82 --> 2372.20]  If it's any consolation, I just sit there with them too for years.
[2372.36 --> 2374.54]  So we're struggling together.
[2375.72 --> 2378.86]  Yeah, but it's kind of your fault, Nick, because you know, you're the one in charge here.
[2378.90 --> 2380.12]  He's just riding your coattails.
[2380.62 --> 2384.20]  I'm probably struggling with the same things you're struggling with because I am literally
[2384.20 --> 2385.28]  using your config.
[2385.52 --> 2387.48]  Okay, I'll open up an issue on his repo.
[2387.64 --> 2388.06]  Come on.
[2388.12 --> 2390.10]  Be like, why is this not work right?
[2390.10 --> 2392.92]  That'll actually probably shame Nick into working on it.
[2393.02 --> 2393.94]  I know him well enough.
[2394.22 --> 2394.48]  It will.
[2396.20 --> 2396.56]  Noted.
[2396.60 --> 2397.42]  I know that about him.
[2397.86 --> 2400.38]  Well, now I'm actually coding again enough that it may happen.
[2400.94 --> 2402.04]  Yeah, that's cool.
[2402.32 --> 2402.88]  So there you have it.
[2402.92 --> 2403.90]  K-Ball's new stack.
[2404.16 --> 2408.40]  We'll see how it, maybe we'll catch up with you again in a few months and see how it's
[2408.40 --> 2412.54]  changed or stayed the same or what you've learned about how the whole system fits together.
[2412.54 --> 2419.54]  Or maybe you'll be ready to beta launch an announcement for a waiting list of making you,
[2419.68 --> 2421.28]  so what's the, it's called Zero to Hero?
[2421.50 --> 2422.36]  Is that what you said it was called?
[2422.78 --> 2424.00]  That's what you said it was called.
[2424.20 --> 2424.56]  Okay.
[2425.22 --> 2430.10]  My working, this is not what a marketing name, but my working name for it for myself, the
[2430.10 --> 2431.92]  name of the repo is NudgeCRM.
[2432.34 --> 2432.82]  I like it.
[2432.98 --> 2433.78]  Can I give you a tagline?
[2434.30 --> 2434.62]  Sure.
[2435.02 --> 2436.86]  Don't drop the K-Ball on this conversation.
[2436.86 --> 2440.00]  Oh, that might be too insider.
[2440.56 --> 2440.94]  K-Ball.
[2442.30 --> 2442.98]  Baseball, I mean.
[2443.68 --> 2444.52]  I do like that.
[2444.64 --> 2445.96]  Don't drop the K-Ball.
[2446.52 --> 2447.72]  They're like, what's a K-Ball?
[2448.00 --> 2449.00]  The guy who made it.
[2449.02 --> 2449.84]  The guy who made it.
[2449.90 --> 2452.96]  They're like, oh, why do I care about a guy who made it?
[2453.16 --> 2454.74]  Yeah, I don't, I'm not getting it yet.
[2455.08 --> 2457.30]  It's like, don't drop the ball, but don't drop the K-Ball.
[2457.54 --> 2458.30]  No, I get it.
[2458.82 --> 2461.38]  It's just that your customers are not going to know who K-Ball is.
[2462.72 --> 2463.64]  Here's a tip, K-Ball.
[2463.64 --> 2466.10]  Do not hire Nick as your chief marketing officer.
[2466.86 --> 2468.02]  At least not right away.
[2468.38 --> 2468.86]  You know what?
[2468.90 --> 2470.14]  That was already on my list.
[2472.46 --> 2473.02]  All right.
[2473.04 --> 2474.04]  We have a little time left.
[2474.10 --> 2478.86]  Let's turn to a few other things that are new and perhaps interesting.
[2479.40 --> 2481.26]  In the news, Bun.
[2481.72 --> 2482.54]  You guys know Bun?
[2483.34 --> 2486.74]  The super exciting alternative to Node.
[2486.96 --> 2490.26]  That's very fast and has captured the hearts,
[2490.26 --> 2493.74]  at least the interests of people on certain websites.
[2493.74 --> 2497.34]  Well, it has a brand new bundler.
[2497.90 --> 2501.72]  So they really put the d'ler into Bun, I guess you could say.
[2501.76 --> 2505.28]  I was going to say, why did they call it the Bun Bundler and not just the Bun D'ler?
[2505.48 --> 2505.98]  I know.
[2506.18 --> 2507.22]  Well, missed opportunity.
[2507.22 --> 2510.90]  But this is just announced a few days back.
[2511.10 --> 2514.90]  The Bun Fast Native Bundler.
[2515.36 --> 2516.18]  It's in beta.
[2516.50 --> 2518.00]  You now have a Bun build command.
[2518.80 --> 2520.92]  And I guess as with all things with Bun,
[2521.02 --> 2526.34]  it's making news because their benchmarks show it to be very, very fast.
[2527.18 --> 2529.32]  Now, I guess buyer beware.
[2529.76 --> 2533.78]  We've had Bun's benchmarks called into question by other people in the community,
[2533.78 --> 2537.38]  such as Ryan Dahl from Dino, who just says, just check the numbers, guys.
[2537.50 --> 2540.22]  Got to look at those numbers again and didn't say much else.
[2540.76 --> 2541.42]  So who knows?
[2542.00 --> 2543.56]  Synthetic benchmarks are what they are.
[2543.70 --> 2547.72]  But in their announcement post, Jared Sumner writes that Bun,
[2548.00 --> 2554.78]  we have a benchmark comparing 10 copies of 3.js from scratch with source maps and minification.
[2554.94 --> 2556.82]  Webpack 5 does this in 38 seconds.
[2557.48 --> 2559.54]  Rollup does it in 32.
[2559.88 --> 2561.46]  Parcel 2 in 26 seconds.
[2561.46 --> 2564.20]  R-SPAC, 4.5.
[2564.72 --> 2568.78]  ES build, pretty stinking fast, guys, 0.3 seconds.
[2568.98 --> 2572.20]  But Bun, 0.17 seconds.
[2572.54 --> 2575.24]  So this is a very fast thing.
[2575.88 --> 2576.70]  What do you guys think?
[2577.02 --> 2578.56]  Fast enough to give it a shot?
[2578.88 --> 2580.66]  Don't care because ES build is good enough?
[2581.66 --> 2584.44]  I can think of a lot of things to do with that 0.13.
[2587.62 --> 2589.90]  You can do a lot of editing things with that time.
[2589.90 --> 2591.06]  So think about that.
[2591.12 --> 2594.28]  Every time you run it, you're saving yourself 0.13 seconds.
[2594.80 --> 2600.58]  I guess I feel like I don't have the, I don't really understand Bun's pitch.
[2601.12 --> 2603.62]  Like, why do I need to switch to a new runtime?
[2604.16 --> 2607.02]  That is my question with this because I know nothing about it.
[2607.58 --> 2610.80]  Is this building it for Bun's runtime and then I can run it there?
[2610.88 --> 2615.80]  Or is this just a, I guess it's just a generic because it's building client side apps.
[2615.80 --> 2616.78]  So, right.
[2616.96 --> 2618.18]  I guess I answered my own question there.
[2618.60 --> 2618.70]  Yeah.
[2618.76 --> 2623.32]  I wouldn't imagine you need to use Bun with this because it's going to end up with a client
[2623.32 --> 2624.16]  side compile thing.
[2624.36 --> 2627.98]  I mean, if we were still using Webpack, like, yeah, that's a huge difference.
[2628.02 --> 2628.52]  That's great.
[2628.88 --> 2629.50]  But I'm not.
[2629.82 --> 2630.74]  I'm using ES build.
[2631.22 --> 2631.38]  Yeah.
[2632.12 --> 2633.06]  There you have it.
[2633.14 --> 2637.42]  I think there's other things they say is cool about it, but I didn't read the entire blog
[2637.42 --> 2637.74]  post.
[2637.82 --> 2641.02]  So let's go to the next piece of news because I'm not using Bun.
[2641.02 --> 2642.34]  So I was just like, ah, Bun Bundler.
[2642.50 --> 2642.98]  It's fast.
[2643.28 --> 2643.64]  Interesting.
[2643.82 --> 2644.34]  Let's chat.
[2644.90 --> 2651.46]  This one I did read more of and I'm actually probably more excited about, but that's baseline.
[2651.62 --> 2654.00]  Have you guys seen Mozilla's baseline now?
[2654.24 --> 2657.16]  This is a new feature on MDN.
[2658.04 --> 2664.20]  So this is like when you go to MDN and you see a particular feature such as CSS grid, you
[2664.20 --> 2665.10]  know, the grid property.
[2665.62 --> 2668.28]  And then you think to yourself, can I use, right?
[2668.28 --> 2672.90]  And then you hop over to can I use and you can see kind of the browser support.
[2673.16 --> 2676.54]  Well, they're going to build this right into the docs on Mozilla Developer Network.
[2676.66 --> 2686.38]  Now, this baseline feature where every page will have, if it's baseline supported, a nice
[2686.38 --> 2690.98]  little label and a call out right there saying like, this is a baseline feature of the web.
[2690.98 --> 2699.30]  And they define that as being it's supported across the most recent two versions of Firefox,
[2699.56 --> 2700.78]  Chrome, Edge, and Safari.
[2701.28 --> 2703.36]  So for me, this is like something I always do.
[2703.44 --> 2704.46]  It's like save a step, right?
[2704.50 --> 2708.44]  So I look at a thing like, cool, I want to use this push notification API.
[2708.78 --> 2712.18]  And then I think to myself, can I actually use it or not?
[2712.34 --> 2715.20]  And I usually hop over and check the compatibility tables and all that.
[2715.20 --> 2719.20]  But for things that are broadly supported, they're just going to throw a label on it right there.
[2720.08 --> 2725.16]  And save you a little time, maybe 0.3 seconds even before you have to go check for yourself.
[2725.50 --> 2727.54]  Don't they already have browser compat on MDN?
[2727.72 --> 2730.12]  It's on there, but it's always like a click away.
[2730.48 --> 2732.12]  This is like, bam, big old label.
[2732.18 --> 2733.14]  Why is it a click away?
[2733.28 --> 2734.40]  Like, I think it's in page.
[2734.58 --> 2735.58]  It's at the bottom of the page.
[2736.02 --> 2737.74]  I thought you had to click to a separate page.
[2738.52 --> 2738.82]  All right.
[2738.82 --> 2741.18]  Well, now it's big and green and right there in the top.
[2741.56 --> 2741.88]  Okay.
[2742.88 --> 2743.98]  You guys don't like big green labels?
[2743.98 --> 2746.20]  What page are you looking at?
[2746.50 --> 2747.48]  Well, it's still rolling out.
[2747.56 --> 2752.18]  So I'm looking at their blog post where they show the CSS grid page.
[2752.36 --> 2753.92]  And it says baseline, widely supported.
[2754.06 --> 2756.04]  It shows the browsers in which it has broad support.
[2756.70 --> 2760.60]  And it says right there next to the, it'd be like right at the top center, I believe.
[2761.26 --> 2763.52]  But all I have is the image from the blog post.
[2763.90 --> 2768.56]  I do see, so if I go to subgrid, it's on there for that.
[2768.78 --> 2770.88]  And it says baseline, not widely supported.
[2770.88 --> 2777.64]  And I actually, I do think it's kind of nice to have that front and center at the top, especially
[2777.64 --> 2780.90]  if I'm like, you know, I see that now before I'm learning about it.
[2780.96 --> 2784.84]  So if I were to come in to check out a new feature and I'm excited about it, I read about
[2784.84 --> 2785.48]  it on a blog post.
[2785.56 --> 2787.40]  I'm like, all right, I'm going to go check this out on MDM.
[2788.04 --> 2790.18]  And before, you know, I'm reading through it.
[2790.20 --> 2791.08]  I'm like, yeah, this looks cool.
[2791.10 --> 2791.64]  I'm going to try it.
[2791.70 --> 2792.20]  I'm going to try it.
[2792.26 --> 2792.48]  Okay.
[2792.48 --> 2797.00]  And then I get down to the bottom and it's like, oh, sorry, this isn't supported anywhere
[2797.00 --> 2800.12]  except Chrome or anywhere except Firefox or whatever.
[2800.34 --> 2804.60]  And I'm like, oh, well, I just spent all this time learning about it, but I can't actually
[2804.60 --> 2808.40]  use it for anything interesting because nobody supports it.
[2808.92 --> 2810.30]  And here it is right at the top.
[2810.54 --> 2814.12]  And it's, you know, you could, they could have done that by putting the compatibility grid
[2814.12 --> 2815.76]  up there, but this is, this is very tight.
[2815.90 --> 2819.48]  It doesn't take away as much, but it maybe catches me before I've gone through that investment
[2819.48 --> 2819.92]  cycle.
[2820.26 --> 2820.62]  Right.
[2820.62 --> 2821.74]  So that's cool.
[2821.90 --> 2822.46]  I like it.
[2822.70 --> 2822.90]  Yeah.
[2823.12 --> 2825.68]  And so I do see it at the top of the grid one now as well.
[2825.76 --> 2828.64]  So it looks like it has rolled out to at least some of the pages.
[2828.88 --> 2832.62]  I guess, I mean, I guess it's a new classification, right?
[2832.66 --> 2832.84]  Yep.
[2832.88 --> 2835.44]  That these are all there, but the data was always there.
[2835.50 --> 2839.50]  It seems like, cause you could just go look at the compatibility tables and they even had
[2839.50 --> 2846.92]  examples of like, if you look up with on MDN, it has a big deprecated banner on that
[2846.92 --> 2847.18]  one.
[2847.46 --> 2848.02]  Like, right.
[2848.02 --> 2849.66]  It's kind of giving you the same information.
[2850.20 --> 2850.32]  Yeah.
[2850.62 --> 2851.36]  Fair enough.
[2852.14 --> 2856.12]  Well, the compatibility table does, now I'm looking at the one where I say you always
[2856.12 --> 2859.92]  have to click away is because it just shows the most recent for every browser, right?
[2860.68 --> 2861.96]  It shows like what's currently recent.
[2862.42 --> 2863.74]  So this is different information.
[2863.90 --> 2866.96]  So you have to click through and see, like if you had some reds, right?
[2867.00 --> 2869.76]  You have to click through and see and do the whole comparison yourself.
[2869.76 --> 2871.60]  That's why I usually do the can I use.
[2871.76 --> 2877.40]  Cause if it gives you that full grid, whereas this is, they're dedicated to having it always
[2877.40 --> 2879.64]  be up to date for the most recent two versions of those.
[2879.68 --> 2884.02]  So as the browsers roll, like those baseline labels will be accurate.
[2884.02 --> 2885.14]  I don't know.
[2885.14 --> 2886.10]  Seems like a sweet feature.
[2886.18 --> 2887.20]  I was excited about it, but.
[2887.48 --> 2887.66]  Yeah.
[2888.02 --> 2888.58]  I dig it.
[2888.80 --> 2889.06]  Sorry.
[2889.16 --> 2890.54]  I didn't, I didn't cut it up guys.
[2890.74 --> 2892.16]  I'm not, I'm not that attached to it.
[2892.22 --> 2894.32]  I feel like we're just meh on both of these.
[2894.60 --> 2894.72]  Yeah.
[2894.72 --> 2897.76]  I am less meh on this than I am on the Bundler.
[2899.34 --> 2899.78]  All right.
[2899.80 --> 2900.54]  Here, I got one more.
[2900.62 --> 2901.28]  Let's try one more.
[2901.78 --> 2903.22]  See if I can get you excited about something.
[2903.92 --> 2905.84]  A new front end framework.
[2906.54 --> 2907.08]  Is it jQuery?
[2907.36 --> 2909.16]  It's called van.js.
[2909.62 --> 2909.98]  All right.
[2910.26 --> 2910.90]  It's in the doc.
[2910.96 --> 2912.22]  I'll throw it in here as well.
[2912.46 --> 2914.16]  Van stands for vanilla.
[2915.00 --> 2915.34]  Okay.
[2915.46 --> 2918.66]  So it's kind of weird because it's a vanilla JS framework, which.
[2918.66 --> 2919.18]  Oh boy.
[2919.24 --> 2922.04]  I get to write markup using JavaScript.
[2922.98 --> 2923.48]  Van.js.
[2923.48 --> 2929.44]  A 1.2 kilobyte grab and go reactive UI framework without React or JSX.
[2930.02 --> 2930.78]  1.2K.
[2931.12 --> 2932.16]  1.2K ball.
[2932.76 --> 2936.96]  It's an ultra lightweight, zero dependency, unopinionated reactive UI framework based on
[2936.96 --> 2939.24]  pure vanilla JavaScript and DOM program with van.js.
[2939.32 --> 2940.50]  Feels a lot like React.
[2940.62 --> 2942.04]  Check out the hello world code below.
[2942.90 --> 2943.80]  So van.js.
[2944.10 --> 2944.78]  Are you guys excited?
[2945.28 --> 2946.64]  Can I use JSX with it?
[2947.06 --> 2949.74]  Which, I mean, honestly, I don't.
[2950.14 --> 2951.78]  JSX I have mixed feelings about.
[2951.78 --> 2956.22]  However, ergonomically, I feel like it's closer to markup.
[2956.54 --> 2957.62]  And I like that.
[2957.94 --> 2959.14]  Like, that's a thing that I like.
[2959.20 --> 2960.42]  I like templating languages.
[2960.66 --> 2961.52]  I like HTML.
[2961.82 --> 2966.80]  I think that they are useful tools for what they do because they are kind of nice and declarative.
[2966.80 --> 2975.80]  And this, like, if I'm having to write a bunch of nested functions to generate my HTML, you've kind of lost me.
[2977.08 --> 2979.12]  Nick, van.js supports TypeScript.
[2979.34 --> 2980.30]  Are you excited about it?
[2981.66 --> 2985.26]  I'll remind you that the key word of all JS Party is excited.
[2985.50 --> 2985.72]  Excited.
[2985.72 --> 2991.46]  I was excited about this when I used it 10 years ago.
[2991.68 --> 2993.98]  And it was called Put Selector by Chris Zeip.
[2994.86 --> 2995.72]  But, oh.
[2995.88 --> 2996.76]  Sick burn.
[2997.00 --> 2997.58]  Sick burn.
[2998.14 --> 3003.86]  Apologies to the Bun team, the Mozilla Developer Network team, and the van.js team.
[3003.86 --> 3007.82]  Okay, so let me highlight something I am excited about with this.
[3008.28 --> 3008.56]  Okay.
[3008.88 --> 3014.04]  Which is, I am really excited to see more and more experimentation in this.
[3014.20 --> 3021.26]  How do we get developer ergonomics and reactive programming and, like, this declarative and compositional way of thinking about UI components
[3021.26 --> 3028.56]  that has shown to be super productive without massive amounts of JavaScript shipping to and running on client devices?
[3029.08 --> 3036.82]  Like, that is, in my mind, the big problem that we are trying to solve in the front-end space.
[3036.94 --> 3038.88]  And they are doing that here in van.js.
[3039.24 --> 3042.52]  Now, do I think they've solved the developer ergonomics problem looking at this?
[3042.82 --> 3045.14]  It does not look like great ergonomics to me.
[3046.04 --> 3048.70]  However, ergonomics are something that vary by person.
[3048.70 --> 3052.66]  And just because they're not there today doesn't mean they won't be there.
[3053.08 --> 3058.58]  And I want to see, I'm really excited to see more experimentation in that space.
[3058.58 --> 3065.84]  Because I think that is, right now, the sort of seat of discontent in the front-end world.
[3066.38 --> 3070.06]  And we're seeing an explosion of people trying to address it, right?
[3070.12 --> 3071.60]  I think Quick is doing this.
[3071.68 --> 3072.44]  Astro is doing this.
[3072.52 --> 3073.38]  Svelte is doing this.
[3073.78 --> 3075.14]  Now Van is doing this.
[3075.78 --> 3076.20]  I missed one.
[3076.28 --> 3077.16]  Solid is doing this.
[3077.16 --> 3081.16]  Like, everybody's trying to solve this problem of how do we maintain these really nice developer
[3081.16 --> 3088.66]  and productive developer ergonomics while not bogging down our networks and our client devices
[3088.66 --> 3090.68]  with tons and tons of JavaScript.
[3091.10 --> 3094.34]  And so, you know, seeing more takes on that is great.
[3094.78 --> 3095.00]  I agree.
[3095.40 --> 3100.62]  And this is cool in that it's using a syntax that is familiar.
[3100.62 --> 3104.08]  And it's not augmenting the language like JSX does.
[3104.62 --> 3111.18]  And it's not adding in these esoteric, weird things that are really hard to understand with template literals.
[3111.52 --> 3116.02]  It's just straight function calls and nested further function calls, which is really cool.
[3116.28 --> 3117.48]  Because it's so straightforward.
[3117.48 --> 3119.84]  Yeah, you want a paragraph, you got a function called P.
[3120.12 --> 3123.04]  You want a list item, you got a function called LI.
[3123.84 --> 3128.24]  And you nest those suckers, call some sort of deal on them, and bam.
[3128.74 --> 3129.54]  Ban.add.
[3129.78 --> 3130.58]  Document.body.
[3130.66 --> 3130.88]  Hello.
[3131.80 --> 3133.00]  Oh, cool idea.
[3133.10 --> 3134.28]  1.2 kilobytes.
[3134.58 --> 3135.50]  I'll remind you.
[3135.62 --> 3136.98]  And TypeScript support.
[3137.08 --> 3137.74]  Look at me over here.
[3137.84 --> 3138.42]  It's on TypeScript.
[3139.30 --> 3140.54]  It has a potential feature.
[3140.66 --> 3142.00]  That's like table stakes at this point.
[3142.38 --> 3142.98]  Is it, though?
[3143.14 --> 3143.38]  Mm-hmm.
[3143.38 --> 3144.58]  I'm with Nick on this.
[3144.78 --> 3145.34]  Jared, sorry.
[3145.74 --> 3147.08]  You're not up to the table yet.
[3147.32 --> 3148.56]  I'm sitting at a different table.
[3148.80 --> 3152.58]  If someone tells me they write JavaScript all day, I assume that they meant TypeScript.
[3153.00 --> 3153.86]  You're probably right.
[3155.28 --> 3157.86]  But pretty soon, there'll be a backlash.
[3158.32 --> 3162.38]  That's because the type, types as comments, whatever it's called, is coming.
[3162.68 --> 3164.08]  Yeah, JSDoc is coming back.
[3164.32 --> 3164.48]  See?
[3164.60 --> 3164.86]  Okay.
[3165.18 --> 3166.44]  Svelte is going away from it.
[3166.72 --> 3168.38]  There's a worthwhile rant.
[3168.96 --> 3169.72]  All right, go for it.
[3169.72 --> 3173.38]  Why would you want to write JSDoc comments over TypeScript?
[3173.70 --> 3175.42]  I just can't put my head around that.
[3176.10 --> 3180.78]  What is so wrong with a compile step that you don't see 99% of the time or care about
[3180.78 --> 3185.22]  that you would rather write comments and have all of this boilerplate above the code
[3185.22 --> 3190.28]  to facilitate the code when you could just have it all in line so that as you're reading
[3190.28 --> 3192.14]  and you're scanning with your eyes, it's there.
[3192.62 --> 3193.30]  I don't understand.
[3193.82 --> 3195.84]  Yeah, I'd rather not do either one of those things personally.
[3196.38 --> 3199.22]  But I don't know.
[3199.22 --> 3202.72]  I think Rich Harris tends to know why he makes certain decisions.
[3202.90 --> 3207.84]  I haven't heard his reasoning, but I did hear the headline of Svelte switching away
[3207.84 --> 3209.20]  from TypeScript for JSDoc.
[3209.54 --> 3210.56]  Oh, is that where this came from?
[3210.90 --> 3211.24]  Yes.
[3212.26 --> 3213.06]  I'm out of the loop.
[3213.08 --> 3213.88]  Maybe he'll tell you why.
[3213.96 --> 3214.60]  Go look that up.
[3214.66 --> 3217.08]  He'll probably tell you why your rant was silliness.
[3217.22 --> 3218.02]  I have no idea, though.
[3218.46 --> 3223.58]  Well, so one thing that Svelte is doing is that they are mucking around with a compile
[3223.58 --> 3228.40]  step themselves and doing other interesting parsing things and other stuff.
[3228.40 --> 3235.24]  And it may be that it's easier to do the kinds of additional magic they want to do and integrate
[3235.24 --> 3240.82]  it cleanly with TypeScript if the type information is in comments rather than having to deal with
[3240.82 --> 3241.98]  the syntactic piece.
[3242.46 --> 3244.04]  So I don't know either.
[3244.04 --> 3246.72]  I have not seen the rationalization here, but let's...
[3246.72 --> 3248.12]  Let me pull in a quote from Rich Harris.
[3248.30 --> 3249.72]  Here's the pull quote.
[3249.84 --> 3250.88]  It's probably not his entire stance.
[3250.98 --> 3252.92]  My position is types are fantastic.
[3253.60 --> 3254.86]  TypeScript is a bit of a pain.
[3255.50 --> 3259.64]  As soon as you use a .ts file, then you have to have the tooling to support that.
[3259.92 --> 3263.56]  There's all these points of friction when you use a non-savion language like TypeScript
[3263.56 --> 3265.56]  that I have come to believe makes it not worth it.
[3265.56 --> 3270.38]  So instead, we have put all our types in JS doc annotations and we get all the type safety,
[3270.64 --> 3272.76]  but none of the drawbacks because it is JavaScript.
[3273.34 --> 3274.22]  Everything's in comments.
[3274.44 --> 3275.32]  You can just run the code.
[3275.66 --> 3280.48]  This is what we do in the SvelteKit code base and has worked out fantastically for Svelte 4.
[3280.74 --> 3284.34]  We're going to do the same for Svelte because it's going to enable us to move much more
[3284.34 --> 3284.92]  quickly.
[3285.16 --> 3288.56]  So actually, Nick, that doesn't seem to address your particular stance.
[3288.86 --> 3290.48]  He just doesn't like it.
[3290.84 --> 3292.22]  He'd rather write the JS doc comments.
[3292.22 --> 3296.04]  I feel like it's a pretty strong assertion that TypeScript is a non-standard language.
[3296.62 --> 3297.50]  What browser does it run in?
[3298.16 --> 3303.34]  Who made browsers the sort of standard of what's a standard language, right?
[3303.46 --> 3305.22]  Like what JavaScript is?
[3305.72 --> 3307.40]  We're not talking JavaScript, right?
[3307.44 --> 3309.88]  I can compile Rust to run in the browser.
[3310.02 --> 3312.02]  I can compile TypeScript to run in the browser.
[3312.16 --> 3316.36]  I can compile a variety of other languages to run in the browser.
[3316.56 --> 3318.32]  You have to compile Svelte to run in the browser.
[3318.46 --> 3320.14]  I can compile Svelte to run in the browser.
[3320.14 --> 3325.82]  But the fact that there's a compile step involved doesn't, to me, say anything at all.
[3326.02 --> 3329.14]  That's orthogonal to standardization or what's standard.
[3329.94 --> 3335.92]  They also are doing the due diligence because I think if they were to just be like, we are
[3335.92 --> 3340.26]  dropping types and we don't care and they're not generating types, well, third-party types
[3340.26 --> 3343.20]  would come up on definitely typed the next day.
[3343.74 --> 3345.04]  But that would hurt them.
[3345.04 --> 3347.56]  They're supporting full TypeScript still, I would assume.
[3348.12 --> 3350.92]  And so I don't think that because...
[3350.92 --> 3352.66]  But they're writing documentation.
[3353.56 --> 3356.82]  And that's not saying that every library author should write documentation, right?
[3356.96 --> 3360.00]  But they're still shipping types so that you can use TypeScript when you use Svelte.
[3360.10 --> 3360.34]  Yeah.
[3360.88 --> 3363.62]  So they're not advocating for you to not use TypeScript.
[3363.90 --> 3364.22]  No.
[3364.60 --> 3365.22]  Neither am I.
[3365.46 --> 3367.30]  I'm just advocating for me not to use TypeScript.
[3368.02 --> 3368.58]  That's different.
[3368.58 --> 3370.84]  Well, and there is an interesting question there, right?
[3370.92 --> 3373.76]  Of like, here, we have these guardrails we can put in place for you.
[3374.14 --> 3376.56]  Do we ship things in a way that you have to use them?
[3377.54 --> 3378.50]  That's a choice, right?
[3379.00 --> 3379.54]  It is.
[3380.32 --> 3380.58]  Yeah.
[3381.18 --> 3385.86]  And I think it's, you know, there are likely to be strong opinions on both sides.
[3386.06 --> 3386.40]  Oh, yeah.
[3386.48 --> 3386.78]  Right.
[3387.38 --> 3390.22]  Which is why I would not force it if it was me.
[3390.66 --> 3392.24]  I wouldn't take that stance myself.
[3392.24 --> 3394.60]  But I could see why somebody might.
[3394.74 --> 3399.98]  And maybe that their library would get popular because it does enforce, require you to use TypeScript, for instance.
[3400.32 --> 3401.78]  Well, there's plenty that do that, right?
[3401.88 --> 3403.00]  Angular, for example.
[3403.72 --> 3403.96]  Yeah.
[3404.44 --> 3405.44]  But they're not getting my business.
[3405.62 --> 3413.50]  I mean, I think there's an argument to be said, which is, you know, if you use types, we know that a certain class of problems won't happen.
[3413.80 --> 3416.70]  And we know that you're not, therefore, going to blame those problems on us.
[3416.70 --> 3424.34]  Because if we ship a library in a way that you don't have to use types, and you use something, and it errors down in our code because you passed it something that was type illegal.
[3424.72 --> 3424.84]  Sure.
[3425.14 --> 3428.26]  I know that's not my bug, but you're going to file it on my GitHub anyway.
[3428.94 --> 3433.96]  Yeah, but that's like the cat in the hat, you know, where they take the streak and they rub it on something else and it moves to that thing.
[3434.54 --> 3437.10]  You just shift what you're going to complain about.
[3437.22 --> 3439.96]  Like, people are still going to blame bugs on you that aren't yours.
[3440.64 --> 3441.70]  They're just going to be different.
[3442.44 --> 3444.58]  So, I don't know if that necessarily reduces support.
[3444.58 --> 3445.24]  Maybe it does.
[3445.24 --> 3449.24]  We have to have a longitudinal study on such things.
[3449.78 --> 3451.78]  This would be bigger news if they weren't shipping types still.
[3451.90 --> 3454.22]  But they're shipping types, so it doesn't matter.
[3454.30 --> 3454.64]  Oh, yes.
[3454.68 --> 3455.70]  I didn't mean to imply that.
[3455.84 --> 3456.96]  I knew they were shipping types still.
[3457.48 --> 3459.16]  I say they switched to JS Doc, was what I was saying.
[3459.30 --> 3459.46]  Yeah.
[3459.86 --> 3460.68]  Bone School would be happy.
[3461.68 --> 3462.24]  That's true.
[3462.78 --> 3463.16]  And Jared.
[3463.22 --> 3463.58]  For sure.
[3464.08 --> 3465.04]  I am happy about it.
[3465.12 --> 3471.56]  I just like to say, I just know that every, with every action causes an equal, and I can't even say the phrase.
[3472.08 --> 3473.50]  It's late on Friday, guys.
[3473.80 --> 3474.58]  Let's end this show.
[3474.58 --> 3477.00]  You made Jared smile, and you made Nick frown.
[3477.48 --> 3478.56]  Equal and opposite.
[3478.86 --> 3479.38]  There you go.
[3479.72 --> 3481.18]  Every lash has a backlash.
[3481.68 --> 3481.92]  Okay?
[3482.38 --> 3483.58]  And TypeScript will have its day.
[3483.98 --> 3484.98]  And I'll be here waiting.
[3485.26 --> 3485.88]  Mwahaha.
[3485.88 --> 3488.72]  I'll have a whiplash.
[3489.28 --> 3491.86]  That's the final word from Nick Neesey.
[3492.20 --> 3494.52]  About as good as his opening remarks as well.
[3495.20 --> 3496.54]  Let's call it a show.
[3496.86 --> 3503.48]  Listener, if you're more excited about the things that I read off in the news section than these guys are, the links are in the show notes for you.
[3503.48 --> 3507.64]  If you want to check out the class Variance Authority, it's also in the show notes.
[3507.64 --> 3509.94]  All right, that's JS Party.
[3510.06 --> 3512.92]  I got to play this outro music because we are ready to dance it out.
[3512.92 --> 3524.08]  That is our show for this week.
[3524.30 --> 3525.50]  Thanks for partying with us.
[3525.50 --> 3527.56]  What do you think about CBA?
[3528.10 --> 3529.14]  Or K-Ball's new stack?
[3529.46 --> 3530.44]  Or Bun's new bundler?
[3530.80 --> 3532.82]  Or TypeScript versus JS Doc?
[3533.18 --> 3534.88]  Let us know in the comments.
[3535.32 --> 3536.90]  There's a link in your show notes.
[3537.48 --> 3540.22]  Or you can also tweet at JS Party FM.
[3540.74 --> 3543.68]  Or toot at JS Party at changelog.social.
[3543.92 --> 3545.32]  You did not just say that.
[3545.52 --> 3546.64]  I didn't want to say that, Emma.
[3546.90 --> 3548.40]  But the Fediverse made me do it.
[3549.40 --> 3555.06]  Next up on the pod, K-Ball digs through Nick's toolbox to see what all he has in there.
[3555.50 --> 3558.82]  We know he loves TypeScript and Vim, but is there room for anything else?
[3559.46 --> 3561.02]  Subscribe now so you don't miss it.
[3561.32 --> 3564.08]  Head to jsparty.fm for all the ways.
[3565.10 --> 3571.22]  Thanks once again to our partners Fastly and Fly for helping us bring you awesome pods each and every week.
[3571.34 --> 3578.26]  And to our mysterious friend, Brigmaster Cylinder, who bumps out the best beats in the biz on a continual basis.
[3578.98 --> 3579.82]  That's all for now.
[3580.22 --> 3581.90]  We'll talk to you again next week.
