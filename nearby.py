import pymol
import os

path = r"D:\2023\analyze\nearby\domain"


def exalt_sele_resi(sele_name):
    res_list = pymol.cmd.get_model(sele_name).atom
    # 根据序列号进行排序
    res_list.sort(key=lambda x: x.resi_number)
    # 将残基序列号存储到列表中
    res_num_list = [r.resi_number for r in res_list]
    res_num_list = list(set(res_num_list))
    res_num_list.sort()
    return res_num_list


if __name__ == "__main__":
    pymol.finish_launching()
    near_rna_lis = []
    near_domain_lis = []
    for filename in os.listdir(path):
        if ".pdb" in filename or ".gro" in filename:
            filepath = os.path.join(path,filename)
            pymol.cmd.load(filepath, 'protein_RNA')
            pymol.cmd.select("RNA", "polymer.nucleic")
            pymol.cmd.select("connect_domain", "polymer.protein and resi 122-277")
            pymol.cmd.select("near_rna", "byres (rna around 4) and polymer.protein and resi 122-277")
            pymol.cmd.select("near_protein", "byres (connect_domain around 4) and polymer.nucleic")
            exalt_rna_resi = exalt_sele_resi("near_protein")
            exalt_domain_resi = exalt_sele_resi("near_rna")
            near_rna_lis.append(exalt_rna_resi)
            near_domain_lis.append(exalt_domain_resi)
    print("="*20)
    print("this is near_rna_lis")
    dic = {}
    for i in near_rna_lis:
        print(i)
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
    print(dic)
    dic = {}
    print("=" * 20)
    print("this is near_domain_lis")
    for i in near_domain_lis:
        print(i)
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1
    print(dic)
    print(len(dic))
    for j in dic:
        if dic[j] >12:
            print("{}-{}".format(j,dic[j]))
    #Trp, Arg, Try