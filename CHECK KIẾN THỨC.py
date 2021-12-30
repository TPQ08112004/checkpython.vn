print('### kiểm tra của biến a ###')  # BÀI 1 TỚI 11
a = "quý"
print(a)
print('VÍ DỤ VỀ DỮ LIỆU CỦA BIẾN')
# kiểm tra dữ liệu của biến b
b = "sinh năm 2004"
# kiểm tra dữ liệu của biến c
c = 123456789.1
print(type(a))
print(type(b))
print(type(c))
u = "hahaha"
print(u)
print('xin chào ')
aa = 'a        a '
print(aa)

print('### CÁC VÍ DỤ VỀ CHUỖI ###')
# """đây là các chuỗi được điền vô ko gián đoạn
a = """thập 
phú 
quý xin chào 
mọi người"""
# đây cũng là chuỗi nhưng mà nối tiếp nhau
b = '''bây giờ chúng ta cùng học python thôi nào'''
print(a, b)

# sự khác nhau giữa '' và "  nếu 'a"b"(báo lỗi) còn nếu "a'b"(ct mới đúng) a,b:dữ liệu py
b = 'end"và'
print(b)
# nội dung có chứa 2 cặp '' và ""
A = 'ninh thuận   "85" "quê tôi" nhá nhá '
print(A)
# chuỗi nhiều dòng
s = '''  chuỗi 1
      chuỗi 2
      chuỗi 3'''
print(s)
v = '''dong1
dong2 
dong3'''
print(v)
# chuỗi vừa có kí tự và vừa có chuỗi kí tự
h = '''chuoi vua co ki tu "vua có ki tu", oi that la vi dieu"'''
l = """chuỗi vừa có kí tự '''vừa có kí tự'''''' ,'thật là vi diệu' nhỉ"""
print(h)
print(l)

# định dang bằng toán tử %
a = 'thapphuquy xin %s các em yêu dấu nhé' % (
    'chào')  # nó print my name is thapphuquy do nó thay %s BẰNG %('thapphuquy')
# và %s CÓ THỂ THAY THẾ các %s khác như %d,v,b,n,m,m,......thành %('giá trị N lần ,,,,) như ví dụ trên ấy
print(a)
a1 = 'thapphuquy xin %s %s các em yêu dấu nhé' % ('chào', 'chào lần 2')  # nếu xóa đi 1 %s thì chương trình báo lỗi
# kq sẽ báo lỗi .Nếu muốn đúng thêm 1 chuỗi chỗ %('chào,'giá trị chuỗi')
# bên đây(%s%s)có bên kia bấy nhiêu (=)  ('chuỗi 1','chuỗi 2') COI KĨ VÍ DỤ TRÊN RỒI SẼ HIỂU THÔI
print(a1)
b = '%s %s'
print(b % ('2', '2'))
# một số ví dụ thú vị
b1 = '%.2f' % (3.456)  # kq sẽ là 3.46 vì nó chỉ lấy 2 số thập phân sau cùng biến b1 và nó làm tròn
print(b1)
b2 = "%.5f" % (23.09654321)  # kq là 23.09654 giải thích tương tự như biến b1 thôi
print(b2)
f = '%.f' % (3.59999)  # kq 4 sẽ tự làm tròn <5 đi xuống và >5 đi lên
print(f)
# ví dụ về một f-string
f1 = f'abc'
print(f1)
# ví dụ nâng caao f-string
print(f'a\tb')

# ví dụ về result
t = 'thapphuquy'
p = '08/11/2004'
q = 'văn lâm'
result = f'tên:{t}\nnăm sinh:{p}\nđịa chỉ:{q}'
print(result)
# định dạng bằng phương thức format
t1 = '''a:{},b{},c{}'''.format(1, 2, 3)
print(t1)
t2 = 'a:%d,b:%d,c:%d' % (1, 2, 3)  # tương tự như dùng phương thức format bài trước thôi
print(t2)
t3 = '1:{one};2:{two}'.format(one=111, two=222)
print(t3)

print('###ví dụ về chuỗi trần ###')
print('xin chào,\\tất cả mọi người ')
a = r'\neu mot ngay'
print(a)
s = 'tqp'
s += "thập phú quý"
print(s)
s1 = ',tpq'
s2 = s + s1
print(s2)
# ý là tạo ra chuỗi bằng cách lặp lại chuỗi 'a' 10 lần
b = "a" * 10
print(b)
# ví dụ thêm vê chuỗi
c = 'abcd  '
c *= 10
print(c)
c *= 0
# tất cả các chuỗi nhân với số 0 đều bằng ''
h = 'abcdef' * 0
print(h)
print(c)
# kiểu dữu liệu boolean
ss = 'thapphuquy' in 'tpq'  # kết quả sẽ false vì chuỗi'thapphuquy'không có TRONG chuỗi'tpq'
print(ss)

sss = "ninhthuan" in "ninhthuan85"  # kết quả là true vì chuỗi "ninhthuan" có TRONG chuỗi "ninhthuan85"
print(sss)

a1 = '2004' in '04'
print(a1)  # kq là false vì chuỗi'2004' ko có TRONG chuỗi '04'

s = 'ă' < 'â'
print(s)  # kết quả là false vì 'ă' đứng sau 'â' trong mã unicode NẾU muốn true thì đổi '<' sang '>'

s1 = 'a' > 'b'
print(s1)  # kq false như BIẾN S trên và đổi '>' sang '<'

s2 = 'd' < 'g'
print(s2)  # kq là true vì 'g' đứng sau 'd'

s2 = 'o' < 'ơ'  # kq là true vì ơ đứng sau O
print(s2)

s3 = 'a' == 'a'  # kq là true vì 'a' = 'a'
print(s3)

s4 = '19' >= '20'
print(s4)  # kq là false vì 19 ko thể nhỏ bằng 20
s5 = '2021' < '2022'

print(s5)  # kq là true vì '2021' nhỏ '2022'

print('#VÍ DỤ CẶP CHUỖI NHỚ THAM KHẢO VÍ DỤ TRONG SÁCH PYTHON')
# ví dụ về cặp chuỗi kí tự
t = 'ac' > 'abc'  # kq là True vì ở kí tự thứ hai thì 'c' > 'b' nên đúng
print(t)

t1 = 'b' > 'def'
print(t1)  # kết quả là false vì chuỗi 'b' ko có trong chuỗi 'def'

mc = 'mcmc' > 'mcmcmc'  # kq là False vì độ dài 'mcmc' nhỏ hơn độ dài 'mcmcmc'
mu = 'fbcfbcfbc' < 'fbcfbcfbcfbc'  # kq là True vì độ dài 'fbcfbcfbc' nhỏ hơn độ dài 'fbcfbcfbcfbcfbc'
print('khi ko tìm thấy có kí tự khác nhau thì CHƯƠNG TRÌNH sẽ so sánh độ dài của 2 chuỗi đó :', mc)
print("này ví dụ cũng tương tự thôi như mc :", mu)

# lấy độ dài của chuỗi
a = 'học lập trình python'
c = a[6:len(a)]
print(c)  # kết quả sẽ là  "p trình python"tại vì nó bỏ từ vị trí 0 -> 5 thôi và LẤY từ vị trí số 6 cho đến hết

a = 'học lập trình python'
c = a[-6:len(a)]  # kq là python vì nó đếm ngược lại nếu len nó là âm bắt đầu -1,....-n.
print(c)

b = 'chào anh thập phú quý'
# còn có cách lấy độ dài của chuỗi là None ví dụ cho dễ hiểu nào !
b1 = b[1: None]
print(b1)  # kết quả sẽ là 'hào anh thập phú quý' vì ta lấy các vị  trị sau số 1 thôi bắt đầu từ "h" đến ""ý"

b2 = 'yêu lập trình '
b3 = b2[0: None]
print(b3)  # kết quả là tất cả phần chuỗi b2

q = 'howkteam'
q1 = q[None:5]  # kq là howkt tại vì None là vị trí đầu nên lấy từ đầu None cho đến độ dài thứ 5 CÒN SAU 5 sẽ bỏ hết
print(q1)

d = 'ninh thuận'
d1 = d[None:None]
z = 'chào em nhé '
z1 = z[:]  # kq là nó lấy cả chuỗi như là sao chép chuỗi để lấy ví dụ cho dễ hiểu

h = 'yêu VIỆT NAM '
h1 = h * 3  # kq là sao chép biến h 3 lần vì h1=h*3
print(h1)
print(z1)
print(d)  # kq là tất cả chuỗi biến d nó giống chuỗi b2 ví dụ trên [None : None] nó =(bằng) [0:None]

# chú ý : TA CÓ THỂ dùng len HOẶC None để lấy độ dài của chuỗi

p = 'python'
p1 = p[None:4:1]  # kq là pyth vì nó lấy từ None đến vị trị thứ 3 trong biến p (ko lấy vị trị thứ 4)
print(p1)

qq = 'howkteam'
qqq = qq[
      None:5:-1]  # Vì do -1 nên nó lấy sau chuỗi howkteam thành (maetkwoh) ứng với(0-1-2-3-4-5-6-7) nên kết quả là "ma"
print(qqq)

# ví dụ thêm [None:None:điểm cắt]

a1 = 'howkteam'  # 01234567
a2 = a1[None:None:2]  # kq là hwta vì nó cắt None là 0 : 2(ứng 0:1:2 cắt 0:1:2,vv)
print(a2)

cc = 'taodanghoc'  # 12345678910
ccc = cc[None:None: 4]  # kq là tao giải thich như trên
print(ccc)

dd = 'chàomừngngàynhàgiáoVIỆTNAM'
ddd = dd[
      None:None:3]  # kq là congngoỆA vì đầu tiên ta lấy 0 tới 3 sau đó lùi 0->3 thành 0->2(lùi n-1) n:bước nhảy(vd là 3)
print(ddd)

ss = 'thapphuquy'
sss = ss[None:None:-4]  # kq là yhh lấy sau chuỗi'thapphuquy'đi đầu lấy 0->4 sau đó lùi 0=>3 cứ 03 cho đến hết chuỗi
print(sss)

print('##ÉP KIỂU DỮ LIỆU')
# ép kiểu dữu liệu
az = '69'
za = 69
# kq print là 69. 69 ở đây là bản chất 2kết quả này là KHÁC NHAU có thể là chuỗi dài hoặc phép toán tử
print(az)
print(za)

# ví dụ sai để chương trình chạy báo lỗi
ca = '69' + '5'  # ta thay chuỗi+5 ('5') vô sẽ thấy kết quả khác nhau liền
ac = 69 + 5
# kq print sẽ khác nhau.Và báo lỗi với chuỗi'69'+5 vì chuỗi ko thể +5 được mà phải +chuỗi 5 mới được => +'5' và ngược lại
# ta thay chuỗi +5 vô sẽ thấy kết quả khác nhau liền
print(ca)
print(ac)
# ép kiểu là phải ép chính xác kiểu dữ liệu đó.VÍ DỤ các kiểu (int,float,complex)
# cú pháp ép kiểu: int,float,complex(<giá trị>)
# ví dụ cho dễ hiểu nào
ra = float('4.5')  # báo lỗi vì '4.5' ko phải số nguyên mà số thưc muốn đúng thay int thành float
ta = int(2004.0811)  # kq sẽ ra 2004 lấy phần nguyên bỏ phần thập phân ko phải làm tròn
ha = float(45)
sa = complex(45)
print(sa)
print(ra)
print(ha)
print(ta)
# hàm str cho chuyển đổi từ số qua chuỗi.CÚ PHÁP : str (<giá trị>).Cùng ví dụ cho nó dế hiểu thôi nào
ae = 'chào anh quý đi mấy em '
print(ae)
ea = str(69) + '5'
print(hash(ae))  # kq là hash là đối tượng ko thể thay đổi
print(hash(ea))  # GIỐNG hash ae

print('###VARIABLE.py###')
a = 3
b = (a := a + 3) + 3  # thay đổi biến a và tạo biến b
print(a)
print(b)
print(c := 100)
print(t := 4)
# so sánh toán học và toán python
print(3 > 1)
print(69 < 10)
print(1 + 1 == 2)
print(5 * 0 == 0)
print('#ví dụ về nôi dung math')
# ví dụ về nôi dung math

import math

print(math)
t = math.trunc(3.9)
print(t, ':kq là số nguyên')
q = math.sqrt(16)
print(q, ':kq là căn bậc hai')
h = math.lcm(4, 5)
print(h, ':kq là bội chung nhỏ nhất')
l = math.ceil(9.4 / 3.3)
print(l, ':kq là số nguyên và lớn hoặc bằng x')
quy = math.lcm(20, 10)  # kq là 20
print('ví dụ về ước chung lớn nhất :', quy)
m = 0;
n = 0.0
print(type(m))
print(type(n))
# giải bài tập
import math

s = math.trunc(15 / -4)
print(s)
w = 15 // -4
print(type(w))

# 1USD=22000 VND
print('#QUY ĐỔI TIỀN TỆ')
USD = 1
VND = 22000
QUYDOITIENTE = USD * VND
print('1USD bằng bao nhiêu VND =', QUYDOITIENTE, 'đồng')

# 1 TRIỆU USD = ?VND
USD = 1000000
VND = 22000
QUYDOITIENTE = USD * VND
print('1TRIỆU USD bằng bao nhiêu =', QUYDOITIENTE, 'đồng')

print('#PHÂN BIỆT RÕ RÀNG VỀ TOÁN TỬ VÀ CHUỖI ĐẤY NHÉ')
a = 23
b = a * 2
print(b, 'kết quả này khác hẵn với chuỗi nhé lấy vd cho dễ nào')
a = '23'
b = a * 2
print(b, 'print ra kq khác hẳn trên là toán tử và dưới là chuỗi')

print('#Chuỗi đinh dạng - {f-string}')  # chú ý ngoặc nhọn{}                                        #VD1
t = 'THẬP PHÚ QUÝ'
p = 'VĂN LÂM 3 PHƯỚC NAM THUẬN NAM NINH THUẬN '
q = '0123456789'
tpq = f'HỌ VÀ TÊN:{t}\nĐỊA CHỈ:{p}\nSĐT:{q}'
print(tpq)  # kq là
# HỌ VÀ TÊN:THẬP PHÚ QUÝ
# ĐỊA CHỈ:VĂN LÂM 3 PHƯỚC NAM THUẬN NAM NINH THUẬN
# SĐT:0123456789


print('#CHUỖI ĐỊNH DẠNG f-string 2 LẦN ngoặc nhọn {{}} cùng xem ví dụ để hiểu thêm nào')  # VD2
t = 'THẬP PHÚ QUÝ'
p = 'VĂN LÂM 3 PHƯỚC NAM THUẬN NAM NINH THUẬN '
q = '0123456789'
tpq = f'HỌ VÀ TÊN:{{t}}\nĐỊA CHỈ:{{p}}\nSĐT:{{q}}'  # CHÚ Ý: ngoặc nhọn {{}}
print(tpq)  # và kết quả khác hẳn ở kq trên #VD1 và vd2 bỏ 1 hoặc 2 ngoặc nhọn thì CT vẫn chạy bth nhé.NHỚ VẬN DỤNG PRO

print('#ĐỊNH DẠNG BẰNG PHƯƠNG THỨC format')
a = 'a:{},b:{},c:{}'.format('thập', 'phú', 'qúy')
print('XUẤT RA KẾT QUẢ BẰNG ĐỊNH DẠNG #formath#:', a)

print('#VD NÂNG CAO')
a = 'a:{1},b:{2},c:{0}'.format('thập', 'phú', 'qúy')  # khi đó formath đánh dấu là #thập là 0 #phú là 1 và #quý là 2
print(a)  # kq sẽ khác vd trên.VÌ c:{0} nên nó bằng chuỗi'thập'.TỰ LẤY VD RỒI SUY RA và CỨ ĐỌC SÁCH RỒI SẼ HIỂU THÔI

print('#VÍ DỤ THÊM VỀ ĐỊNH DẠNG format')
# ví dụ này đối với xuất tất cả
a = 'Thập Phú Quý có tiểu sử như sau:{0},{1},{2}'.format('VĂN LÂM 3', 'PHƯỚC NAM -THUẬN NAM', 'NINH THUẬN')
print(
    a)  # kq là Thập Phú Quý có tiểu sử như sau:VĂN LÂM 3,PHƯỚC NAM -THUẬN NAM,NINH THUẬN.  cứ thay bình thường vô thôi

print('#VÍ DỤ này chỉ xuất 1 hoặc trùng nhau thì kq sx ntn đây')
# vd này chỉ xuất 1 hoặc trùng nhau thì kq sx ntn đây
a = 'Thập Phú Quý có tiểu sử như sau:{0},{1}'.format('VĂN LÂM 3', 'PHƯỚC NAM -THUẬN NAM', 'NINH THUẬN')  ##
print(a)  # format tự định dang là 0:VL3,1:PN-TN và 2:NT. TỪ VIẾT TẮT TRÊN (##)

# vd này trùng nhau chỗ lấy format
a = 'Thập Phú Quý có tiểu sử như sau:{0},{1},{1}'.format('VĂN LÂM 3', 'PHƯỚC NAM -THUẬN NAM', 'NINH THUẬN')
print(a)  # kq là 1 lần văn lâm 3 và 2 lần PN-TN
a = 'Thập Phú Quý có tiểu sử như sau:{0},{0},{0}'.format('VĂN LÂM 3', 'PHƯỚC NAM -THUẬN NAM', 'NINH THUẬN')
print(a)  # kq là IN RA 3 lần VĂN LÂM 3
a = 'Thập Phú Quý có tiểu sử như sau:{1},{1}'.format('VĂN LÂM 3', 'PHƯỚC NAM -THUẬN NAM', 'NINH THUẬN')
print(a)  # 2 lần PHƯỚC NAM - THUẬN NAM

a = 'Thập Phú Quý có tiểu sử như sau:{2},{2},{2}'.format('VĂN LÂM 3', 'PHƯỚC NAM -THUẬN NAM', 'NINH THUẬN')
print(a)  # kq 3 lần NINH THUẬN

print('#VÍ DỤ NÂNG CAO VỀ ĐỊNH DẠNG FORMAT CÙNG BẮT ĐẦU THÔI NÀO')
a = '1:{one},2:{two}'.format(one=111, two=222)
print(a)  # kq là 1:111,2:222

# ví dụ đảo ngược vị trí của nó
a = 'BIỆT HIỆU:{1},XÀM XÍ ĐÚ :{0}'.format('BÀNH VĂN NGÒ', "DEO BIẾT NÓI GÌ CẢ")
# nó tự định dạng BÀNH VĂN NGÒ là 0 và DEO BIẾT NÓI GÌ CẢ là số 1
print(a)  # kq sẽ là bị đảo ngược BIỆT HIỆU:DEO BIẾT NÓI GÌ CẢ,XÀM XÍ ĐÚ :BÀNH VĂN NGÒ

a = 'BIỆT HIỆU:{0},XÀM XÍ ĐÚ :{1}'.format('BÀNH VĂN NGÒ', "DEO BIẾT NÓI GÌ CẢ")
print(a)  # kq này khác hẳn ở ví dụ trên đấy nhé. CHÚ Ý : BIỆT HIỆU:BÀNH VĂN NGÒ,XÀM XÍ ĐÚ :DEO BIẾT NÓI GÌ CẢ

print("#VÍ DỤ VỀ 3 CĂN LỀ CỦA PHƯƠNG THỨC FORMAT")
a = '{:*^50}'.format('MUMCFCB')
print('đây là ví dụ căn lề giữa', a)  # kq là *********************MUMCFCB**********************

a = '{:*>50}'.format('MUMCFCB')
print('đây là ví dụ về căn lề phải', a)  # kq là *********************MUMCFCB

a = '{:*<50}'.format('MUMCFCB')
print('đây là ví dụ về căn lề trái', a)  # kq là MUMCFCB**********************
print('#VÍ DỤ NÂNG CAO VỀ CĂN LỀ')

a = 'Thập {:$^15} Quý '.format('Phú')  # kq là Thập $$$$$$$$Phú$$$$$$$$$$$ Quý
print(a, ': NÂNG CAO Vjpro')

print("#ÔN LẠI NHỮNG KIẾN THỨC ĐÃ HỌC")
# print trong python
a = '#helo các bạn'
print(a)

# comment ghi chú
a = '#ghi chú là comment và được kí hiệu là dấu thân(#)'
print(a)

print('### variable(BIẾN)tiếp theo###')
a = '#tự học lập trình python '
print(a)

# một số dữ liệu cơ bản của python như số thực(float),số nguyên(int),số phức(complex),....
a = 123.8
print(type(a))  # kq là <class 'float'>ý nghĩa là biến a thuộc lớp số thực float và lấy vd tương tự

# tạo phân số fraction
from fractions import *

a = Fraction(3, 9)
print(a)
# nd chuỗi xài r'nd chuỗi'
a = r'\thapphuquy'
print(a)
# toán tử +
a = 'MU'
a += ' gặp MC '  # += nó giống như dấu = và tương tự với dấu nhân *
b = 'sẽ như thế nào '
b1 = a + b
print(b1)
# toán tử in kết quả chỉ có TRUE HOẶC FLASE
a = "tpq" in 't'
print(a)
# xem kí tự trong bãng mả unicode. CỨ LẤY VÍ DỤ TƯƠNG TỰ
a = 'h'
print(ord(a))
a = '6'
print(ord(a))
a = '@'
print(ord(a))
# Indexing
a = 'thapphuquy'
print(a[6])
print(a[-7])
# kiểm tra độ dài chuỗi
a = 'tên thapphuquy'
print((a), 'có độ dài là ', len(a))
# cắt chuỗi
a = 'thapphuquy'
print(a[0:10])  # kq là thapphuquy

# sử dụng None để lấy chuỗi khi quá dài
a = 'adfghjkl'
print(a[1:None])  # kq là bỏ'a' lấy hết
print(a[None:None])  # lấy toàn bộ biến a
print(a[None:4])  # kq là adfg
print(a[-7:None])  # kl toàn bộ

# CẮT CHUỖI TỪ PHẢI QUA TRÁI cú pháp xem sách python
a = 'YÊU MU MC FCB'
print(a[2:5:2])  # kq là UM
print(a[6:8])  # kq là  cách M
print(a[7:11])  # MC F
# ép kiểu dữ liệu
a = '08112004'
b = 204
print(type(a))
print(type(b))
# phân biệt so sánh chuỗi với so sánh toán học
a = '08112004' * 2  # nghĩa là MỘT CHUỖI NHÂN VỚI MỘT SỐ
print(a)
a = 8112004 * 2  # nghĩa là MỘT SỐ NHÂN VỚI MỘT SỐ
print(a)
# hàm int
quy = '2004'
b = a
print(type(b))
# THỨ TỰ ÉP KIỂU DỮ LIỆU int , float , str , .........

# THAY ĐỔI NỘI DUNG CHUỖI
a = 'yêu python'
a = 'Y' + a[1:]
print(a)
print('#LÀM QUEN CÙNG HÀM hash')

a = 'abcd'
print(hash(a), 'ví dụ về hàm hash')

a = '#bài tập chung về math và các kiểu hàm .trunc,.fasb,.floor,.ceil,.sqrt,.gcd,.lcm#'
print(a)
import math

a = math.sqrt(9)  # cứ ví dụ tương tự với các kiểu hàm khác thêm cho nhớ bài học nhé anh QUÝ
print(a)
print('#TOÁN TỬ TRONG PYTHON')
# ví dụ về toán tử %s , %d, %r , %f , .....
a = 'tên'
print(a, ':thập phú quý')  # kiến thức cũ vẫn chưa thấy lạ lẫm gì đk
print('#VÍ DỤ %s')
a = 'thập phú %s ' % (
    'quý')  # ý nghĩa biến a thay %s bằng%('trong chuỗi')cụ thể là thế %s thành ('quý').Rồi print ra cứ in nv
print(a, 'là một ví dụ về %s')
a = 'thập phú quý %s tuổi rồi' % ('17')  # nếu thêm 1%s vô CT báo lỗi.Muốn đúng phải thêm chỗ %('17','nd thêm vào'
print(a)
print('#TÓM TẮT CHUNG :dư bên %s,r,d,f... thì CT vẫn chạy còn thiếu BÊN SAU % thì báo lỗi .NHỚ xem VD VÀ LÀM BT ĐỂ NHỚ')
# ví dụ dễ hình dung nhé cậu QUÝ
# a='YÊU ĐB MU FBC MC %s %s'%('HAHAHA')
# print(a)#CT BÁO LỖI VÌ BÊN %s ko bằng % bên kia. XÓA # CT SẼ SAI.ĐỂ # CT coi như là một commend.MUỐN SỬA ĐÚNG THÌ XEM VD
a = 'YÊU ĐB MU FBC MC %s %s' % ('haha', 'haha lần 2')
print(a, ': VÍ DỤ XÀM XÍ ĐÚ ẤY MÀ ')  # ct báo đúng ngay và chạy ngay lập tức
a = '%s %s'
print(a, ':in bình thường thôi cái này đã học rồi nhé ANH QUÝ')
a = '%s %s '
a1 = a % (
'one', 'two')  # TỨC là bạn hoàn toàn có thể gán cái chuỗi này in trước đó(chuỗi định dạng ấy) vào các chuỗi khác
# và tái sử dụng lại.Mục đích là xđ cụ thể những chỗ nào bạn cần hiển thị cái gì giống như bạn có 1 biến trong chuỗi ấy
# và có nhiều vị trí cần thay đổi chỉ cần cái biến nhét đúng vào vị trí cần thay đổi.COI VD SẼ HIỂU THÔI
print((a1), ':ví dụ thêm về %s')
print('#VÍ DỤ VỀ %r')
a = 'thập phú %r ' % ('quý %r')
print(a, 'ví dụ về %r')

print("#CÁC PHƯƠNG THỨC CỦA KIỂU DỮ LIỆU CHUỖI TRONG python")
print('*CÁC PHƯƠNG THỨC BIẾN ĐỔI')
print('1.PHƯƠNG THỨC capitalize')
a = 'thập Qúy'
b = a.capitalize()
print(b)  # kq là in chữ đầu là HOA và các chữ còn lại chữ THƯỜNG
print('2.PHƯƠNG THỨC upper')
a = 'bành văn ngò'
b = a.upper()
print(b)  # kq là in ra TẤT CẢ CHỮ HOA
print('3.PHƯƠNG THỨC lower')
a = 'mU MC fCB'
b = a.lower()
print(b)  # kq in ra TẤT CẢ CHỮ THƯỜNG
print('4.PHƯƠNG THỨC swapcase')
a = 'tôI YÊu vIỆt NaM'
b = a.swapcase()
print(b)  # kq là in ra chữ thường thành chữ HOA và NGƯỢC LẠI.
print('5.PHƯƠNG THỨC title')
a = 'ninh THuận quê Tôi'
b = a.title()
print(b)  # kq là in ra chuỗi với ĐỊNH DẠNG LÀ TIÊU ĐỀ.
print('\t''+NHỚ THAM KHẢO VÀ ÔN BÀI NHÉ BÀNH VĂN NGÒ+')
print('*CÁC PHƯƠNG THỨC ĐỊNH DẠNG')
print('1.PHƯƠNG THỨC center')
a = 'THẬP QUÝ'
b = a.center(15, '$')
print(b)  # kq là in ra $$$THẬP QUÝ$$$ với căn lề GIỮA có chứa kí tự $.
print('2.PHƯƠNG THỨC rjust')
a = 'haha là hihi'
b = a.rjust(20, '!')
print(b)  # kq là in ra !!!!!haha là hihi với căn lề PHẢI
print('3.PHƯƠNG THỨC ljust')
a = 'TIÊM VỀ KHỎE RA VÊ LỜ '
b = a.ljust(25, '^')
print(b)  # kq là in ra TIÊM VỀ KHỎE RA VỀ LỜ ^^^ .
print('\t!!!NHỚ ÔN LẠI KIẾN THỨC ĐÃ HỌC NHÉ!!!')
print('*CÁC PHƯƠNG THỨC XỬ LÍ')
print('1.PHƯƠNG THỨC encode')
a = 'THẬP PHÚ QUÝ'
b = a.encode()
print(b)  # kq này được gọi là MÃ HÓA


print('2.PHƯƠNG THỨC join')
a = 'Tôi Yêu Lập Trình'
b = a.join(('@ ', '+ ', '- '))
print(b)  # kq này gọi nối các chuỗi bằng các kí tự trong ngoặc().NHỚ THAM KHẢO TRONG SÁCH NHÉ


print('3.PHƯƠNG THỨC replace')
a = 'Tôi thích đội bóng MU MC FCB'
b = a.replace('MC', '2012')#kq là Tôi thích đội bóng MU 2012 FCB
print(b)


a1 = 'abc how abc kteam'.replace('abc', 'AA', 1)
print(a1, ':số lần thay thế chỉ 1 lần')#kq là AA how abc kteam :số lần thay thế chỉ 1 lần


a2 = 'abc how abc kteam'.replace('abc', 'BB', 0)##vì có 0 là kq trả lại chuỗi ban đầu
print(a2, ':số lần thay thế bằng 0 sẽ ntn')# kq là abc how abc kteam :số lần thay thế bằng 0 sẽ ntn


a = 'Tôi thích đội bóng MU MC FCB' # có thể nhiều chuỗi
b = a.replace('MC', 'Manchester City') #kq là Tôi thích đội bóng MU Manchester City FCB
print(b)


a = 'Tôi thích đội bóng MU MC FCB'
b = a.replace('MC', '2004', 0)
print(b)  # kq là trả về chuỗi ban đầu


a = 'Tôi Thích TtT đội bóng MU MC FCB'#python đánh dấu 'T' lần lượt là 1,2,3.       CHÚ Ý KO BẮT ĐẦU SỐ 0
b = a.replace('T', '@@', 3)
print(b)  # kq là @@ôi @@hích @@tT đội bóng MU MC FCB.VÌ T thay @@ 3 lần từ TRÁI sang Phải.Sau lần t3 thì giữ nguyên.


a = 'Tôi thích đội bóng MU MC FCB'
b = a.replace('MC', '2004', 0)
print(b)  # kq vẫn vậy ko thay 'MC' thành '2004' đâu nhé bạn già do có SỐ 0. NHỚ THAM KHẢO TRONG SÁCH NHIỀU VÔ NHÉ.


print('4.PHƯƠNG THỨC strip')  # |chú ý| nếu chuỗi có nhiều chars chỉ cắt đúng 1.COI TRONG SÁCH VÀ VỞ PYTHON HIỂU THÊM..
a = 'TPQ tpq TPQ'
b = a.strip('TPQ')
print(b)  # kq là tpq.         TỨT là là nó cắt đi phần đầu và phần đuôi có trong ('TPQ') gọi là [(chars)].


a = 'THẬP phú QUý'
b = a.strip('T')  # kq là HẬP phú QUý.   TỨC là cắt bỏ phần đầu T và phần còn lại giữ nguyên
print(b, ':ví dụ thêm về strip(CẮT)')

a='TÔI LÀ TÔI 2021'# phần nằm trong () có thể đảo ngược như ví dụ ở dưới đây
b=a.strip('10T')#kq là ÔI LÀ ÔI 202. NẾU CÓ SỐ 0 THÌ VẪN LẤY SỐ 0
print(b)


print('5.PHƯƠNG THỨC rstrip')
a = ' ^^^^^ MONG CÓ PHÉP MÀU ĐẾN GIA ĐÌNH CỦA BẠN ^^^^^'
b = a.rstrip('^')
print(b)  # kq chỉ lấy phần bên TRÁI bỏ bên PHẢI



print('6.PHƯƠNG THỨC lstrip')
a = '+++Cầu mong cầu mong và chỉ cầu mong+++'
b = a.lstrip('+')
print(b)  # kq chỉ lấy phần sau VÀ bỏ kí tự phần đầu trong ngoặc.TỨC lấy PHẢI bỏ TRÁI trong()


print('7.PHƯƠNG THỨC removeprefix')
a = 'chào chào chào mừng bạn đến với tự học lập trình'
b = a.removeprefix('chào')  # CÔNG DỤNG : là trả về một chuỗi MỚI bỏ đi phần trong ngoặc()còn đc gọi là [prefix]
print(b)  # kết quả sẽ là|mừng bạn đến với tự học lập trình|.Nếu [prefix] ko có sẽ tự động trả về CHUỖI BAN ĐẦU


print('8.PHƯƠNG THỨC removesuffix')
a = 'chào nhé anh Qúy Qúy'
b = a.removesuffix('Qúy')  # CÔNG DỤNG: cũng như removeprefix NHƯNG nó xóa đi phần chuỗi ở CUỐI.
print(b)  # kq là              chào nhé anh Qúy



print('#PHƯƠNG THỨC TÁCH CHUỖI ')
print('1.PHƯƠNG THỨC split')
a = 'bạn có ổn chứ'
b = a.split(' ')  # vd với sep = khoảng cách
print(b)  # kq là ['bạn', 'có', 'ổn', 'chứ'].     COI THÊM VD TRONG SÁCH VỞ ĐỂ HIỂU THÊM VỀ VD NÀY
a = 'mong hư sẽ ổn nhé'
b = a.split('n')  # với sep='n'
print(b)  # kq là      ['mo', 'g hư sẽ ổ', ' ', 'hé']. CHỖ NÀY CAU CŨNG CHƯA HIỂU CHO LẮM nên tìm hiểu thêm nhé
a = 'mạnh mẽ lên hư'
b = a.split(' ', 2)  # số 2 này cứ hiểu là cắt bao nhiểu lần.
print(b)  # kq là      ['mạnh', 'mẽ', 'lên hư']
a = 'mạnh mẽ lên hư'
b = a.split('m', 1)  # giải thích: tại biến b cắt 'm' 1 lần trong biến a
print(b)  # kq là          ['', 'ạnh mẽ lên hư']
a = 'mạnh mẽ lên hư'
b = a.split('lên', -1)  # giải thích:tại biến b cắt chuỗi'lên' với số lần -1 sẽ đếm từ P -> T
print(b)  # kq là           ['mạnh mẽ ', ' hư']
a = 'chúc--hư--tất--cả'
b = a.split('--')  # bỏ đi phần cắt --
print(b)  # kq là      ['chúc', 'hư', 'tất', 'cả']
a = 'qua+cú+sốc+này+nhé+hư'
b = a.split('+')  # bỏ đi'+'
print(b)  # kq là      ['qua', 'cú', 'sốc', 'này', 'nhé', 'hư']
print('2.PHƯƠNG THỨC rsplit')  # P
a = 'cố gắng lên nhé '
b = a.rsplit(' ', 2)  # tách từ phải sang trái.         số lần tách là 2 lần
print(b, ': ví dụ là rsplit')  # kq là         ['cố gắng lên', 'nhé', ''] rsplit
print('3.PHƯƠNG THỨC lsplit')  # ví dụ nó không ra đau lòng quá                    #T
# a='cố gắng lên nhé '
# b=a.lsplit(' ',2)
# print(b,': ví dụ là lsplit')
a = 'ta là điên khùng đấy nhé ko biết lấy vd nữa luôn'
b = a.rsplit('luôn', 4)
print(b, ': VD THÊM VỀ rsplit ')
a = 'xàm xí đú đú xí xàm haha hihi'
b = a.rsplit(' ', -1)
print(b, ':vd về rsplit nữa')  # kq là  ['xàm', 'xí', 'đú', 'đú', 'xí', 'xàm', 'haha', 'hihi'] :vd về rsplit nữa
a = 'xàm xí đú đú xí xàm haha hihi'
b = a.rsplit(' ', 1)
print(b, 'vd rsplit lần 2')  # kq là        ['xàm xí đú đú xí xàm haha', 'hihi'] vd rsplit lần 2
a = 'xàm xí đú đú xí xàm haha hihi'
b = a.rsplit(' ', 8)
print(b, 'vd rsplit lần 3')  # kq giống -1
a = 'xàm xí đú đú xí xàm haha hihi'
b = a.rsplit('xí', 7)
print(b, 'lần 4')  # chú ý từ xí.Do có xí 2 lần nên kq là  ['xàm ', ' đú đú ', ' xàm haha hihi'] lần 4
print('#NHỚ TÌM HIỂU PHẦN NÀY CAU VẪN CÒN HOANG MANG LẮM  KAKAKAKAKA')
print('4.PHƯƠNG THỨC splitlines')
a = 'thap\nphu\nquy\nTPQ'
b = a.splitlines()  # CÔNG DỤNG như split nhưng các phần tử \n là xuống dòng bài cũ
print(b, ':đây là ví splitlines')  # kq là ['thap', 'phu', 'quy', 'TPQ']
a = 'thap\nphu\nquy\nTPQ'
b = a.splitlines(True)  # keppendes là true tách bởi phần tử \n và kq sẽ là   ['thap\n', 'phu\n', 'quy\n', 'TPQ']
print(b, ':keppends là True')
a = 'thap\nphu\nquy\nTPQ'
b = a.splitlines(False)  # keppendes là false tách bởi phần tử \n và kq GIỐNG \n là    ['thap', 'phu', 'quy', 'TPQ']
print(b, 'keppendes là False')
print('5.PHƯƠNG THỨC partition')
a = 'Bành Văn Ngò là biệt hiệu'
b = a.partition('V')
print(
    b)  # kq là ('Bành ', 'V', 'ăn Ngò là biệt hiệu').giải thích:nó tìm chỗ nào có chữ V tách cái chuỗi ra làm đôi.COI VD
a = 'Bành Văn Ngò là biệt hiệu'
b = a.partition('Văn')  # kq là ('Bành', 'Văn', 'Ngò là biệt hiệu')
print(b, ':lấy 1 chuỗi kq sẽ ntn đây ?')
a = 'Bành Văn Ngò là biệt hiệu'
b = a.partition('văn')  # kq là ('Bành Văn Ngò là biệt hiệu','','')
print(b, ':lấy 1 chuỗi ko có trong biến a kq sẽ ntn đây ?')
print('6.PHƯƠNG THỨC rpartition')
# a='thap phu quy python'
# b=a.rpartiton('') hoặc () # chương trình sẽ báo lỗi nếu để ('')hoặc ()
# print(b)
a = 'thap phu quy python'
b = a.rpartition('Y')  # kq là ('','','thap phu quy python')
print(b)
# nếu lấy kí tự hay 1 chuỗi có trong biến thì kq sẽ khác đấy nhé cùng vd cho dễ hiểu nào.CHÚ Ý:rpartition lấy từ P SANG T
a = 'thap phu quy python'
b = a.rpartition('y')  # kq là ('thap phu quy p','y','thon')
print(b, ':ví dụ thêm rpartition')
print('#PHƯƠNG THỨC TIỆN ÍCH')
print('1.PHƯƠNG THỨC count')
a = 'python python python python '
b = a.count('y')  # kq là 4.GIẢI THÍCH thêm là từ biến a đếm có bn kí tự là 'y' có trong BIẾN a thế thôi đơn giản
print('đếm số lượng có bao nhiêu là', b)
# ví du này với chuỗi trong biến
a = 'python python python python '
b = a.count(
    'python')  # kq là 4.GIẢI THÍCH thêm là từ biến a có bn CHUỖI tên là python co trong biến a THẾ THÔI HIỂU HIỂU
print('đếm chuỗi pythom có bn trong biến a : ', b)
# ví dụ thêm về count
a = 'pypypy'
b = a.count('y', 3)  # kq là 2.GT:tìm cho tôi trong biến a có bn chữ y từ đầu đến vị trí số 3.
print(b, ':vd này có end')
# ví dụ thêm về count có start và end
a = 'tôi yêu lập trình'
b = a.count('l', 0, 5)  # kq là 0 vì tại vị trí kết thúc end 5 ko có có chữ l
print(b, ':lần 1 vd về count')
a = 'tôi yêu lập trình'
b = a.count('l', 0,
            9)  # kq là 1 vì tại vị trí end là 9 có xuất hiện chữ l. count tăng lên 1 đơn vị:8 thành 9 và 9 thành 10,..
print(b, ':vd thêm count')
print('2.PHƯƠNG THỨC startswith')
a = 'Thập Qúy'
b = a.startswith('Th')  # kq là True vì bắt đầu chuỗi là 'Th'
print(b)
# vd thêm startwith
a = 'Thập Qúy 27/11'
b = a.startswith('27/11')  # kq là False
print('ví dụ thêm startswith:', b)
# vd thêm về startswith
a = 'thâp phú quý 2021'
b = a.startswith('T', 0, 5)  # kq là false vì từ vị trí 0 đến 5 ko có kí tự T
print('xem kq sẽ ntn đây :', b)  # NHỚ COI THÊM BÀI TẬP TRONG SÁCH PYTHON
print('3.PHƯƠNG THỨC endswith')
a = 'môn l khó lắm thế nhỉ'
b = a.endswith('ỉ')  # kq là True vì kết thúc là chữ ỉ
a = 'môn l khó lắm thế nhỉ'
b = a.endswith('i')
print('đúng với chữ ỉ :', b)
print('sai với chữ i :', b)  # sai vì trong python có phân biệt chữ hoa thường và dấu khi ta INPUT vào
# ví dụ về endswith
a = 'môn l khó lắm thế nhỉ'
b = a.endswith('m')
print(b, 'kết quả chắc là false')  # vì kết thúc chỉ chữ ỉ chứ ko phải là m
print('4.PHƯƠNG THỨC find')
a = 'hôm nay là chủ nhật'
b = a.find('nay')  # kq là 4.Vì từ đầu chuỗi đến vị trí 'nay' bắt đâu là 456 nên có kq là 4
print('tìm chuỗi có từ "nay" kết quả sẽ là : ', b)
# còn nếu find là vị đầu tức là =0 kq sẽ ntn đây
a = 'hôm nay là chủ nhật phải chứ'
b = a.find('h')  # kq là 0.Vì h xuất hiện đầu tiên tức là = 0
print('lấy từ vị trí đầu kq sẽ ntn đây:', b)
# nếu find chuỗi từ vị trí đã cho trong() thì kq sẽ là -1.  CÙNG VÍ DỤ CHO DỄ HIỂU NÀO
a = 'hôm nay là chủ nhật mà nó cứ mưa hoài'
b = a.find(
    'q')  # kq là -1.GT:hãy tìm cho tôi từ biến a find ra ở vị trí 5 có xuất hiện chữ 'y' hay ko ?NẾU KO KQ LÀ= -1
print('ví thêm về find ko có xuất hiện trong chuỗi : ', b)
# ví dụ về find có sup,start và end
a = 'đờ mờ mưa gì lắm thế'
b = a.find('m', 0, -1)  # kq là 3.TẠI VỊ TRÍ 3 XUẤT HIỆN m nên = 3
print('có sup,start và end :', b)
print('5.PHƯƠNG THỨC rfind')
a = 'ngừng mưa hộ cái trời ơi'
b = a.rfind('m')  # kq là 6
print('đây là ví dụ về rfind:', b)
print('6.PHƯƠNG THỨC index kết quả của phương thức này CT BÁO LỖI')
# a='hahahahahahahahihihihihhihi'
# b=a.index('b')#kq là CHƯƠNG TRÌNH BÁO LỖI. NÓ(index) giống find chỉ khác là nếu ko thấy thì CT BÁO LỖI.  DỄ HIỂU
# print('vd về index cho nó báo lôi chơi:',b)
print('7.PHƯƠNG THỨC rindex')
a = 'abcde'
b = a.rindex('c')  # kq là 2 nó giống find thôi.NẾU KO TÌM THẤY BÃO LỖI giống index ấy.NẾU('z) ct báo lỗi ngay lập tức
print(b)
print('#CÁC PHƯƠNG THỨC XÁC THỰC')
print('1.PHƯƠNG THỨC islower')
a = 'thapphuquy08112004'
b = a.islower()  # kq là True.Vì chuỗi bắt đầu chữ thường.Nếu thay t ->T kq là false
print('ví dụ về islower:', b)
print('2.PHƯƠNG THỨC isupper')
a = 'THAPPHUQUY CÓ BIỆT HIỆU LÀ BÀNH VĂN NGÒ'
b = a.isupper()  # kq là True.Nếu thay T -> t kq là false luôn nhé QUÝ
print('ví dụ về isupper:', b)  # CHÚ Ý PYTHON CÓ PHÂN BIỆT CHỮ HOA VÀ CHỮ THƯỜNG ĐẤY NHÉ BẠN GIÀ  hahahahahaha
print('3.PHƯƠNG THỨC istitle')
a = 'Tôi Là Thập Phú Qúy'
b = a.istitle()  # kq là True.CÒN NẾU 'TÔI là thập Phú Qúy' kq là sẽ là False
print('ví dụ về istitle : ', b)
print('4.PHƯƠNG THỨC isidentifier')
a = '_hết mưa'
b = a.isidentifier()  # kq là false. VÌ CÓ KHOẢNG TRẮNG
print('ví dụ về isidentifier :', b)
# vd thêm về isidentifier
a = 'tpq'
b = a.isidentifier()  # kq là True.      VÌ chuỗi bắt đầu là kí tự chữ
print('ví dụ isidentifier lần 2 :', b)
# ví dụ isidentifier có kq là false
a = '$tiền'
b = a.isidentifier()  # kq là false.VÌ CHUỖI CÓ CHỨA KÍ TỰ ĐẶC BIỆT LÀ $ nên false
print('ví dụ có kq sai về isidentifier :', b)
print('5.PHƯƠNG THỨC isdigit')
a = '08112004'
b = a.isdigit()  # kq là true.VÌ BIẾN LÀ SỐ NÊN THÕA MÃN CÔNG DỤNG CỦA NÓ ĐỀ RA
print('ví dụ về isdigit :', b)
# ví dụ về isdigit ra kq là False
a = 'tpq08112004'
b = a.isdigit()  # kq là False.VÌ BIẾN A CÓ CHỮ XUẤT HIỆN ĐẦU NÊN RA KẾT QUẢ LÀ FALSE.CHÚ Ý:isdigit chỉ nhận chuỗi là con số
print('ví dụ isdigit ra kq là False :', b)
print('6.PHƯƠNG THỨC isspace')
a = ' '
b = a.isspace()  # kq là True,VÌ TRONG DẤU ' ' có khoảng trắng
print('ví dụ về isspace :', b)
# ví dụ ra kq là false
a = '     ế     ế      ế      nữa     '
b = a.isspace()  # kq là false
print('ví dụ ra kq là false :', b)
print('7.PHƯƠNG THỨC iskeyword')
import keyword

b = keyword.iskeyword('not')  # kq là True.VÌ 'not' có trong từ khóa của Python nên đúng
print('ví dụ về keyword :', b)
# ví dụ về từ khóa của python ra kq là false
import keyword

b = keyword.iskeyword('TPQ')  # kq False vì trong từ khóa của python ko có 'TPQ' nên sai
print('100% kq là False :', b)

print('#MỘT SỐ escape sequence CƠ BẢN')
a = 'TỨT chưa ngủ mà mưa con mẹ nó rồi \bai \bbebbe conbedobe\beb'
print('1 số escape sequence :', a)
# kq là TỨT chưa ngủ mà mưa con mẹ nó rồiaibebbe conbedobeb
a = 'hahhahhahahahahahahahhahahaha\thahahahahaahah'
print('ví dụ về \\t:', a)

# VÍ DỤ NÀY CÁI NÀO CÒN THẮC MẮC ĐẤY THÔI NHÉ
print('#MỘT SỐ escap sequence NHỚ COI THÊM BÀI TẬP')
a = 'quý quy quy\t     hahahahah\thahahah'
print('đây là tab bằng \\tt', a)
a = 'ha\'hahhhaha\'hhahahahahha\'hahhaha'
print("vd về \' thôi:", a)
print('### VÍ DỤ VỀ  len lấy độ dài')
a = 'chiếm lấy em đi'
b = a[14:len(a)]  # kq là i vì vị trí 14 là i
print('XUẤT len :', b)


print('###ví dụ nâng cao về f-string###')
#Chuyển số thành chuỗi trong python | hàm str()
a=18
print("Em chưa "+ str(a) +" tuổi")#kq là Em chưa 18 tuổi

#Chuyển số thành chuỗi để nối chuỗi trong python
num1 = 8
num2 = 6
print(str(num1) + "+" + str(num2) + "=" + str(num1 + num2)) #kq là 8+6=14


# vd thêm về len
a = 'chiếm lấy em đi'
b = a[15:len(a)]  # kq là không có.NÓ CÓ KẾT QUẢ NHƯ THẾ NÀY NÈ: XUẤT len lần 2:
print('XUẤT len lần 2:', b)

# ĐÂY LÀ VÍ DỤ VỀ CHUỖI
s = 'abc xyz'
print(s[1: 7: 2], 'đây là các ví dụ về cắt chuỗi')
# VÍ DỤ VỀ len LẤY ĐỘ DÀI
q = 'tôi yêu lập trình viên và ngôn ngữ thích học nhất chính là python'
a = q[len(q) - 1]  # kq là n.Vì len nó lấy độ cuối cùng
print(a)

# VÍ DỤ VỀ %s khi muốn thay thế %s thành các % khác

a = 'tpq %st: văn lâm %sp : ninh thuận %s' % ('tên :', 'địa chỉ:', 'nơi sống')
print(a)

# ví dụ về %s và %r,%d,%f
a = '%s' % ([1, 2, 3])
print(a, ': ví về %s')

a = '%r' % ([1, 2, 3])
print(a, ': đây là ví về %r')

a = '%d' % (2)  # kq là [1,2,3]
print(a, ': ví dụ về %d')

a = '%d' % (3.9)  # kq là 3 vì chỉ lấy phần nguyên
print(a, ':ví dụ %d lần 2')

# ví dụ sai %d
# a='%d'%('2')#CHƯƠNG TRÌNH BÁO LỖI vì '2' ko phải là số. DO %d chỉ NHẬN MỘT SỐ
# print(a,': ví dụ sai về %d')


a = '%f' % (5.9)  # kq 5.900000
print(a, ': ví dụ về %f')

a = '%.2f' % (5.55555)
print(a, ': ví dụ về %f lần 2')  # kq là 5.56  chỉ lấy 3 lần phần thập phân và %f có thể tự làm tròn lên

print('#CÁC PHƯƠNG THỨC XỬ LÍ CHUỖI')

# VÍ DỤ encode(mã hóa)
a = 'yêu MU MC FCB'  # kq là b'y\xc3\xaau MU MC FCB' .KẾT QUẢ này gọi là chuỗi được mã hóa
print('đây là ví dụ về encode(mã hóa) :', a.encode())



# ví dụ về join(nối chuỗi,.......)
a = "+++"# có thể bằng các khác như là haha,111,####,+haha+hihi+huhu+,.........NÓI CHUNG ĐA DẠNG
b = ("Java", "Python", "PHP")# kq là Java+++Python+++PHP.NỐI các chuỗi bằng dấu '+'(biến a)
#chuỗi b phụ thuộc vào giá trị gán vào a để nhận giá trị đó. COI VÍ DỤ RỒI SẼ HIỂU THÔI
print (a.join(b))


#ví dụ nâng cao chút nào anh QUÝ
a=''
print(a.join(["Apple", "Orange", "Lemon"]))#kq là AppleOrangeLemon.VÌ ('') ko có kí tự nên ra kq như vậy CHÚ Ý ĐIỀU NÀY


                                                # list TRONG PYTHON
print("KHỞI TẠO MỘT list")
list1 = [1, 2, 3, 4, [5, 6, 7], "A", 'B']
print(list1) #kq là [1, 2 ,3 ,4,  [5, 6 ,7] 'A', 'B']
print(type(list1)) #xuất ra kiểu dữ liệu của list

print('#CÁC THAO TÁC CƠ BẢN VỚI list')
                            #TRUY CẬP ĐẾN MỘT PHẦN TỬ CÓ TRONG list (lấy ví dụ list1 để minh họa)
print(list1[3]) # kq là 4
print(list1[4]) # kq là [5, 6, 7].VÌ list [5, 6, 7] nằm trong ( biến list1).
# NẾU THÊM (2,3,...n dấu ngoặc vuông [] )  thì (KẾT QUẢ   =  dấu ngoặc vuông đac cung cấp vô )
print(list1[5]) # kq là A
print(list1[0]) # kq là 1


                    # GÁN GIÁ TRỊ MỚI CHO MỘT PHẦN TỬ CÓ TRONG list (lấy vd biến list1)
list1 = [1, 2, 3, 4, [5, 6, 7], "A", 'B']
list1[3]=10  #kq là [1, 2, 3, 10, [5, 6, 7], 'A', 'B'] . THAY 10 vào vị trí số 3 trong ( biến list1 )
list1[4]='567'#kq là [1, 2, 3, 10, '567', 'A', 'B']  .
list1[5]=8112004 #kq là [1, 2, 3, 10, '567', 8112004, 'B']
print(list1)


                    #LẤY ĐỘ DÀI CỦA list (len)
list1 = [1, 2, 3, 4, [5, 6, 7], "A", 'B']
print('Xuất ra độ dài của list là ',len(list1)) # kq là 7


                    #THÊM PHẦN TỬ MỚI VÀO list (append)
list1 = [1, 2, 3, 4, [5, 6, 7], "A", 'B']
list1.append(['TPQ']) #kq là [1, 2, 3, 4, [5, 6, 7], 'A', 'B', 'TPQ']
list1.append(['TPQ']) #kq là  [1, 2, 3, 4, [5, 6, 7], 'A', 'B', ['TPQ']] . CHÚ Ý DẤU ngoặc vuông [ ]
print(list1)


                         #GỘP HAI list (extend)
list1 = [1, 2, 3, 4, [5, 6, 7], "A", 'B']
list2 = ['anh quy khong tam mot mot']
list1.extend(list2) #kq là [1, 2, 3, 4, [5, 6, 7], 'A', 'B', 'anh quy khong tam mot mot']
list2.extend(list1)#kq là ['anh quy khong tam mot mot', 1, 2, 3, 4, [5, 6, 7], 'A', 'B', 'anh quy khong tam mot mot']
#ra kq như vậy là đầu tiên lấy (list2) và sau đó lấy KẾT QUẢ TRƯỚC ĐÓ là (list1).

print('gộp list2 vào list1: ',list1)
print('gộp list 1 vào list 2 :',list2)


                        #XÓA MỘT PHẦN TỬ TỪ list (remove)
list1 = [1, 2, 3, 4, [5, 6, 7], "A", 'B']
list1.remove('A') #kq là xóa kí tự A có trong list1 kq là :  [1, 2, 3, 4, [5, 6, 7], 'B']
#list1.remove([5,6,7]) #la là xÓA ([đgl list2]) có trong list1 kq là  [1, 2, 3, 4, 'B']
print('XÓA kí tự A có trong list1 kq là : ',list1)


                        #SẮP XẾP list (sort)
list1 = [4, 3, 5, 2, 1, 6, 2]
list1.sort() #kq là [1, 2, 2, 3, 4, 5, 6]
print('kết quả sắp xếp của list1 là : ',list1)


list1 = [4, 3, 5, 2, 1, 6, 2]
list1.sort(reverse=True) #kq là [6, 5, 4, 3, 2, 2, 1]
print('kết quả có reverse = True sẽ ntn :',list1)


list1 = [4, 3, 5, 2, 1, 6, 2]
list1.sort(reverse=False)#kq là [1, 2, 2, 3, 4, 5, 6]
print('kết quả có reverse = False sẽ ntn :',list1)


                                                #SỬ DỤNG list comprehension
print('1.SỬ DỤNG list comprehension')
a=[tpq for tpq in range(5)]
print(a)#kq là [0, 1, 2, 3, 4] . HIỂU NÔM NA LÀ từ biến tpq để so sánh từ số đến số 5
b=[[n, n*2, n+4, n*3] for n in range(1,4)]
print(b) #kq là [[1,2,5,3], [2,4,6,6], [3,6,7,9]] .GT:lấy từ vị bắt đầu là (1,4) thực hiện các phép toán có trong list
#CỨ LẤY VÍ DỤ TƯƠNG TỰ


print('2.SỬ DỤNG CONSTRUCTOR list')
lst=([8,11,2004]) #kq là [8, 11, 2004] . chả có gì lạ cả
print(lst)

lst1=list('ĐOCHAMTIEU') #kq là ['Đ', 'O', 'C', 'H', 'A', 'M', 'T', 'I', 'E', 'U'] . CHÚ Ý : list trước ()
print(lst1)


#a=list(200292)
#print(a) #kq là báo lỗi TypeError: 'int' object is not iterable


print('3.MỘT SỐ TOÁN TỬ list trong py')
print('#Toán tử +')
a=[1,2]
q=a+['one','two'] #kq là [1, 2, 'one', 'two']
#q+='TPQ' #kq là [1, 2, 'one', 'two', 'T', 'P', 'Q']
print(q)
#CHÚ Ý : LIST cộng CHUỖI thì được , CHUỖI cộng LIST thì không được


print('#Toán tử *')
lst=list('haha')*2 #kq là ['h', 'a', 'h', 'a', 'h', 'a', 'h', 'a']
print(lst)


lst=[8,11,2004]*4 #kq là [8, 11, 2004, 8, 11, 2004, 8, 11, 2004, 8, 11, 2004]
print(lst)


print('#Toán tử in')
a=[2004,2021]
b=2004 in a #kq là True     vì 2004 có trong a
print(b)


a=[2004,2021]
b='TPQ' in a #kq là False   vì chuỗi 'TPQ' không có trong a
print(b)

print('#4.CÁC TOÁN TỬ SO SÁNH')
t=[1,2,3]==[1,2,3] # kq là True  vì [1,2,3] bằng [1,2,3]
print(t)

t=[1,2,3]==[1,2] # kq là False  vì [1,2,3] không bằng [1,2]
print(t)


p=[1,2,3] > [1,2] #kq là True vì [1,2,3] dài hơn
print(p)


q=[20] > [12,20] # kq là True vì do so sánh giá trị đầu tiên , ta có 20 > 12
print(q)


lst=['aaaa','b','c','d'] < ['aaaa','x','y','z'] # kq là True . NẾU so sánh giá trị đầu bằng nhau qua gt rồi đưa ra kq
print(lst)

print('#5.Indexing và cắt list trong Python')
list1 = [1, 2, 3, 4, [5, 6, 7], 'A', 'B',[2004]]
print(list1[4]) #kq là [5, 6, 7]
print(list1[-1]) #kq là [2004]
print(list1[0]) #kq là 1
print(list1[::-1]) #kq là đảo ngược thành [[2004], 'B', 'A', [5, 6, 7], 4, 3, 2, 1]
print(list1[1:5]) #kq là [2, 3, 4, [5, 6, 7]] Ý là lấy từ 1 tới 4 (ko lấy vị trí thứ 5)
print(list1[0:-1]) # kq là [1, 2, 3, 4, [5, 6, 7], 'A', 'B'] . CHÚ Ý : bỏ phần -1
print(list1[:4]) #kq là [1, 2, 3, 4] . NÓ HIỂU LÀ lấy từ vị trí 0 đến vị trí 3 ( KO LẤY VỊ TRÍ SỐ 4 )
print(list1[::]) #kq là [1, 2, 3, 4, [5, 6, 7], 'A', 'B', [2004]]       lấy nguyên list1


print('#6.THAY ĐỔI NỘI DUNG list trong Python')
print('MA TRẬN ')
a=['tôi '],['tên '],['TPQ ']
print(a[0]) #kq là ['tôi ']
print(a[1]) #kq là ['tên ']
print(a[2]) #kq là ['TPQ ']
#XEM THÊM CÁC BÀI TẬP TRONG SÁCH


print('#7.TOÁN TỬ is')
a=[1 ,2, 3]
b=[1, 2, 3]
print(a is b) #kq là False


a[1]=100
print(a) #kq là [1, 100, 3]
print(b) #kq là [1, 2, 3]


a=[1, 2, 3]
b=a
print(b is a) #kq là True
a[1]=100
print(a) #kq là [1, 100, 3]
print(b) #kq là [1, 100, 3]


print('#CÁC PHƯƠNG THỨC CỦA KIỂU DỮ LIỆU list TRONG python')
print('1PHƯƠNG THỨC count')
a=[8,11,2004,8,11,2021]
b=a.count(8) # kq là 2 VÌ 8 xuất hiện 2 lần trong biến a
print('xuất ra có bao nhiêu số 8 trong biến a :',b)

a=[1,62,34,5,5,]
b=a.count(11) #kq là 0 VÌ 11 ko xuất hiện trog biến a
print('xuất xem có bn số 11 có trong a :',b)



print('2.PHƯƠNG THỨC index')
a=['hahha',888,111,200004]
b=a.index('hahha') #kq là O  VÌ hahha xh vị trí 0
print('hahha xuất hiện ở vị trí thứ mấy :',b)
    #NẾU (sub) không thấy CT BÁO LỖI


print('3.PHƯƠNG THỨC copy')
a=['tpq',8,11,2004]
b=a.copy()
b[0]='TPQ'
print(a)
print(b)


print('4.PHƯƠNG THỨC clear ')
a=['thapquy','yêu em',8112004]
a.clear() #kq là []
print('xóa tất cả phần tử có trong list ',a)


print('#CÁC PHƯƠNG THỨC CẬP NHẬT')
print('1.PHƯƠNG THỨC append')
a=['haha','hihi',81112004,'tên :']
a.append('THAPQUY') #kq là thêm THAPQUY vào list : ['haha', 'hihi', 81112004, 'tên :', 'THAPQUY']
print('thêm THAPQUY vào list :',a)


#CHÚ Ý VÍ DỤ NÀY CHỖ append([2022)
a=[8112004,[2004]]
a.append([2022]) #kq là [8112004, [2004], [2022]]
print(a)


#KHÔNG NÊN apppend một list vào chính nó
a=[8112004,[2004]]
a.append(a) #kq là [8112004, [2004], [...]]
print(a)

print('2.PHƯƠNG THỨC extend')
a=['quy','TPQ',2022]
a.extend('PYTHON') #kq là ['quy', 'TPQ', 2022, 'P', 'Y', 'T', 'H', 'O', 'N']
print('xuất extend :',a)


a=['quy','TPQ',2022]
a.extend([2090])
print('chú ý vd này để phân biệt giữa append với extend :',a)

print('3.PHƯƠNG THỨC insert')
q=['mm','haizzz',8112004]
q.insert(1,'HAIZZZ')
print(q)

q=[8,11,2004]
q.insert(4,2022) #kq là [8,11,2004,2022]  VÌ vị trí i lớn hơn hoặc bằng thì kq đẩy về sau list
print(q)

q=['tpq',8112004,2022]
q.insert(-2,2004) #kq là ['tpq', 2004, 8112004, 2022]
print(q)


print('4.PHƯƠNG THỨC pop')
a=['variable','integer','float',123456,98765,3456]
a.pop(1) #kq là ['variable', 'float', 123456, 98765, 3456]
print('xóa đi phần tử ở vị trí 1 :',a)


a=['variable', 'float', 123456, 98765, 3456]
a.pop(-3) #kq là xóa đi phần tử -3 : ['variable', 'float', 98765, 3456]
print('xóa đi phần tử -3 :',a)


a=['variable', 'float', 123456, 98765, 3456]
a.pop() #kq là nếu cho rỗng kq sẽ ntn : ['variable', 'float', 123456, 98765] VÌ nếu ko có thì mặc định xóa phần tử cuối
print('nếu cho rỗng kq sẽ ntn :',a)

print('5.PHƯƠNG THỨC remove')
a=[1,2,4,8,9]
a.remove(1)#kq là [2, 4, 8, 9] VÌ xóa đi phần tử đầu tiên
print('xóa đi phần tử đầu là 1 :',a)

a=[1,2,43,6373]
a.remove(6373)
print('xóa đi phần tử 6373 :',a)


#a=[12,3647,75958]
#a.remove(121) #kq là ValueError: list.remove(x): x not in list VÌ 121 ko có trong list
#print(a)

print('#CÁC PHƯƠNG THỨC XỬ LÍ ')
print('1.PHƯƠNG THỨC reverse')
a=['tôi','tên','Qúy']
a.reverse() #kq là ['Qúy', 'tên', 'tôi']
print('xuất kq ra là đảo ngược :',a)

print('2.PHƯƠNG THỨC sort')
a=[1,23,5,655,685,35,2,55]
a.sort() #kq là [1, 2, 5, 23, 35, 55, 655, 685]
print('xuất ra kq được sắp xếp từ bé đến lớn :',a)



list1 = [4, 3, 5, 2, 1, 6, 2]
list1.sort(reverse=True) #kq là [6, 5, 4, 3, 2, 2, 1]
print('kết quả có reverse = True sẽ ntn :',list1)


list1 = [4, 3, 5, 2, 1, 6, 2]
list1.sort(reverse=False)#kq là [1, 2, 2, 3, 4, 5, 6]
print('kết quả có reverse = False sẽ ntn :',list1)


print('GIỚI THIỆU VỀ tuple TRONG python')
print('1.KHỞI TẠO tuple')
tuple1= (1, 2, 3, 4, (5, 6, 7), "A", 'B') #kq là  (1, 2, 3, 4, (5, 6, 7), 'A', 'B')
print('kết quả của tuple 1 :',tuple1)

#vd với tuple bằng rỗng
tuple2=() #kq là ()
print('xuất kq với tuple bằng rỗng :',tuple2)
#CHÚ Ý THÊM TRONG SÁCH PY

print('2.SỬ DỤNG tuple comprehension sẽ được học trong phần sau nhé ')

print('3.SỬ DỤNG constructor tuple ')
tuple0=tuple('TPQ') #kq là ('T', 'P', 'Q')
print('xuất tuple :',tuple0)

print('SỬ DỤNG tuple comprehension THÔNG QUA BƯỚC TRUNG GIAN')
#KHI CHƯA QUA TRUNG GIAN
tup=((i+2,i*2)for i in range(1,5))
print('khi chưa qua bước trung gian :',tup) #kq là <generator object <genexpr> at 0x00000275992D4C80> DO KO QUA BƯỚC TRUNG GIAN

#KHI QUA TRUNG GIAN
a=tuple(tup)  #kq là ((3, 2), (4, 4), (5, 6), (6, 8))
print('xuất tuple comprehension đã qua trung gian :',a)

print('4.MỘT SỐ TOÁN TỬ CỦA tuple')
#TOÁN TỬ +
tup=(8,11,2004)
tup1=tup+(8112004,8112021) #kq là (8, 11, 2004, 8112004, 8112021)
print('xuất toán tử + :',tup1)


a=(4,6,6,76)
a+=(442,42526,6262)
print(a)


#TOÁN TỬ *
tuple1=('tpq',8112004)
tuple2=tuple1 * 3 #kq là ('tpq', 8112004, 'tpq', 8112004, 'tpq', 8112004)
print(tuple2)


a=('hahaha',2022)
a*=5 #kq là ('hahaha', 2022, 'hahaha', 2022, 'hahaha', 2022, 'hahaha', 2022, 'hahaha', 2022)
print('nhân biến a 5 lần :',a)


tuple1=tuple('QUY') * 3 #kq là ('Q', 'U', 'Y', 'Q', 'U', 'Y', 'Q', 'U', 'Y')
print('xuất tuple constructor với toán tử * :',tuple1)


#TOÁN TỬ in
tuplee=(8,11,2004,'TPQ')
a= 'TPQ' in tuplee # kq là True
a1= 1111 in tuplee #kq là False
print('xuất "TPQ" có trong tuplle hay ko :',a)
print('xuất 1111 có trong tuplle hay ko :',a1)

print('5.INDEXING VÀ CẮT tuple TRONG py') # giống cắt chuỗi và list
tuple1=('quy','chào','rà',2021)
print(tuple1[0]) #kq là quy
print(tuple1[3]) #kq là 2021
#lấy vd tương tự và xem sách vd trong sách nhé


print('6.THAY ĐỔI NỘI DUNG tuple trong Py') #tuple ko thể thay nd LÍ DO VÀ TẠI SAO SẼ ĐƯỢC HỌC PHẦN SAU
#tup=('hahha',67890)
#tup[1]='hihi' # kq là báo lỗi vì tuple ko cho phép thay đổi nd VÀ list thì thay đổi được
#print(tup)

print('7.MA TRẬN ')
tup=((12,256,5,3456),(1314,25366,256),(345,45,56,56))
print('lấy (tuple 0) ở vị trí (thứ 2) trong tuple 0 đó : ',tup[0][2]) #kq là 5
print('lấy (tuple 2) ở vị trí (thứ 4) trong tuple 2 đó :',tup[2][-4]) #kq là 345
# cứ lấy ví dụ tương tự

print('CÁC PHƯƠNG THỨC XỬ LÍ ')
print('1.PHƯƠNG THỨC count')
tup=('a',34,25367,8,8,8,6,88,00,8,5,4,'a','a')
print('đếm số lượng số 8 xh bn lần :',tup.count(8)) #kq là 8 vì count là đếm và nó đếm được số 8 là 4
print('đếm số lượng "a" xuất hiện bao nhiêu lần trong biến tup : ',tup.count('a'))#kq là 3

print('2.PHƯƠNG THỨC index')
tup=('t',2,8,'pq')
print('xuất "pq" nó nằm vị trị mấy trong biến tup :',tup.index('pq',3,5)) # kq là 3
#print('xuất "tpq" nó nằm vị trị mấy trong biến tup :',tup.index('tpq')) # kq là BÁO LỖI VÌ KO TÌM THẤY 'tpq' trong biến

print('#GIỚI THIỆU VỀ HÀM id')
t = id (1234) #kq là 3076815383856
q = id('TPQ') #kq là 3076816008816
print('xuất 1234 có id là bn :',t)
print('xuất "TPQ" có id là bn :',q)

print('#TOÁN TỬ LÀ MỘT PHƯƠNG THỨC ')
a = 69
print('cho a = 69 :',a)
print(a+1)
print('#tương tự khi ta a+1 :',a.__add__(1)) #tương tự khi ta a+1
print('#tương tự khi ta a-9 :',a.__sub__(9)) #tương tự khi ta a-9
print('#tương tự khi ta a*2 :',a.__mul__(2)) #tương tự khi ta a*2
print('#tương tự khi 2+a :',a.__radd__(2)) #tương tự khi 2+a
print('#tương tự khi 9-a :',a.__rsub__(9)) #tương tự khi 9-a
print('#tương tự khi -a :',a.__neg__()) #tương tự khi -a

print('#GIỚI THIỆU VỀ set TRONG PYTHON') # set là sắp xếp ko có thứ tự
print('1.CÁCH KHỞI TẠO set')
set1={'chào RẮN python',2021} #kq là {'chào RẮN python',2021}
print(set1)
print('xuất kiểu dữ liệu của set1',type(set1)) # class < 'set' >
print('xuất độ dài của set1',len(set1)) # kq là 2

print('2.SỬ DỤNG set comprehension')
set2={value for value in range(6)} #kq là {0,1,2,3,4,5}
print('xuất kq có sd set comprehension :',set2)

print('3.SỬ DỤNG set constructor')
set3=set(('python py',123,'hahahah')) # kq là {'hahahah', 123, 'python py'}
print('xuát kq có sd set constructor :',set3)

print('#MỘT SỐ TOÁN TỬ set TRONG python')
print('1.TOÁN TỬ in')
print('tpq' in {'tpq',222,33,'hahahahahahahaha',7890,'py py pypy pypy'}) # kq là True       vì 'tpq' có trong set
print(8112004 in {'tpq',222,33,'hahahahahahahaha',7890,'py py pypy pypy'} ) # kq là False   vì 8112004 ko có trong set

print('2.TOÁN TỬ - ')
sett={'py','hahaha',8,11,2004,'tpq'} - {'py py','hahaha',8,11,2021,'py pypypypypypypyp'}
print('xuất kq của toán tử - :',sett) #kq là {'py', 2004, 'tpq'}

set11={'quy',88,11,2004} -{'quy',88,11,2004} # kq là set ()
print(set11)

print('3.TOÁN TỬ &')
set1={'yêu RẮN',567890,2012,} & {'py python',12345,2526272} # kq là  set ()
print('xuất kq của toán tử & :',set1)

set2= {'set set','settttt',3.4373,200000} & {'se(ttttttttt','set set',200000}  #kq là {'set set',200000}
print('xuất kq của toán tử & lần 2 :',set2)

set3= {'sake sake',27} & {'sake sake',27}   #kq là {27,'sake sake'}
print('xuất kq toán tử & lần 3 :',set3)

print('4.TOÁN TỬ |')
sett={1,2,3,'QQ'} | {12,2,4,'QQ'} # kq là {1, 2, 3, 4, 12, 'QQ'}        CHÚ Ý : set ko lấy các phần tử trùng lặp nhau
print('xuất kq của toán tử | :',sett)

settt= {'hhhhhh hhhhh',2345678,2345678,8} | {'hhhhhh hhhhh',2345678,2345678,8} # kq là {'hhhhhh hhhhh',2345678,8}
print('xuất kq có toán tử | lần 2 :',settt)

set11= {1,2,3,'py and py','python'} | {456,7,'hahaha'} #kq là {1, 2, 3, 'python', 7, 456, 'py and py', 'hahaha'}
print('xuất kq có toán tử | :',set11)

set111= {'qq',6789,'qqqqq'} | {'qqqqq',6789,'qq'} # kq là {6789, 'qqqqq', 'qq'}
print('xuất kq có toán tử | :',set111)

print('5.TOÁN TỬ ^')
sett= {'python','py',2020} ^ {8,'py'} # kq là {8, 'python', 2020}
print('xuất kq có toán tử ^ :',sett)

settt= {'love love',123} ^ {'love love',123} # kq là  set ()
print('xuất kq có toán tử ^  lần 2 :',settt)

print('#INDEXING VÀ CẮT set TRONG PYTHON')
print('vì SET không quan tâm đến vị trí của các phần tử nằm trong SET nên việc indexing và cắt SET không được hỗ trợ')

print('#CÁC THAO TÁC CƠ BẢN CỦA set')
print('1.Thêm một phần tử vào Set')
addd = {20,12,'love sake'}
addd.add(('love sake',1234)) # kq là  {'love sake', ('love sake', 1234), 20, 12}
print('vd thêm phần tử vào set :',addd)

a={1,2,3,4,5,'six',7,8} # kq là {1, 2, 3, 4, 5, 7, 8, ('nine', 10), 'six'}
a.add(('nine',10))
print('vd về thêm phần tử váo set lần 2 :',a)

print('2.Xoá một phần tử bằng discard')
a1={1,2,3,4,5,'six',7,8}
a1.discard(('six')) # kq là {1, 2, 3, 4, 5, 7, 8}
print('vd về xóa một phần tử trong set :',a1)
#CHÚ Ý : có thể sd đc pop , remove , clear , ........Sử dụng remove nếu ko có trong set thì báo lỗi còn discard thì ko





































































































































































































































































































































