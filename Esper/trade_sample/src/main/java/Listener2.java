import com.espertech.esper.common.client.EventBean;
import com.espertech.esper.runtime.client.EPRuntime;
import com.espertech.esper.runtime.client.EPStatement;
import com.espertech.esper.runtime.client.UpdateListener;

import java.util.HashMap;

/** 实现UpdateListener接口，来定义事件的后置处理过程 **/
public class Listener2 implements UpdateListener {

    public void update(EventBean[] eventBeans, EventBean[] eventBeans1, EPStatement epStatement, EPRuntime epRuntime) {
        try {
            if(epStatement.getName().equals("Average-Price-of-A-30Sec")){
                double avgPrice30Sec = (double) eventBeans[0].get("avgPrice30Sec");
                String company = (String) eventBeans[0].get("company");
                System.out.printf("Average Price %s(time: 30 seconds): %.4f\n", company, avgPrice30Sec);
            }else if(epStatement.getName().equals("Average-Price-of-A-30SecBatch")){
                double avgPrice30SecBatch = (double) eventBeans[0].get("avgPrice30SecBatch");
                String company = (String) eventBeans[0].get("company");
                System.out.printf("Average Price %s(time_batch: 30 seconds): %.4f\n", company, avgPrice30SecBatch);
            }else if(epStatement.getName().equals("Average-Price-of-All-30SecBatch")){
                for (EventBean e: eventBeans){
                    Object o = e.getUnderlying();
                    System.out.printf("%s\t", o.toString());
                }
                System.out.println("\n");
            }else if(epStatement.getName().equals("Pattern")){
                for (EventBean e: eventBeans){
                    Object o = e.getUnderlying();
                    System.out.printf("%s\t", o.toString());
                }
                System.out.println("\n");
            }else if(epStatement.getName().equals("Average-Price-Difference")){
                double priceA = (double) eventBeans[0].get("priceA");
                double priceB = (double) eventBeans[0].get("priceB");
                double priceDiff = (double) eventBeans[0].get("priceDiff");
                System.out.printf("Average Price A: %.4f\tAverage Price B: %.4f\tPrice Diff: %.4f\n", priceA, priceB, priceDiff);
            }
        }catch(Exception e) {
            e.printStackTrace();
        }
    }
}
