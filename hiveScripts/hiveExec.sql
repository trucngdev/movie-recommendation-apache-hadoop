use recomsys;

SELECT a.uid, a.itemid, b.itemtitle 
FROM content a JOIN items b
ON (a.itemid=b.itemid) and (a.uid=${uid});


