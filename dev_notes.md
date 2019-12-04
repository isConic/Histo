Thoughts:
 
Pagination: 

- places API returns a next page token. 
- Looks like this 
```json
"next_page_token":"CsQCPQEAANhw9qMf9DXMlfAOI6bxnbk6sqcU7rC_JxK97ft5d_-PDYI4lq7YkaehZRggxSNi--zTZlqHoHeD7pLOgaPOads_nUeE2Vu_S0UGrsTOM_6Ku3gA4H8CUbldxUt6Cttr-EgSj0jX87WXY3KE-qh12p_Th7SVLO5k837f9sl02R_CxXWsgeVfRXLF5OF864iOLN-hw7aHbwW4mUbmJBDUOY8MQWHm-O3lOKLcOWWQ_lvHrTyGb_2P2nF2QBllT9cWsJ_C2dWVtVwKy20sVaK54HDIlCr1EjeAEaWohmULBkTjkSVuHBuOnq71X9ZCr1tLTSfaLtP_F4w_D4KqIepjBHgy-Qg8Q8Sj6SMY1w9I6GbODxcB6mfW3S-Qp_6hltvCQjI3XCoRxtk11JM6yo777H6sxglz_Hc46zjBZbv90gVOEhDi0vOihhRXX-U3tOYRdkuaGhR1Z_50Nl7B3i4g_7BrebuQKkEskA"
```


Single points:

- When I search `Verdun, Montreal` I get a "boundaries" section in my geojson response. This makes sense. Verdun 
is a district in Montreal. It spans an area. This spanning area is used to calculate zoom levels. 

- When I search `Guy-Concordia, Montreal` this same boundaries section does not exist. This means that zoom level does not have 
a spanning area. Spanning area should be predetermined or modifiable using a slider. 
   - distance as a function of walking time threshold. 
   
   

