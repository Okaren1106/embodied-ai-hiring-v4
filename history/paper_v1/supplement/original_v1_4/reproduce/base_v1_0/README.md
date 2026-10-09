# 精简复算入口

Python 3.10及以上。表格和严格语境汇总只用标准库，无需联网或原工作区。

```powershell
python reproduce.py --output generated
```

输出目录必须尚不存在。入口先核对inputs/manifest.json与锁定方法协议，校验唯一成员、唯一状态、合法状态及全部20个情景格，缺失不可填0。成功才发布输出目录。

5组主表共8份CSV由已验收原表重排，表5严格G由84个不同状态键、303个情景成员重新汇总。figure_data.json提供3图全部源值。其他语境及公司点值保留作附录，不新增语义判断。可选重画PNG/SVG：

```powershell
python -m pip install -r requirements-figures.txt
python reproduce.py --output generated_with_figures --figures
```

绘图优先Microsoft YaHei/SimHei；其他系统须配置可用中文字体。不同字体或绘图库版本的图像字节可能不同，以数值表一致为准。

frozen_input_manifest.csv记录完整冻结源文件的原路径和哈希，但入口不打开这些路径；原绝对路径只作来源追溯。handoff_manifest.csv保留Grok/DS原交付身份。当前精简包不是V3全量4,402,134格的重建环境；该工作已由V3交付的独立复算材料承担。
