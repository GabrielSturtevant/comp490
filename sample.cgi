#!/bin/bash
echo "Content-type: text/html"
echo ""

echo "<html><head>"
echo "<link rel=\"stylesheet\" href=\"stylesheet.css\" type=\"text/css\">"
echo "<title>Project</title></head>"
echo "<body>"
echo "<h1 class="foo">Hello World</h1>"
echo "<!----!>"
if [ -n "${QUERY_STRING}" ] ; then
	/usr/bin/curl -s ${QUERY_STRING}
fi
echo "</body></html>"
