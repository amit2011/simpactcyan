#!/usr/bin/env python

import subprocess
import platform
import sys

if __name__ == "__main__":

    style = '''
body {
   font-family: Helvetica, arial, sans-serif;
   font-size: 14px;
   line-height: 1.6;
   padding-top: 10px;
   padding-bottom: 10px;
   background-color: white;
   text-align: justify;
   padding: 30px; }

body > *:first-child {
   margin-top: 0 !important; }
body > *:last-child {
   margin-bottom: 0 !important; }

a {
   color: #4183C4; }
a.absent {
   color: #cc0000; }
a.anchor {
   display: block;
   padding-left: 30px;
   margin-left: -30px;
   cursor: pointer;
   position: absolute;
   top: 0;
   left: 0;
   bottom: 0; }

h1, h2, h3, h4, h5, h6 {
   margin: 20px 0 10px;
   padding: 0;
   font-weight: bold;
   -webkit-font-smoothing: antialiased;
   cursor: text;
   position: relative; }

h1:hover a.anchor, h2:hover a.anchor, h3:hover a.anchor, h4:hover a.anchor, h5:hover a.anchor, h6:hover a.anchor {
   text-decoration: none; }

h1 tt, h1 code {
   font-size: inherit; }

h2 tt, h2 code {
   font-size: inherit; }

h3 tt, h3 code {
   font-size: inherit; }

h4 tt, h4 code {
   font-size: inherit; }

h5 tt, h5 code {
   font-size: inherit; }

h6 tt, h6 code {
   font-size: inherit; }

h1 {
   font-size: 28px;
   color: black; }

h2 {
   font-size: 24px;
   border-bottom: 1px solid #cccccc;
   color: black; }

h3 {
   font-size: 18px; }

h4 {
   font-size: 16px; }

h5 {
   font-size: 14px; }

h6 {
   color: #777777;
   font-size: 14px; }

p, blockquote, ul, ol, dl, li, table, pre {
   margin: 15px 0; }

hr {
   border: 0 none;
   color: #cccccc;
   height: 4px;
   padding: 0;
}

body > h2:first-child {
   margin-top: 0;
   padding-top: 0; }
body > h1:first-child {
   margin-top: 0;
   padding-top: 0; }
body > h1:first-child + h2 {
   margin-top: 0;
   padding-top: 0; }
body > h3:first-child, body > h4:first-child, body > h5:first-child, body > h6:first-child {
   margin-top: 0;
   padding-top: 0; }

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
   margin-top: 0;
   padding-top: 0; }

h1 p, h2 p, h3 p, h4 p, h5 p, h6 p {
   margin-top: 0; }

li p.first {
   display: inline-block; }
li {
   margin: 0; }
ul, ol {
   padding-left: 30px; }

ul :first-child, ol :first-child {
   margin-top: 0; }

dl {
   padding: 0; }
dl dt {
   font-size: 14px;
   font-weight: bold;
   font-style: italic;
   padding: 0;
   margin: 15px 0 5px; }
dl dt:first-child {
   padding: 0; }
dl dt > :first-child {
   margin-top: 0; }
dl dt > :last-child {
   margin-bottom: 0; }
dl dd {
   margin: 0 0 15px;
   padding: 0 15px; }
dl dd > :first-child {
   margin-top: 0; }
dl dd > :last-child {
   margin-bottom: 0; }

blockquote {
   border-left: 4px solid #dddddd;
   padding: 0 15px;
   color: #777777; }
blockquote > :first-child {
   margin-top: 0; }
blockquote > :last-child {
   margin-bottom: 0; }

table {
   padding: 0;border-collapse: collapse; }
table tr {
   border-top: 1px solid #cccccc;
   background-color: white;
   margin: 0;
   padding: 0; }
table tr:nth-child(2n) {
   background-color: #f8f8f8; }
table tr th {
   font-weight: bold;
   border: 1px solid #cccccc;
   margin: 0;
   padding: 6px 13px; }
table tr td {
   border: 1px solid #cccccc;
   margin: 0;
   padding: 6px 13px; }
table tr th :first-child, table tr td :first-child {
   margin-top: 0; }
table tr th :last-child, table tr td :last-child {
   margin-bottom: 0; }

img {
   max-width: 100%; }

span.frame {
   display: block;
   overflow: hidden; }
span.frame > span {
   border: 1px solid #dddddd;
   display: block;
   float: left;
   overflow: hidden;
   margin: 13px 0 0;
   padding: 7px;
   width: auto; }
span.frame span img {
   display: block;
   float: left; }
span.frame span span {
   clear: both;
   color: #333333;
   display: block;
   padding: 5px 0 0; }
span.align-center {
   display: block;
   overflow: hidden;
   clear: both; }
span.align-center > span {
   display: block;
   overflow: hidden;
   margin: 13px auto 0;
   text-align: center; }
span.align-center span img {
   margin: 0 auto;
   text-align: center; }
span.align-right {
   display: block;
   overflow: hidden;
   clear: both; }
span.align-right > span {
   display: block;
   overflow: hidden;
   margin: 13px 0 0;
   text-align: right; }
span.align-right span img {
   margin: 0;
   text-align: right; }
span.float-left {
   display: block;
   margin-right: 13px;
   overflow: hidden;
   float: left; }
span.float-left span {
   margin: 13px 0 0; }
span.float-right {
   display: block;
   margin-left: 13px;
   overflow: hidden;
   float: right; }
span.float-right > span {
   display: block;
   overflow: hidden;
   margin: 13px auto 0;
   text-align: right; }

code, tt {
   margin: 0 2px;
   padding: 0 5px;
   white-space: nowrap;
   border: 1px solid #eaeaea;
   background-color: #f8f8f8;
   border-radius: 3px; }

pre code {
   margin: 0;
   padding: 0;
   white-space: pre;
   border: none;
   background: transparent; }

.highlight pre {
   background-color: #f8f8f8;
   border: 1px solid #cccccc;
   font-size: 13px;
   line-height: 19px;
   overflow: auto;
   padding: 6px 10px;
   border-radius: 3px; }

pre {
   background-color: #f8f8f8;
   border: 1px solid #cccccc;
   font-size: 13px;
   line-height: 19px;
   overflow: auto;
   padding: 6px 10px;
   border-radius: 3px; }
pre code, pre tt {
   background-color: transparent;
   border: none; }

sup {
   font-size: 0.83em;
   vertical-align: super;
   line-height: 0;
}
* {
	 -webkit-print-color-adjust: exact;
}
@media screen and (min-width: 914px) {
   body {
      width: 854px;
      margin:0 auto;
   }
}
@media print {
	 table, pre {
		  page-break-inside: avoid;
	 }
	 pre {
		  word-wrap: break-word;
	 }
}
'''

    style += '''
body {
        counter-reset: section;
}

h2 {
        counter-increment: section;
        counter-reset: subsection;
}

h3 {
        counter-increment: subsection;
        counter-reset: subsubsection;
}

h4 {
        counter-increment: subsubsection;
}

h2:before {
        content: counter(section) ". ";
}

h3:before {
        content: counter(section) "." counter(subsection) " ";
}

h4:before {
        content: counter(section) "." counter(subsection) "." counter(subsubsection) " ";
}

img {
    display: block;
    margin-left:auto;
    margin-right:auto;
}
'''

    style += '''
        #tocdiv {
            position: fixed;
            top: 0px;
            right: 0px;
            width: 50%;
            height: 100%;
            overflow-y: scroll;
            white-space:nowrap;
            z-index: 1;
            background-color: white; 
            border-width: 1px;
            border-style: solid;
            padding: 5px;
        }

        .showhidetocdiv {
            position: fixed;
            top: 0px;
            left: 0px;
            background-color: white; 
            border-width: 1px;
            z-index: 2;
            cursor: pointer;
            border-style: solid;
            margin: 5px;
            padding: 5px;
        }

        @media print
        {    
            .no-print, .no-print *
            {
                    display: none !important;
            }
        }
'''

    header = '''
<div id="initdiv">
Loading documentation...
</div>
<div id="fulldiv" style="display:none;">
    <div class="showhidetocdiv no-print">Show/hide contents</div>
    <div id="tocdiv" class="no-print" style="display:none;">
        <p><strong>Table of contents</strong></p>
    </div>
    <div id="documentation">
'''
    footer = '''
    </div>
</div> <!-- end of "fulldiv" -->
<script>
    function endsWith(s, end, caseInsensitive)
    {
        if (typeof s != "string")
            return false;

        var l = s.length;

        if (l < end.length)
            return false;

        var startIdx = l-end.length;

        if (caseInsensitive)
        {
            if (s.substr(startIdx).toLowerCase() == end.toLowerCase())
                return true;
        }
        else
        {
            if (s.substr(startIdx) == end)
                return true;
        }

        return false;
    }

    (function()
    { 
        var as = document.getElementsByTagName("a");
        var parts = document.location.pathname.split("/")
        parts.splice(-1,1); // remove last element
        var ipythonViewerPrefix = "http://nbviewer.ipython.org/url"

        for (var i = 0 ; i < as.length ; i++)
        {
            var a = as[i];
            var href = a.getAttribute("href");
            if (href)
            {
                if (href.length > 0 && href[0] != '#')
                    a.setAttribute("target", "_blank");

                if (endsWith(href, ".ipynb", true))
                {
                    var newParts = parts.slice();
                    newParts.push(href);
                    var fullUrl = ipythonViewerPrefix + "/" + document.location.hostname + newParts.join("/");
                    a.setAttribute("href", fullUrl);
                }
            }
        }
    })();

    (function()
    {
        var counters = [0, 0, 0];
        var increaseCounter = function(headerLevel)
        {
            var idx = headerLevel-2;
            counters[idx]++;
            for (var i = idx+1 ; i < counters.length ; i++)
                counters[i] = 0;
        }

        var getCounterString = function()
        {
            var idx = 0;
            var s = "";

            while (idx < counters.length && counters[idx] != 0)
            {
                s += "" + counters[idx] + ".";
                idx++;
            }
            return s;
        }

        var headers = $("h2, h3, h4");
        
        for (var i = 0 ; i < headers.length ; i++)
        {
            var h = headers[i];
            var headerLevel = parseInt($(h).prop("tagName")[1]);
            increaseCounter(headerLevel);
            var counterString = getCounterString();

            var id = "tocanchor_" + counterString.split(".").join("_");

            var a = $("<a>", { "name": id });
            $(h).before(a);

            a = $("<a>", { "href": "#" + id });
            a.text(counterString + " " + $(h).text());

            var span = $("<span>");
            var s = "";

            for (var j = 0 ; j < counterString.length ; j++)
            {
                if (counterString[j] == ".")
                    s += "&nbsp;&nbsp;&nbsp;";
            }
            span.html(s);

            $("#tocdiv").append(span);
            $("#tocdiv").append(a);
            $("#tocdiv").append($("<br>"));
        }
        $("#tocdiv").append($("<br>"));

    })();

    function toggleToc()
    {
        var elem = $("#tocdiv");
        if (elem.is(":visible"))
          elem.hide();
        else
          elem.show();
    }

    $(".showhidetocdiv").click(toggleToc);
    $(document).keyup(function(e) 
    {
         if (e.keyCode == 27) 
            $("#tocdiv").hide();
    });

    MathJax.Hub.Register.StartupHook("End",function () 
    {
        document.getElementById("initdiv").style.display = "none";
        document.getElementById("fulldiv").style.display = "";

        if (document.location.hash.length == 0)
        {
            if ("state" in sessionStorage)
            {
                var state = JSON.parse(sessionStorage["state"]);
                $("body").scrollTop(state["scrollBody"]);
                $("html").scrollTop(state["scrollHtml"]);
            }
        }
    });

    setInterval(function()
    {
        if (document.getElementById("initdiv").style.display == "none")
        {
            var state = { };
            state["scrollBody"] = $("body").scrollTop();
            state["scrollHtml"] = $("html").scrollTop();
            sessionStorage["state"] = JSON.stringify(state);
        }
    }, 1000);
</script>
'''

    pandoc = "pandoc"
    if platform.system() == "Darwin":
        pandoc = "/Applications/RStudio.app/Contents/MacOS/pandoc/pandoc"

    output = subprocess.check_output([ pandoc, "--from", "markdown", "--to", "html", "--mathjax=http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" , "-s" ] + sys.argv[1:])
    output = output.replace("</head>", "<style>\n" + style + "</style><script src='http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script></script></head>")
    output = output.replace("<body>", "<body>" + header + "\n")
    output = output.replace("</body>", footer + "\n</body>")
    sys.stdout.write(output)

