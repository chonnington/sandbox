
/*

<xsl:template match="li[@class='selected']/p"> <fo:block background-color="blue">
            <xsl:apply-templates/>
        </fo:block>
    </xsl:template>

*/



var liElements = document.getElementsByTagName("li"); for (var i = 0; i < liElements.length; i++) {
    if (liElements[i].className === "selected") { var children = liElements[i].childNodes; for (var j = 0; j < children.length; j++) {
    var child = children[j];
    if (child.nodeType === Node.ELEMENT_NODE && child.tagName === "P") {
                        child.setAttribute("style", "background-color: blue");
                    }
    } }
    }

