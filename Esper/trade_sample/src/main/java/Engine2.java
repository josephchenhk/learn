import com.espertech.esper.common.client.EPCompiled;
import com.espertech.esper.common.client.configuration.Configuration;
import com.espertech.esper.compiler.client.CompilerArguments;
import com.espertech.esper.compiler.client.EPCompileException;
import com.espertech.esper.compiler.client.EPCompiler;
import com.espertech.esper.compiler.client.EPCompilerProvider;
import com.espertech.esper.runtime.client.*;
import com.opencsv.exceptions.CsvException;

import java.io.IOException;

public class Engine2 {

    static String[] rowData;
    static String timeStr;
    static java.sql.Timestamp ts;
    static String company;
    static Double px;

    public static void main(String[] args) throws IOException, CsvException, EPCompileException, EPDeployException, InterruptedException {
        System.out.println("Test Esper Engine");

        EPCompiler compiler = EPCompilerProvider.getCompiler();
        Configuration configuration = new Configuration();
        configuration.getCommon().addEventType("Event", Event.class);

        /* 描述复杂事件 Test different statements */

        // 计算company A的30s移动窗口的平均价，每次遇到company A的Event都会触发Listener
        String epl = "@name('Average-Price-of-A-30Sec') select avg(px) as avgPrice30Sec, company from Event.win:time(30 sec) where company=\"A\";";
        // 计算company A的30s移动窗口的平均价，累计30s才会触发一次Listener
        // String epl = "@name('Average-Price-of-A-30SecBatch') select avg(px) as avgPrice30SecBatch, company from Event.win:time_batch(30 sec) where company=\"A\";";
        // 计算所有公司（A，B，C，D）的30s移动窗口的平均价，累计30s才会触发一次Listener [注意：如果用Event.win:time(30 sec)，则每次遇到Event都会触发Listener，这样每次只能得到该Event对应的公司的30s均价，因为前面的触发事件已经被销毁了]
        // String epl = "@name('Average-Price-of-All-30SecBatch') select avg(px) as avgPrice30Sec, company from Event.win:time_batch(30 sec) group by company;";
        // 找最近邻的A和B，计算两者的px价格之差（每次遇到事件A，就会寻找下一个事件B，当找到之后触发Listener；然后重新开始等待事件A）
        // String epl = "@name('Pattern') select a.px, b.px, (a.px-b.px) as diff from pattern [every a=Event(company=\"A\") -> b=Event(company=\"B\")];";
        // 创建一个context
        // String epl = "create context DiffContext partition by company from Event(company=\"A\" or company=\"B\");\n" +
        //         "@name('Named-Window') context DiffContext select avg(px), company from Event.win:length(2);";
        // 分别监控A和B最近2次的价格平均值，计算两者均值的价格差
        // String epl = "insert into A select avg(px) as price, company from Event(company=\"A\").win:length(2);\n" +
        //         "insert into B select avg(px) as price, company from Event(company=\"B\").win:length(2);\n" +
        //         "@name('Average-Price-Difference')select A.price as priceA, B.price as priceB, (A.price-B.price) as priceDiff from A.win:length(1), B.win:length(1);";


        CompilerArguments compilerArguments = new CompilerArguments(configuration);
        EPRuntime runtime = EPRuntimeProvider.getDefaultRuntime(configuration);
        EPCompiled compiled = compiler.compile(epl, compilerArguments);
        // 部署方法1：
         EPDeployment deployment = runtime.getDeploymentService().deploy(compiled);
         deployment.getStatements()[deployment.getStatements().length-1].addListener(new Listener2());
        // 部署方法2：
        // runtime.getDeploymentService().deploy(compiled, new DeploymentOptions().setDeploymentId("test-deployment"));
        // runtime.getDeploymentService().getStatement("test-deployment","Average-Price-Difference").addListener(new Listener2());

        /* 代入数据进行实验 */
        String fileName = "/Users/joseph/Dropbox/code/learn/Q/table.csv";
        DataReader dr = new DataReader(fileName);
        // dr.r.forEach(x -> System.out.println(Arrays.toString(x)));
        for(int i=1; i<dr.r.size(); i++){
            rowData = dr.r.get(i);
            timeStr = rowData[0];
            company = rowData[1];
            px = Double.valueOf(rowData[2]);
            // convert time string to timestamp
            ts = java.sql.Timestamp.valueOf("2021-01-04 "+timeStr) ;
            Event event = new Event(ts, company, px);
            System.out.println("    " + i + " " + event);
            runtime.getEventService().sendEventBean(event, "Event");
            Thread.sleep(1000);
        }
    }
}
