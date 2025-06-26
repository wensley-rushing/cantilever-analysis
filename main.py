# ----------------------------------------
# Cantilever Retaining Wall
# ----------------------------------------


# Gerekli kütüphaneler import ediliyor.
import xara
import veux

# Çağırılan opensees komutları ile oluşturulan her şeyi temizle.

# Model oluşturacağımız uzayı tanımlıyoruz.
model = xara.Model('basic','-ndm',2,'-ndf',2) # 2 yönde yer değiştirme, düzlem dışı yer değiştirmeler ve dönmeler kısıtlı.

# Düğüm noktaları koordinatları (m)
model.node(1, 0.0,  0.0)
model.node(2, 0.0,  0.5)
model.node(3, 0.5, 0.0)
model.node(4, 0.5, 0.5)
model.node(5, 1.0, 0.0)
model.node(6, 1.0, 0.5)
model.node(7, 2.0, 0.0)
model.node(8, 2.0, 0.5)
model.node(9, 0.56, 1.5)
model.node(10, 1.0, 1.5)
model.node(11, 0.63, 2.5)
model.node(12, 1.0, 2.5)
model.node(13, 0.69, 3.5)
model.node(14, 1.0, 3.5)
model.node(15, 0.75, 4.5)
model.node(16, 1.0, 4.5)


# Mesnet bilgileri
# Sistemde 6 adet kayıcı mesnet(ikisi 1 düğümünde) bulunmakta.
model.fix(1, 1, 1)
model.fix(2, 1, 0)
model.fix(3, 0, 1)
model.fix(5, 0, 1)
model.fix(7, 0, 1)

# Malzeme tanımlama
model.nDMaterial('ElasticIsotropic', 1, 32000000.0, 0.2)

# Eleman tanımlama
# Elemanlarımız üçgen eleman, düzlem-şekil değiştirme sistemi
model.element('Tri31', 1, 1, 4, 2, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 2, 3, 4, 1, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 3, 3, 6, 4, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 4, 5, 6, 3, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 5, 5, 8, 6, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 6, 7, 8, 5, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 7, 4, 10, 9, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 8, 6, 10, 4, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 9, 9, 12, 11, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 10, 10, 12, 9, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 11, 11, 14, 13, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 12, 12, 14, 11, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 13, 13, 16, 15, 1.0, 'PlaneStrain', 1)
model.element('Tri31', 14, 14, 16, 13, 1.0, 'PlaneStrain', 1)

# Zaman serisi tanımlama
model.timeSeries("Linear", 1)

# Yük sınıfı tanımlama
# Tek tip yükümüz var.
model.pattern("Plain", 1, 1)

# Yükler tanımlanır. (kN)
model.load(7, -24.0, 0.0)
model.load(8, -24.0, -60.0)
model.load(6, -41.0, -60.0)
model.load(10,-73.0, 0.0)
model.load(12,-56.0, 0.0)
model.load(14,-38.0, 0.0)
model.load(16,-14.0, 0.0)

model.system('BandSPD')
model.numberer('RCM')
model.constraints('Plain')
model.integrator('LoadControl', 1.0)

# Çözüm algoritması
model.algorithm('Linear')
 
# Analiz türü
model.analysis('Static')
model.analyze(1) # Analizin kaç kez yapılacağını belirtir.

# ---------------------------------
# Çıktı
# ---------------------------------

# Yer değiştirmeler
for i in range(1,17):
    print(i,"numaralı düğüm x=",model.nodeDisp(i,1),"m  -  y=",model.nodeDisp(i,2),"m")

# Modeli çizdir
veux.serve(veux.render(model, state=model.nodeDisp, ndf=2))

