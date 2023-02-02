using MocksETH as sETHToken
using MockSlotSettlementRegistry as slotSettlementRegistry

methods {
    //// Regular methods
    totalETHReceived() returns (uint256) envfree
    isKnotRegistered(bytes32) returns (bool) envfree

    //// Resolving external calls
	// stakeHouseUniverse
	stakeHouseKnotInfo(bytes32) returns (address,address,address,uint256,uint256,bool) => DISPATCHER(true)
    memberKnotToStakeHouse(bytes32) returns (address) => DISPATCHER(true) // not used directly by Syndicate
    // stakeHouseRegistry
    getMemberInfo(bytes32) returns (address,uint256,uint16,bool) => DISPATCHER(true) // not used directly by Syndicate
    // slotSettlementRegistry
	slotSettlementRegistry.stakeHouseShareTokens(address) returns (address) envfree
	slotSettlementRegistry.currentSlashedAmountOfSLOTForKnot(bytes32) returns (uint256)
	slotSettlementRegistry.numberOfCollateralisedSlotOwnersForKnot(bytes32) returns (uint256) envfree
	slotSettlementRegistry.getCollateralisedOwnerAtIndex(bytes32, uint256) returns (address) envfree
	slotSettlementRegistry.totalUserCollateralisedSLOTBalanceForKnot(address, address, bytes32) returns (uint256)
    // sETH
    sETHToken.balanceOf(address) returns (uint256) envfree
    // ERC20
    name()                                returns (string)  => DISPATCHER(true)
    symbol()                              returns (string)  => DISPATCHER(true)
    decimals()                            returns (string) envfree => DISPATCHER(true)
    totalSupply()                         returns (uint256) => DISPATCHER(true)
    balanceOf(address)                    returns (uint256) => DISPATCHER(true)
    allowance(address,address)            returns (uint)    => DISPATCHER(true)
    approve(address,uint256)              returns (bool)    => DISPATCHER(true)
    transfer(address,uint256)             returns (bool)    => DISPATCHER(true)
    transferFrom(address,address,uint256) returns (bool)    => DISPATCHER(true)

    //// Harnessing
    // harnessed variables
    accruedEarningPerCollateralizedSlotOwnerOfKnot(bytes32,address) returns (uint256) envfree
    totalETHProcessedPerCollateralizedKnot(bytes32) returns (uint256) envfree
    sETHStakedBalanceForKnot(bytes32,address) returns (uint256) envfree
    sETHTotalStakeForKnot(bytes32) returns (uint256) envfree
    // harnessed functions
    deRegisterKnots(bytes32) 
    deRegisterKnots(bytes32,bytes32)
    stake(bytes32,uint256,address)
    stake(bytes32,bytes32,uint256,uint256,address)
    unstake(address,address,bytes32,uint256)
    unstake(address,address,bytes32,bytes32,uint256,uint256)
    claimAsStaker(address,bytes32)
    claimAsStaker(address,bytes32,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32)
    claimAsCollateralizedSLOTOwner(address,bytes32,bytes32)
    registerKnotsToSyndicate(bytes32)
    registerKnotsToSyndicate(bytes32,bytes32)
    addPriorityStakers(address)
    addPriorityStakers(address,address)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32)
    batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32)

    // added by neumo
    getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32) returns(uint256) envfree
    sETHUserClaimForKnot(bytes32, address) returns(uint256) envfree
    PRECISION() returns(uint256) envfree
    lastAccumulatedETHPerFreeFloatingShare(bytes32) returns(uint256) envfree
    owner() returns (address) envfree
    updatePriorityStakingBlock(uint256)
    accumulatedETHPerFreeFloatingShare() returns(uint256) envfree
    accumulatedETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    isNoLongerPartOfSyndicate(bytes32) returns (bool) envfree
    priorityStakingEndBlock() returns (uint256) envfree
    isPriorityStaker(address) returns (bool) envfree
    lastSeenETHPerCollateralizedSlotPerKnot() returns(uint256) envfree
    lastSeenETHPerFreeFloating() returns(uint256) envfree
    calculateETHForFreeFloatingOrCollateralizedHolders() returns(uint256) envfree
    calculateUnclaimedFreeFloatingETHShare(bytes32, address) returns(uint256) envfree
    previewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    getETHBalance(address) returns(uint256) envfree
    batchPreviewUnclaimedETHAsFreeFloatingStaker(address, bytes32) returns(uint256) envfree
    calculateNewAccumulatedETHPerFreeFloatingShare() returns (uint256) envfree
    batchPreviewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    previewUnclaimedETHAsCollateralizedSlotOwner(address, bytes32) returns(uint256) envfree
    getUnprocessedETHForAllFreeFloatingSlot() returns (uint256) envfree
    getUnprocessedETHForAllCollateralizedSlot() returns (uint256) envfree
    numberOfRegisteredKnots() returns (uint256) envfree
    totalFreeFloatingShares() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedSharePerKnot() returns (uint256) envfree
    totalClaimed() returns (uint256) envfree
    calculateCollateralizedETHOwedPerKnot() returns (uint256) envfree
    calculateNewAccumulatedETHPerCollateralizedShare(uint256) returns (uint256) envfree
    updateAccruedETHPerShares()
    updateCollateralizedSlotOwnersAccruedETH(bytes32)
    initialize(address, uint256, address, bytes32)
    isInitialized() returns(bool) envfree
}

/// We defined additional functions to get around the complexity of defining dynamic arrays in cvl. We filter them in 
/// normal rules and invariants as they serve no purpose.
definition notHarnessCall(method f) returns bool = 
    f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32).selector
    && f.selector != batchUpdateCollateralizedSlotOwnersAccruedETH(bytes32,bytes32).selector
    && f.selector != deRegisterKnots(bytes32).selector
    && f.selector != deRegisterKnots(bytes32,bytes32).selector
    && f.selector != stake(bytes32,uint256,address).selector
    && f.selector != stake(bytes32,bytes32,uint256,uint256,address).selector
    && f.selector != unstake(address,address,bytes32,uint256).selector
    && f.selector != unstake(address,address,bytes32,bytes32,uint256,uint256).selector
    && f.selector != claimAsStaker(address,bytes32).selector
    && f.selector != claimAsStaker(address,bytes32,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32).selector
    && f.selector != claimAsCollateralizedSLOTOwner(address,bytes32,bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32).selector
    && f.selector != registerKnotsToSyndicate(bytes32,bytes32).selector
    && f.selector != addPriorityStakers(address).selector
    && f.selector != addPriorityStakers(address,address).selector
    && f.selector != batchPreviewUnclaimedETHAsFreeFloatingStaker(address,bytes32).selector
    && f.selector != getETHBalance(address).selector
    && f.selector != calculateCollateralizedETHOwedPerKnot().selector
    && f.selector != calculateNewAccumulatedETHPerCollateralizedShare(uint256).selector
    && f.selector != getCorrectAccumulatedETHPerFreeFloatingShareForBLSPublicKey(bytes32).selector
    && f.selector != isInitialized().selector
    && f.selector != initialize(address,uint256,address,bytes32).selector
    && f.selector != getETHBalance(address).selector;


/// Functions with onlyOwner modifier.
definition onlyOwnerFunctions(method f) returns bool = 
    f.selector == deRegisterKnots(bytes32[]).selector
    || f.selector == registerKnotsToSyndicate(bytes32[]).selector
    || f.selector == addPriorityStakers(address[]).selector
    || f.selector == updatePriorityStakingBlock(uint256).selector;


/// Corrollary that can be used as requirement after sETH solvency is proven.
function sETHSolvencyCorrollary(address user1, address user2, bytes32 knot) returns bool {
    return sETHStakedBalanceForKnot(knot,user1) + sETHStakedBalanceForKnot(knot,user2) <= sETHTotalStakeForKnot(knot);
}

/*-------------------------------------------------
|                  Unit tests                      |
--------------------------------------------------*/

/**
 * √ An unregistered knot can not be deregistered.
 */
rule canNotDeregisterUnregisteredKnot() {
    bytes32 knot; env e;
    require !isKnotRegistered(knot);

    deRegisterKnots@withrevert(e, knot);

    assert lastReverted, "deRegisterKnots must revert if knot is not registered";
}

/**
 * √ Injected Bug 1: when unstaking, if contract balance is less than amount
 * call must revert
 */
rule unstakeNotEnoughBalance() {

    env e;

    address unclaimedETHRecipient;
    address sETHRecipient;
    bytes32 blsPubKey;
    uint256 sETHAmount;
    
    uint256 balanceContract = sETHToken.balanceOf(currentContract);

    require balanceContract < sETHAmount;

    unstake@withrevert(e, unclaimedETHRecipient, sETHRecipient, blsPubKey, sETHAmount);

    assert lastReverted, "Not enough balance";
}


/**
 * X sETHUserClaimForKnot must account for accumulatedETHPerShare after unstake call
 * [catches Injected bug 9]
 */
rule sETHUserClaimForKnotAfterUnstake() {

    env e;

    address unclaimedETHRecipient;
    address sETHRecipient;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    uint256 accumulatedETHPerSharePre = lastAccumulatedETHPerFreeFloatingShare(blsPubKey) > 0 ?
        lastAccumulatedETHPerFreeFloatingShare(blsPubKey) :
        accumulatedETHPerFreeFloatingShare();
    uint256 sETHUserClaimForKnotPre = sETHUserClaimForKnot(blsPubKey, e.msg.sender);
    uint256 sETHStakedBalanceForKnotPre = sETHStakedBalanceForKnot(blsPubKey, e.msg.sender);
    require sETHUserClaimForKnotPre ==
                (accumulatedETHPerSharePre * sETHStakedBalanceForKnotPre) / PRECISION();
    
    unstake(e, unclaimedETHRecipient, sETHRecipient, blsPubKey, sETHAmount);

    uint256 accumulatedETHPerSharePost = lastAccumulatedETHPerFreeFloatingShare(blsPubKey) > 0 ?
        lastAccumulatedETHPerFreeFloatingShare(blsPubKey) :
        accumulatedETHPerFreeFloatingShare();
    uint256 sETHUserClaimForKnotPost = sETHUserClaimForKnot(blsPubKey, e.msg.sender);
    uint256 sETHStakedBalanceForKnotPost = sETHStakedBalanceForKnot(blsPubKey, e.msg.sender);

    assert sETHUserClaimForKnotPost ==
                (accumulatedETHPerSharePost * sETHStakedBalanceForKnotPost) / PRECISION(), "Wrong sETHUserClaimForKnot";
}

/**
 * √ Initialize function can only be called once
 */
rule cannotInitializeTwice(method f) filtered {
    f -> f.selector == initialize(address, uint256, address[], bytes32[]).selector
}{

    env e;

    bool isInitialized = isInitialized();

    require !isInitialized;

    calldataarg args1;
    calldataarg args2;

    f(e, args1);
    f@withrevert(e, args2);

    assert lastReverted, "Contract instance has already been initialized";

}

/**
 * √ Owner after initialization must be the contractOwner
 * After initialization, knot identified by blsPubKey must be registered
 * After initialization, priorityStaker must be a priority staker
 */
rule afterInitializationChecks(){

    env e;

    bool isInitialized = isInitialized();

    require !isInitialized;

    address contractOwner;
    uint256 priorityStakingEndBlock;
    address priorityStaker;
    bytes32 blsPubKey;

    initialize(e, contractOwner, priorityStakingEndBlock, priorityStaker, blsPubKey);

    assert owner() == contractOwner, "Owner not set properly";
    assert isKnotRegistered(blsPubKey), "Knot was not registered correctly";
    assert priorityStakingEndBlock > e.block.number => (isPriorityStaker(priorityStaker) && priorityStakingEndBlock() == priorityStakingEndBlock), "Priority staker and/or priorityStakingEndBlock were not registered correctly";

}

/**
 * √ updatePriorityStakingBlock: priorityStakingEndBlock is set correctly after call
 */
rule updatePriorityStakingBlockCheck(){

    env e;
    
    uint256 priorityStakingEndBlock;

    updatePriorityStakingBlock(e, priorityStakingEndBlock);

    assert priorityStakingEndBlock() == priorityStakingEndBlock, "PriorityStakingEndBlock was not set correctly";

}

/**
 * √ Functions with modifier onlyOwner can only be called by the owner
 */
rule onlyOwnerFunctionsOnlyCallableByOwner(method f) filtered {
    f -> onlyOwnerFunctions(f)
}{

    env e;

    require e.msg.sender != owner();

    calldataarg args;
    f@withrevert(e, args);

    assert lastReverted, "Ownable: caller is not the owner";

}

/**
 * √ stake: onBehalfOf cannot be zero address.
 */
rule stakeOnBehalfOfCannotBeZeroAddress() {

    env e;

    address onBehalfOf;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    require onBehalfOf == 0;

    stake@withrevert(e, blsPubKey, sETHAmount, onBehalfOf);

    assert lastReverted, "onBehalfOf cannot be equal to address(0)";

}

/**
 * √ stake: sETHAmount cannot be less than one gwei.
 */
rule stakeSETHAmountCannotBeLessThanOneGwei() {

    env e;

    address onBehalfOf;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    require sETHAmount < 1000000000;

    stake@withrevert(e, blsPubKey, sETHAmount, onBehalfOf);

    assert lastReverted, "sETHAmount cannot be less than one gwei";

}

/**
 * √ stake: Knot must be registered.
 */
rule stakeKnotMustBeRegistered() {

    env e;

    address onBehalfOf;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    require !isKnotRegistered(blsPubKey) || isNoLongerPartOfSyndicate(blsPubKey);

    stake@withrevert(e, blsPubKey, sETHAmount, onBehalfOf);

    assert lastReverted, "Knot must be registered";

}

/**
 * √ stake: Only priority staker can stake before priority staking end block.
 */
rule stakeOnlyPriorityStakerCanStakeBeforeEndBlock() {

    env e;

    address onBehalfOf;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    require e.block.number < priorityStakingEndBlock() && !isPriorityStaker(onBehalfOf);

    stake@withrevert(e, blsPubKey, sETHAmount, onBehalfOf);

    assert lastReverted, "Only priority staker can stake before priority staking end block";

}

/**
 * √ stake: Total staked cannot surpass 12 ether.
 */
rule stakeTotalStakedCannotSurpassTwelveEther() {

    env e;

    address onBehalfOf;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    stake(e, blsPubKey, sETHAmount, onBehalfOf);

    assert sETHTotalStakeForKnot(blsPubKey) <= 12000000000000000000, "Total staked cannot surpass 12 ether";

}

/**
 * √ when staking, if msg.sender balance is less than amount
 * call must revert
 */
rule stakeNotEnoughBalance() {

    env e;

    address onBehalfOf;
    bytes32 blsPubKey;
    uint256 sETHAmount;
    
    uint256 balanceSender = sETHToken.balanceOf(e.msg.sender);

    require balanceSender < sETHAmount;

    stake@withrevert(e, blsPubKey, sETHAmount, onBehalfOf);

    assert lastReverted, "Not enough balance";
}

/**
 * unstake: sETHRecipient cannot be zero address.
 * (when testing with bug11.patch the rule still passes, because sETH.transfer(_sETHRecipient, _sETHAmount)
 * violates the addressZeroHasNoBalance() invariant. Leaving rule just in case)
 */
rule unstakeSETHRecipientCannotBeZeroAddress() {

    env e;

    address unclaimedETHRecipient;
    address sETHRecipient;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    require sETHRecipient == 0;

    unstake@withrevert(e, unclaimedETHRecipient, sETHRecipient, blsPubKey, sETHAmount);

    assert lastReverted, "sETHRecipient cannot be equal to address(0)";

}

/**
 * √ unstake: cannot unstake more than the knot balance
 */
rule unstakeCannotUnstakeMoreThanTheKnotBalance() {

    env e;

    address unclaimedETHRecipient;
    address sETHRecipient;
    bytes32 blsPubKey;
    uint256 sETHAmount;

    require sETHAmount > sETHStakedBalanceForKnot(blsPubKey, e.msg.sender);

    unstake@withrevert(e, unclaimedETHRecipient, sETHRecipient, blsPubKey, sETHAmount);

    assert lastReverted, "Cannot unstake more than the knot balance";

}



/*-------------------------------------------------
|         Invariants, ghosts and hooks             |
--------------------------------------------------*/

/**
 * Ghost 1 to account for the total stake of sETH
 */
ghost mathint sETHTotalStake1 {
    init_state axiom sETHTotalStake1 == 0 ;
}

/**
 * Ghost 2 to account for the total stake of sETH
 */
ghost mathint sETHTotalStake2 {
    init_state axiom sETHTotalStake2 == 0 ;
}
    
/**
 * Hook to update the ghost sETHTotalStake1 on every change to the mapping sETHTotalStakeForKnot
 */
hook Sstore sETHTotalStakeForKnot[KEY bytes32 blsPubKey] uint256 newValue (uint256 oldValue) STORAGE {
    sETHTotalStake1 = sETHTotalStake1 + newValue - oldValue;
}
    
/**
 * Hook to update the ghost sETHTotalStake2 on every change to the mapping sETHStakedBalanceForKnot
 */
hook Sstore sETHStakedBalanceForKnot[KEY bytes32 blsPubKey][KEY address account] uint256 newValue (uint256 oldValue) STORAGE {
    sETHTotalStake2 = sETHTotalStake2 + newValue - oldValue;
}

/**
 * Address 0 must have zero sETH balance.
 */
invariant addressZeroHasNoBalance()
    sETHToken.balanceOf(0) == 0

/**
 * If knot is no longer part of syndicate, it must be registered
 */
invariant noLongerPartOfSyndicateImpliesRegistered(bytes32 blsPubKey)
    isNoLongerPartOfSyndicate(blsPubKey) => isKnotRegistered(blsPubKey)

/**
 * totalETHProcessedPerCollateralizedKnot always less than or equal than accumulatedETHPerCollateralizedSlotPerKnot.
 */
invariant accumulatedETHPerCollateralizedSlotPerKnotGTEtotalETHProcessedPerCollateralizedKnot(bytes32 blsPubKey)
    totalETHProcessedPerCollateralizedKnot(blsPubKey) <= accumulatedETHPerCollateralizedSlotPerKnot()

/**
 * sETHTotalStake1 and sETHTotalStake2 must match.
 */
invariant sETHTotalStakeGhostsMatch()
    sETHTotalStake1 == sETHTotalStake2