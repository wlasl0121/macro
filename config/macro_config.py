#좌석 선택 영역
#A(ax,ay)와 B(bx,by) 좌표 구한 후 (ax, ay, bx-ax, by-ay)
SEARCH_REGION_ax = 558
SEARCH_REGION_ay = 341
SEARCH_REGION_bx = 1252
SEARCH_REGION_by = 991
SEARCH_REGION = (SEARCH_REGION_ax, SEARCH_REGION_ay, SEARCH_REGION_bx-SEARCH_REGION_ax, SEARCH_REGION_by-SEARCH_REGION_ay)
#좌석 새로고침하는 버튼 영역
REFRESH_REGION_ax = 785
REFRESH_REGION_ay = 708
REFRESH_REGION_bx = 889
REFRESH_REGION_by = 727
REFRESH_REGION = (REFRESH_REGION_ax, REFRESH_REGION_ay, REFRESH_REGION_bx-REFRESH_REGION_ax, REFRESH_REGION_by-REFRESH_REGION_ay)
# 다음단계 버튼 좌표
CLICK_DESTINATION = (845, 636)
# 티켓 버튼 좌표
CLICK_TICKET = (724, 333)
# CLICK_TICKET = (762, 308) #test

# 티켓 타겟 색깔 
# TARGET_COLOR = (159,212,39) #테이블석(2인)
TARGET_COLOR = (68,125,168) #1루 일반석
# TARGET_COLOR = (123,104,238) # 포도알색깔 #TEST용도

# 예매 url
RESERVATION_URL = "https://tickets.interpark.com/special/sports/promotion?seq=27"



# public으로 해도 될 정보들과 private 으로 바꿔야할 정보를 다른 설정 파일을 만들 예정
# ini, json ... ?
# private_config.json / private_config.ini / ...